class Scoring:

    def __init__(self):
        self.total = 0

    def scoring_frame_bowl1(self, bowling_dict, bowl_1, frame_turns):

        if self.check_strike(bowl_1):
            print("\t\tStrike")
            bowling_dict[f"Frame {frame_turns}"] = ["", "X"]

        else:
            bowling_dict[f"Frame {frame_turns}"] = [bowl_1, ""]



    def scoring_frame_bowl2(self, bowling_dict, frame_turns, bowl_1, bowl_2, pins):
        if self.check_strike(bowl_1):
            pass

        else:
            if self.check_spare(pins):
                print("\t\tSpare")
                bowling_dict[f"Frame {frame_turns}"] = [bowl_1, "/"]

            else:
                bowling_dict[f"Frame {frame_turns}"] = [bowl_1, bowl_2]


    def scoring_frame_bowl1_10(self, bowling_dict, bowl_1, frame_turns):

        if self.check_strike(bowl_1):
            print("\t\tStrike")
            bowling_dict[f"Frame {frame_turns}"] = ["X", "", ""]

        else:
            bowling_dict[f"Frame {frame_turns}"] = [bowl_1, ""]



    def scoring_frame_bowl2_10(self, bowling_dict, frame_turns, bowl_1, bowl_2, pins, count_s):
        if count_s == 1:
            if self.check_strike(bowl_2):
                print("\t\tStrike")
                bowling_dict[f"Frame {frame_turns}"] = ["X", "X", ""]

            else:
                bowling_dict[f"Frame {frame_turns}"] = ["X", bowl_2, ""]

        else:
            if self.check_spare(pins):
                print("\t\tSpare")
                bowling_dict[f"Frame {frame_turns}"] = [bowl_1, "/", ""]

            else:
                bowling_dict[f"Frame {frame_turns}"] = [bowl_1, bowl_2]


    def scoring_frame_bowl3_10(self, bowling_dict, frame_turns, bowl_1, bowl_2, bowl_3, count_s, count_sp, pins):
        if count_s == 2:
            if self.check_strike(bowl_3):
                print("\t\tStrike")
                bowling_dict[f"Frame {frame_turns}"] = ["X", "X", "X"]

            else:
                bowling_dict[f"Frame {frame_turns}"] = ["X", "X", bowl_3]

        elif count_s == 1:
            if self.check_strike(bowl_3):
                print("\t\tStrike")
                bowling_dict[f"Frame {frame_turns}"] = ["X", bowl_2, "X"]

            else:
                if self.check_spare(pins):
                    bowling_dict[f"Frame {frame_turns}"] = ["X", bowl_2, "/"]

                else:
                    bowling_dict[f"Frame {frame_turns}"] = ["X", bowl_2, bowl_3]

        elif count_sp == 1:
            if self.check_strike(bowl_3):
                print("\t\tStrike")
                bowling_dict[f"Frame {frame_turns}"] = [bowl_1, "/", "X"]

            else:
                bowling_dict[f"Frame {frame_turns}"] = [bowl_1, "/", bowl_3]

        else:
            if self.check_spare(pins):
                print("\t\tSpare")
                bowling_dict[f"Frame {frame_turns}"] = [bowl_1, bowl_2, "/"]

            else:
                bowling_dict[f"Frame {frame_turns}"] = [bowl_1, bowl_2, bowl_3]


    def check_strike(self, bowl_1):
        if bowl_1 == 10:
            return True
        else:
            return False


    def check_spare(self, pins):
        if pins == 0:
            return True
        else:
            return False


    def totals(self, bowling_dict, frame_turns):
        if bowling_dict[f"Frame {frame_turns}"][1] == "X":
            self.total += 10
        else:
            if bowling_dict[f"Frame {frame_turns}"][1] == "/":
                self.total += 10
            else:
                self.total += (bowling_dict[f"Frame {frame_turns}"][0] + bowling_dict[f"Frame {frame_turns}"][1])

        if frame_turns != 1:
            if bowling_dict[f"Frame {frame_turns-1}"][1] == "X":
                if bowling_dict[f"Frame {frame_turns}"][1] == "X":
                    self.total += 20
                else:
                    if bowling_dict[f"Frame {frame_turns}"][1] == "/":
                        self.total += 10
                    else:
                        self.total += (
                                    bowling_dict[f"Frame {frame_turns}"][0] + bowling_dict[f"Frame {frame_turns}"][1]
                                      )

            if bowling_dict[f"Frame {frame_turns-1}"][1] == "/":
                if bowling_dict[f"Frame {frame_turns}"][1] == "X":
                    self.total += 10

                else:
                    self.total += bowling_dict[f"Frame {frame_turns}"][0]


    def totals_10(self, bowling_dict, frame_turns):
        if bowling_dict[f"Frame {frame_turns - 1}"][1] == "X":

            if bowling_dict[f"Frame {frame_turns}"][0] == "X":
                self.total += 10

                if bowling_dict[f"Frame {frame_turns}"][1] == "X":
                    self.total += 10

                else:
                    self.total += bowling_dict[f"Frame {frame_turns}"][1]

            else:
                if bowling_dict[f"Frame {frame_turns}"][1] == "/":
                    self.total += 10

                else:
                    self.total += (
                            bowling_dict[f"Frame {frame_turns}"][0] + bowling_dict[f"Frame {frame_turns}"][1]
                    )

        if bowling_dict[f"Frame {frame_turns - 1}"][1] == "/":
            if bowling_dict[f"Frame {frame_turns}"][0] == "X":
                self.total += 10

            else:
                self.total += bowling_dict[f"Frame {frame_turns}"][0]

        if bowling_dict[f"Frame {frame_turns}"][0] == "X":
            self.total += 10

            if bowling_dict[f"Frame {frame_turns}"][1] == "X":
                self.total += 10

                if bowling_dict[f"Frame {frame_turns}"][2] == "X":
                    self.total += 10

                else:
                    self.total += bowling_dict[f"Frame {frame_turns}"][2]

            else:
                if bowling_dict[f"Frame {frame_turns}"][2] == "/":
                    self.total += 10

                else:
                    print(bowling_dict[f"Frame {frame_turns}"][1])
                    self.total += bowling_dict[f"Frame {frame_turns}"][1]

                    if bowling_dict[f"Frame {frame_turns}"][2] == "X":
                        self.total += 10

                    else:
                        self.total += bowling_dict[f"Frame {frame_turns}"][2]

        else:
            if bowling_dict[f"Frame {frame_turns}"][1] == "/":
                self.total += 10

                if bowling_dict[f"Frame {frame_turns}"][2] == "X":
                    self.total += 10

                else:
                    self.total += bowling_dict[f"Frame {frame_turns}"][2]

            else:
                self.total += (bowling_dict[f"Frame {frame_turns}"][0] + bowling_dict[f"Frame {frame_turns}"][1])
