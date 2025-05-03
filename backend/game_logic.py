from packet_processor import PacketProcessor
from schemas import ActivityEvent, ProximityEvent
from config import Config
from pymongo.asynchronous.database import AsyncDatabase


class GameLogic:
    def __init__(self, config: Config, packet_processor: PacketProcessor, db: AsyncDatabase):
        self.config = config
        self.packet_processor = packet_processor
        self.stations = db["stations"]
        self.users = db["users"]
        self.events = db["events"]


    # ===== APIs for PacketProcessor =====
    async def on_activity_event(evt: ActivityEvent):
        pass


    async def on_proximity_event(evt: ProximityEvent):
        pass
