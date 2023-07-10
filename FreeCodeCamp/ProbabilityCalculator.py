import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            balls_drawn = self.contents
            self.contents = []
        else:
            balls_drawn = random.sample(self.contents, num_balls)
            for ball in balls_drawn:
                self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_dict = {}

        for ball in balls_drawn:
            balls_dict[ball] = balls_dict.get(ball, 0) + 1

        match = True
        for color, count in expected_balls.items():
            if color not in balls_dict or balls_dict[color] < count:
                match = False
                break

        if match:
            expected_count += 1

    probability = expected_count / num_experiments
    return probability