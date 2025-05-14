import random

class Nim():
    def __init__(self, initial=[4, 4, 4, 4]):
        self.piles = initial.copy()
        self.player = 0
        self.winner = None

    @classmethod
    def available_actions(cls, piles):
        actions = set()
        for i, pile in enumerate(piles):
            for j in range(1, pile + 1):
                actions.add((i, j))
        return actions

    @classmethod
    def other_player(cls, player):
        return 0 if player == 1 else 1

    def switch_player(self):
        self.player = Nim.other_player(self.player)

    def move(self, action):
        pile, count = action
        self.piles[pile] -= count
        self.switch_player()
        if all(pile == 0 for pile in self.piles):
            self.winner = self.player


class NimAI():
    def __init__(self, alpha=0.5, epsilon=0.1):
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def get_q_value(self, state, action):
        return self.q.get((tuple(state), action), 0)

    def update_q_value(self, state, action, old_q, reward, future_q):
        new_q = old_q + self.alpha * (reward + future_q - old_q)
        self.q[(tuple(state), action)] = new_q

    def best_future_reward(self, state):
        best_q = 0
        for action in Nim.available_actions(state):
            q = self.get_q_value(state, action)
            if q > best_q:
                best_q = q
        return best_q

    def choose_action(self, state, epsilon=True):
        actions = list(Nim.available_actions(state))
        if not actions:
            return None

        if epsilon and random.random() < self.epsilon:
            return random.choice(actions)
        else:
            best_q = float('-inf')
            best_actions = []
            for action in actions:
                q = self.get_q_value(state, action)
                if q > best_q:
                    best_q = q
                    best_actions = [action]
                elif q == best_q:
                    best_actions.append(action)
            return random.choice(best_actions) if best_actions else random.choice(actions)

    def update(self, old_state, action, new_state, reward):
        old_q = self.get_q_value(old_state, action)
        best_future_q = self.best_future_reward(new_state)
        self.update_q_value(old_state, action, old_q, reward, best_future_q)

def train(n):
    player = NimAI()
    for _ in range(n):
        game = Nim()
        last_move = {0: {"state": None, "action": None}, 1: {"state": None, "action": None}}
        while True:
            state = game.piles.copy()
            action = player.choose_action(state)
            last_move[game.player]["state"] = state
            last_move[game.player]["action"] = action
            game.move(action)
            new_state = game.piles.copy()
            if game.winner is not None:
                player.update(state, action, new_state, -1)
                player.update(last_move[game.player]["state"], last_move[game.player]["action"], new_state, 1)
                break
            elif last_move[game.player]["state"] is not None:
                player.update(last_move[game.player]["state"], last_move[game.player]["action"], new_state, 0)
    return player
