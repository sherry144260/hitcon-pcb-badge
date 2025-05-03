import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta
import pymongo


@dataclass
class Constants:
    DATABASE_NAME = "game_logic"
    ATTACK_HISTORY_COLLECTION = "attack_history"

    STATION_SCORE_LB = -1000
    STATION_SCORE_UB = 1000
    STATION_NEUTRAL_LB = -300
    STATION_NEUTRAL_UB = 300

    STATION_SCORE_DECAY_INTERVAL = 30 # seconds
    STATION_SCORE_DECAY_AMOUNT = 10


const = Constants()


def clamp(value: int, min_value: int, max_value: int) -> int:
    """
    Clamp the value between min_value and max_value.
    """
    return max(min(value, max_value), min_value)


def sign(value: int) -> int:
    """
    Return the sign of the value.
    """
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0


class _GameLogic:
    def __init__(self, mongo_client: pymongo.AsyncMongoClient, start_time: datetime = None):
        # TODO: maybe use config to update constants
        self.db = mongo_client[const.DATABASE_NAME]
        self.attack_history = self.db[const.ATTACK_HISTORY_COLLECTION]

        if start_time is None:
            start_time = datetime.now()
        self.start_time = start_time

    async def clear_attack_history(self):
        await self.attack_history.delete_many({})

    async def attack_station(self, player_id: int, station_id: int, amount: int, timestamp: datetime):
        """
        This method is called when a player attacks a station.
        This will add a record in the database. The station's score will be calculated
        based on the history of attacks.
        """
        await self.attack_history.insert_one({
            "player_id": player_id,
            "station_id": station_id,
            "amount": amount,
            "timestamp": timestamp,
        })

    async def get_station_score(self, station_id: int, before: datetime = None) -> int:
        # TODO: cache the results
        if before is None:
            before = datetime.now()

        cursor = self.attack_history.find(
            {
                "station_id": station_id,
                "timestamp": {"$lt": before},
            }
        ).sort("timestamp", pymongo.ASCENDING)

        total_score = 0
        time_pointer = self.start_time

        def proceed(until: datetime):
            nonlocal time_pointer
            nonlocal total_score
            # Decay the score based on the time passed
            while time_pointer <= until:
                time_pointer += timedelta(seconds=const.STATION_SCORE_DECAY_INTERVAL)
                total_score += -1 * sign(total_score) * min(const.STATION_SCORE_DECAY_AMOUNT, abs(total_score))

        async for record in cursor:
            proceed(record["timestamp"])
            total_score = clamp(total_score + record["amount"], const.STATION_SCORE_LB, const.STATION_SCORE_UB)

        proceed(before)
        return total_score


async def test_station_score_history():
    const.STATION_SCORE_DECAY_INTERVAL = 1
    eps = 0.1

    time_base = datetime.now()
    gl = _GameLogic(pymongo.AsyncMongoClient("mongodb://localhost:27017"), time_base)
    await gl.clear_attack_history()

    # Simulate
    scores = [100, 200, 300, -50, -100, -200, -300, -400, -500, -600, 400, 400, 400, 400, 400, 400, 400]
    for i, score in enumerate(scores):
        await gl.attack_station(1, 1, score, time_base + timedelta(seconds=i + 0.5))

    # Test
    total_score = 0
    for i in range(len(scores)):
        # decay the score
        if total_score > 0:
            total_score = max(0, total_score - const.STATION_SCORE_DECAY_AMOUNT)
        elif total_score < 0:
            total_score = min(0, total_score + const.STATION_SCORE_DECAY_AMOUNT)

        assert total_score == await gl.get_station_score(1, time_base + timedelta(seconds=i + eps))

        # add the score
        total_score = clamp(total_score + scores[i], const.STATION_SCORE_LB, const.STATION_SCORE_UB)

        assert total_score == await gl.get_station_score(1, time_base + timedelta(seconds=i + 0.5 + eps))

    for i in range(len(scores), len(scores) + 10):
        # decay the score
        if total_score > 0:
            total_score = max(0, total_score - const.STATION_SCORE_DECAY_AMOUNT)
        elif total_score < 0:
            total_score = min(0, total_score + const.STATION_SCORE_DECAY_AMOUNT)

        assert total_score == await gl.get_station_score(1, time_base + timedelta(seconds=i + eps))


if __name__ == "__main__":
    asyncio.run(test_station_score_history())
