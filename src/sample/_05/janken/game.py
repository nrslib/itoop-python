class JankenGame:
    def play(self, left_hand: int, right_hand: int, lang: str, rule_name: str):
        """
        :param lang: ja:日本語,en:英語
        :param rule_name: default:通常, reverse:逆
        """
        rule = self.get_rule(rule_name)
        result = rule.judge(left_hand, right_hand)
        display = self.get_display(lang)
        display.show(result)

    def get_rule(self, rule_name: str):
        if rule_name == "default":
            return NormalRule()
        else:
            return ReverseRule()

    def get_display(self, lang: str):
        if lang == "ja":
            return JapaneseDisplay()
        else:
            return EnglishDisplay()


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
