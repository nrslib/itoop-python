from janken import JankenGame, JapaneseDisplay


def main():
    game = JankenGame()
    game.play(0, 2, JapaneseDisplay(), "default")
    game.play(1, 2, JapaneseDisplay(), "default")
    game.play(2, 2, JapaneseDisplay(), "default")


if __name__ == '__main__':
    main()
