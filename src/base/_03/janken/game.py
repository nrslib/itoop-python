class JankenGame:
    def play(self, left_hand: int, right_hand: int, lang: str):
        """
        :param lang: ja:日本語,en:英語
        """
        result = self.judge(left_hand, right_hand)
        self.show_result(result, lang)

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

    def show_result(self, result: int, lang: str):
        # ja: 日本語、en: 英語で結果を表示しよう
        if result == 1:
            print("勝ち")
        elif result == 0:
            print("引き分け")
        else:
            print("負け")
