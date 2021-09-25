class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')

player1 = PlayerCharacter("ramesh")

print(player1.name)