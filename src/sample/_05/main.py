from janken import JankenGame


def main():
    game = JankenGame()
    game.play(1, 2, "ja", "default")
    game.play(1, 2, "en", "reverse")


if __name__ == '__main__':
    main()
