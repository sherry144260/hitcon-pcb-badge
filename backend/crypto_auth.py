from typing import Optional
from schemas import IrPacket
from database import db
from ecc_utils import ecc_sign, ecc_verify


class UnsignedPacketError(Exception):
    pass


# This module is responsible for verifying & signing the packets
class CryptoAuth:
    # ===== Generic methods for any other layers =====
    @staticmethod
    async def get_pubkey_by_username(username: int) -> Optional[int]:
        pass


    # ===== APIs for PacketProcessor =====
    @staticmethod
    async def verify_packet(ir_packet: IrPacket) -> Optional[int]:
        """
        Verify the packet. Throws an exception if the packet is invalid.
        Returns username if the packet is valid.
        """
        # TODO: handle case for ActivityPacket, in which the signature must be validate against two usernames   
        pass
