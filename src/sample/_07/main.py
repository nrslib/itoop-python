from janken import JankenGame, JapaneseDisplay, NormalRule


def main():
    display = JapaneseDisplay()
    rule = NormalRule()
    game = JankenGame(display, rule)
    game.play(0, 2)
    game.play(1, 2)
    game.play(2, 2)


if __name__ == '__main__':
    main()
