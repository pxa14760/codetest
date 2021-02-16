class Rewards_Strategy:
    def __init__(self, category, reward):
        self.category = category
        self.reward = reward

    def madeupStrategy(self):
        if self.category in {"drink", "sandwich", "retail"} and self.reward in {"blue", "green", "yellow"}:
            if self.category == "drink":
                if self.reward == "blue":
                    reward_pts = 1
                if self.reward == "green":
                    reward_pts = 2
                if self.reward == "yellow":
                    reward_pts = 3
            if self.category == "sandwich":
                if self.reward == "blue":
                    reward_pts = 2
                if self.reward == "green":
                    reward_pts = 3
                if self.reward == "yellow":
                    reward_pts = 4
            if self.category == "retail":
                if self.reward == "blue":
                    reward_pts = 3
                if self.reward == "green":
                    reward_pts = 4
                if self.reward == "yellow":
                    reward_pts = 5
        else:
            reward_pts = 0
        return reward_pts

