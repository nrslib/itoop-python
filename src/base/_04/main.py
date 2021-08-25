from janken import JankenGame


def main():
    game = JankenGame()
    game.play(1, 2, "ja")
    game.play(1, 2, "en")


if __name__ == '__main__':
    main()
