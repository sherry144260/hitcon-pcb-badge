from packet_processor import PacketProcessor
from schemas import ProximityEvent, PubAnnounceEvent, TwoBadgeActivityEvent, GameActivityEvent, SingleBadgeActivityEvent, SponsorActivityEvent

class GameLogic:
    # ===== APIs for PacketProcessor =====
    @PacketProcessor.event_handler
    @staticmethod
    async def on_single_badge_activity_event(evt: SingleBadgeActivityEvent):
        pass


    @PacketProcessor.event_handler
    @staticmethod
    async def on_two_badge_activity_event(evt: TwoBadgeActivityEvent):
        pass


    @PacketProcessor.event_handler
    @staticmethod
    async def on_game_activity_event(evt: GameActivityEvent):
        pass


    @PacketProcessor.event_handler
    @staticmethod
    async def on_sponsor_activity_event(evt: SponsorActivityEvent):
        pass


    @PacketProcessor.event_handler
    @staticmethod
    async def on_proximity_event(evt: ProximityEvent):
        pass


    @PacketProcessor.event_handler
    @staticmethod
    async def on_pub_announce_event(evt: PubAnnounceEvent):
        pass
