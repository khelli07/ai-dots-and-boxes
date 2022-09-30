# import numpy as np

from Bot import Bot
from GameAction import GameAction
from GameState import GameState


class TucilBot(Bot):
    def get_action(self, state: GameState) -> GameAction:
        raise NotImplementedError()