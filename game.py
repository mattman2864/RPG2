# https://github.com/mattman2864
# everything by Matt Stein
print("Byte To Survive 2")
print("By mattman2864 on GitHub")


import colored
import json
from tabulate import tabulate

def jsonToDict(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

class Item:
    def __init__(self, id: str):
        self.id = id
    def __str__(self) -> str:
        return self.id

class StackableItem(Item):
    def __init__(self, id: str, count: int):
        super().__init__(id)
        self.count = count
    def __str__(self) -> str:
        return f"{self.count} " + self.id

class Inventory:
    def __init__(self):
        self.inventory = []
    def addToInventory(self, addItem: Item):
        for item in self.inventory:
            if item.id == addItem.id and type(addItem) == StackableItem:
                item.count += addItem.count
                return None
        self.inventory.append(addItem)
    def __str__(self) -> str:
        returnString = ""
        for i in self.inventory:
            returnString += str(i) + " "
        return returnString

class Player:
    def __init__(self, inventory: Inventory):
        self.inv = inventory

class CommandHandler:
    def __init__(self):
        self.commands = jsonToDict("commands.json")

class Game:
    def __init__(self, player: Player, commander: CommandHandler):
        self.isRunning = True
        self.player = player
        self.commands = commander.commands.copy()
    def takeCommand(self, args):
        if not args:
            return
        cmd = args[0]
        if not args[0] in self.commands:
            print(f"Invalid command \"{cmd}\". Type \"help\" for a list of commands.")
            return
        if len(args) < self.commands[cmd]["numOfArgs"][0]:
            if len(args) > self.commands[cmd]["numOfArgs"][-1]:
                print(f"Invalid number of arguments. \"{cmd}\" requires at least {self.commands[cmd]['numOfArgs'][0]} arguments.")
                return
            else:
                print(f"Invalid number of arguments. \"{cmd}\" requires no more than {self.commands[cmd]['numOfArgs'][-1]} arguments.")
                return
        if cmd == "help":
            self.help()
    def help(self):
        commandTable  = []
        print()
        for i in self.commands:
            if self.commands[i]["enabled"]:
                commandTable.append([i, self.commands[i]["description"]])
        print(tabulate(commandTable, headers=["Command", "Description"])+"\n")

player = Player(Inventory())
game = Game(player, CommandHandler())
while game.isRunning:
    cmd = input(colored.yellow(">>> ")).split()
    game.takeCommand(cmd)