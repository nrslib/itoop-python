def main():
    play(1, 2)


def play(left_hand: int, right_hand: int):
    result = judge(left_hand, right_hand)
    show_result(result)


def judge(left_hand: int, right_hand: int) -> int:
    # 勝敗を判定して結果（1:勝ち, 2:引き分け, 3:負け）を返却しよう
    return 0


def show_result(result: int):
    # 結果をもとに勝敗を print を使って表示しよう
    print("結果を表示")


if __name__ == '__main__':
    main()
