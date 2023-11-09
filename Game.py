import random

class Player:
    def __init__(self, name):
        self.list = []
        self.name = name

    def verif(self):
        suma = 0
        if len(self.list) == 3:
            for el in self.list:
                if 1 > el or el > 9:
                    return False
                suma = suma + el
        if suma == 15:
            return True
        else:
            return False


class Game:
    def __init__(self):
        self.playerA = Player('A')
        self.playerB = Player('B')
        self.playerList = [self.playerA, self.playerB]
        self.lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def find_tuples(self, target_sum):
        result = []
        #max_value = target_sum
        for i in range(1, target_sum + 1):
            j = target_sum - i
            if 0 < j <= 9 and i <= j:
                result.append((i, j))
        return result

    def heuristic(self, player):
        suma = 0
        rez = 0
        if len(player.list) == 0:
            rez = random.choice(self.lst)
            self.lst.remove(rez)
            return rez
        elif len(player.list) == 1:
            temp = player.list[0]
            suma = 15 - temp
            tuples = self.find_tuples(suma)
            for el in tuples:
                if el[0] in self.lst:
                    rez = el[0]
                    self.lst.remove(rez)
                    return rez
        elif len(player.list) == 2:
            for el in player.list:
                suma = suma + el
            rez = 15 - suma
            if (rez not in self.lst):
                rez = random.choice(self.lst)
        return rez

    def validation(self, num):
        if (0 < num < 10):
            return True
        else:
            return False

    def transition(self, player):
        chosen = self.heuristic(player)
        if self.validation(chosen):
            player.list.append(chosen)
        else:
            return 0

    def game(self):
        while (len(self.playerA.list) < 3 and len(self.playerA.list) < 3):
            self.transition(self.playerA)
            self.transition(self.playerB)
        if self.playerA.verif():
            print("Castigatorul este A: " + str(self.playerA.list))
        elif self.playerB.verif():
            print("Castigatorul este B: " + str(self.playerB.list))
        else:
            print("Tie")


game = Game()
game.game()

