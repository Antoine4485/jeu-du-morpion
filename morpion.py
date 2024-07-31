from random import randrange
from os import system, name


class Morpion:

    def __init__(self):
        self._players = ["X", "O"]
        self._grid = []
        while True:
            if not self._play():
                return

    def _play(self) -> bool:
        ind = randrange(2)
        self._grid = ["" for _ in range(9)]

        while True:
            self._clear_screen()
            self._show_grid()

            if self._game_won():
                print(f"Jeu terminé. Le joueur {self._players[ind]} a gagné.")
                break
            if self._grid_full():
                print("Jeu terminé. Aucun gagnant.")
                break

            # changement de joueur
            ind = 1 if ind == 0 else 0

            n = input(f"Tour du joueur {self._players[ind]}. Entrez un nombre entre 1 et 9 : ")
            if n.lower() == "q":
                return False
            try:
                n = int(n)
                if n < 1 or n > 9:
                    continue
                if self._grid[n - 1] != "":
                    print("Cette case est déjà remplie.")
                    continue
                self._grid[n - 1] = self._players[ind]
            except ValueError:
                continue

        return True if input("\nNouvelle partie (o/n) ? ").lower() == "o" else False

    def _show_grid(self):
        draw = ""
        for i in range(9):
            draw += f"{self._grid[i]:^3}"
            draw += "|" if (i + 1) % 3 != 0 else "\n"
        print(draw)

    def _game_won(self) -> bool:
        if (self._grid[0] != "" and self._grid[0] == self._grid[1] == self._grid[2] or
                self._grid[3] != "" and self._grid[3] == self._grid[4] == self._grid[5] or
                self._grid[6] != "" and self._grid[6] == self._grid[7] == self._grid[8] or
                self._grid[0] != "" and self._grid[0] == self._grid[3] == self._grid[6] or
                self._grid[1] != "" and self._grid[1] == self._grid[4] == self._grid[7] or
                self._grid[2] != "" and self._grid[2] == self._grid[5] == self._grid[8] or
                self._grid[0] != "" and self._grid[0] == self._grid[4] == self._grid[8] or
                self._grid[2] != "" and self._grid[2] == self._grid[4] == self._grid[6]):
            return True
        return False

    def _grid_full(self) -> bool:
        return False if "" in self._grid else True

    @staticmethod
    def _clear_screen():
        system('cls') if name == 'nt' else system('clear')


if __name__ == '__main__':
    Morpion()