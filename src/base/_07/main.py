from janken import JankenGame, JapaneseDisplay, NormalRule


def main():
    display = JapaneseDisplay()
    rule = NormalRule()
    game = JankenGame()
    game.play(0, 2, display, rule)
    game.play(1, 2, display, rule)
    game.play(2, 2, display, rule)


if __name__ == '__main__':
    main()
