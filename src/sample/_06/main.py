class JankenGame:
    def play(self, left_hand: int, right_hand: int, display, rule):
        result = rule.judge(left_hand, right_hand)
        display.show(result)


class JapaneseDisplay:
    def show(self, result: int):
        if result == 1:
            print("勝ち")
        elif result == 0:
            print("引き分け")
        else:
            print("負け")


class EnglishDisplay:
    def show(self, result: int):
        if result == 1:
            print("win")
        elif result == 0:
            print("draw")
        else:
            print("lose")


class NormalRule:
    def judge(self, left_hand: int, right_hand: int) -> int:
        if left_hand == 0:  # Goo
            if right_hand == 0:  # Goo
                return 0
            elif right_hand == 1:  # Choki
                return 1
            else:  # Par
                return -1
        elif left_hand == 1:  # Choki
            if right_hand == 0:  # Goo
                return -1
            elif right_hand == 1:  # Choki
                return 0
            else:  # Par
                return 1
        else:  # Par
            if right_hand == 0:  # Goo
                return 1
            elif right_hand == 1:  # Choki
                return -1
            else:  # Par
                return 0


class ReverseRule:
    def judge(self, left_hand: int, right_hand: int) -> int:
        if left_hand == 0:  # Goo
            if right_hand == 0:  # Goo
                return 0
            elif right_hand == 1:  # Choki
                return -1
            else:  # Par
                return 1
        elif left_hand == 1:  # Choki
            if right_hand == 0:  # Goo
                return 1
            elif right_hand == 1:  # Choki
                return 0
            else:  # Par
                return -1
        else:  # Par
            if right_hand == 0:  # Goo
                return -1
            elif right_hand == 1:  # Choki
                return 1
            else:  # Par
                return 0


def main():
    display = JapaneseDisplay()
    rule = NormalRule()
    game = JankenGame()
    game.play(0, 2, display, rule)
    game.play(1, 2, display, rule)
    game.play(2, 2, display, rule)


if __name__ == '__main__':
    main()
