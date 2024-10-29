from Scoring import Scoring
import random as r

class Game:

    def __init__(self):
        self.bowl_1 = 0
        self.bowl_2 = 0
        self.bowl_3 = 0
        self.pins = 10
        self.frame_turns = 1
        self.bowling_dict = {"Frame 1": [], "Frame 2": [], "Frame 3": [], "Frame 4": [], "Frame 5": [], "Frame 6": [],
                             "Frame 7": [], "Frame 8": [], "Frame 9": [], "Frame 10": []}
        self.score = Scoring()
        self.count_s = 0
        self.count_sp = 0


    def new_frame(self):
        self.frame_turns += 1
        print(f"Starting frame {self.frame_turns} now.")
        self.start_frame()


    def reset_pins(self):
        self.pins = 10
        print("\nPins have been reset.")


    def turn_1(self):
        print("\n\tBowl 1")
        self.bowl_1 = r.randint(0, self.pins)
        self.pins = self.pins - self. bowl_1

        print(f"\t\tYou knocked over {self.bowl_1} pins.")

        self.score.scoring_frame_bowl1(self.bowling_dict, self.bowl_1, self.frame_turns)
        print(f"\t{self.bowling_dict}")


    def turn_2(self):
        print("\n\tBowl 2")
        self.bowl_2 = r.randint(0, self.pins)
        self.pins = self.pins - self.bowl_2

        print(f"\t\tYou knocked over {self.bowl_2} pins.")

        self.score.scoring_frame_bowl2(self.bowling_dict, self.frame_turns, self.bowl_1, self.bowl_2, self.pins)
        print(f"\t{self.bowling_dict}")


    def start_game(self):
        print("Starting a new game.")
        self.start_frame()


    def start_frame(self):
        print(f"\nFrame {self.frame_turns}")
        if self.frame_turns == 10:
            self.frame_10()

        else:
            self.turn_1()
            self.turn_2()
            self.score.totals(self.bowling_dict, self.frame_turns)
            print(f"\n\tTotal: {self.score.total}")
            self.reset_pins()
            self.new_frame()


    def frame_10(self):
        self.turn_1_10()
        if self.score.check_strike(self.bowl_1):
            self.count_s += 1
            self.reset_pins()
            self.turn_2_10()
            if self.score.check_strike(self.bowl_2):
                self.count_s += 1
                self.reset_pins()
                self.turn_3_10()
            elif self.score.check_spare(self.pins):
                self.count_sp += 1
                self.reset_pins()
                self.turn_3_10()
            else:
                self.turn_3_10()
        else:
            self.turn_2_10()
            if self.score.check_spare(self.pins):
                self.count_sp += 1
                self.reset_pins()
                self.turn_3_10()

        self.score.totals_10(self.bowling_dict, self.frame_turns)
        print(f"\n\tTotal: {self.score.total}")


    def turn_1_10(self):
        print("\n\tBowl 1")
        self.bowl_1 = r.randint(0, self.pins)
        self.pins = self.pins - self.bowl_1

        print(f"\t\tYou knocked over {self.bowl_1} pins.")

        self.score.scoring_frame_bowl1_10(self.bowling_dict, self.bowl_1, self.frame_turns)
        print(f"\t{self.bowling_dict}")


    def turn_2_10(self):
        print("\n\tBowl 2")
        self.bowl_2 = r.randint(0, self.pins)
        self.pins = self.pins - self.bowl_2

        print(f"\t\tYou knocked over {self.bowl_2} pins.")

        self.score.scoring_frame_bowl2_10(self.bowling_dict, self.frame_turns, self.bowl_1, self.bowl_2, self.pins, self.count_s)
        print(f"\t{self.bowling_dict}")


    def turn_3_10(self):
        print("\n\tBowl 3")
        self.bowl_3 = r.randint(0, self.pins)
        self.pins = self.pins - self.bowl_3

        print(f"\t\tYou knocked over {self.bowl_3} pins.")

        self.score.scoring_frame_bowl3_10(self.bowling_dict, self.frame_turns, self.bowl_1, self.bowl_2, self.bowl_3,
                                          self.count_s, self.count_sp, self.pins)
        print(f"\t{self.bowling_dict}")



a = Game()

a.start_game()