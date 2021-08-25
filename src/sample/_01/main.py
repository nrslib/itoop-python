def main():
    play(1, 2)


def play(left_hand: int, right_hand: int):
    result = judge(left_hand, right_hand)
    show_result(result)


def judge(left_hand: int, right_hand: int) -> int:
    if left_hand == 0:  # Goo
        if right_hand == 0:  # Goo
            return 2
        elif right_hand == 1:  # Choki
            return 1
        else:  # Par
            return 3
    elif left_hand == 1:  # Choki
        if right_hand == 0:  # Goo
            return 3
        elif right_hand == 1:  # Choki
            return 2
        else:  # Par
            return 1
    else:  # Par
        if right_hand == 0:  # Goo
            return 1
        elif right_hand == 1:  # Choki
            return 3
        else:  # Par
            return 2


def show_result(result: int):
    if result == 1:
        print("勝ち")
    elif result == 2:
        print("引き分け")
    else:
        print("負け")


if __name__ == '__main__':
    main()
