# import numpy as np

from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState

"""
    Functions will move here after it is stable.
    For temporary use, please code in RandomBot.py
"""


class TucilBot(Bot):
    def get_action(self, state: GameState) -> GameAction:
        raise NotImplementedError()
