# THIS PROGRAM TITLED "BATTLE OF ROBOTS"
# IS A GAME THAT USES OOP IN PYTHON
# AS PART OF URO APPLICATION TEST, MODULE 2

from random import choice

# CREATE CLASSES

class Robot:

    def __init__(self, name=str, element=str, hit_points=int, attacks=list) -> None:
        self.name = name
        self.element = element
        self.attacks = attacks
        self.hit_points = hit_points

    def update_hitpoints(self, damage=int):
        if self.hit_points >= damage:
            self.hit_points = self.hit_points -1*damage
        else:
            self.hit_points = 0

    def is_dead(self):
        return True if self.hit_points <= 0 else False
    
    def player_attack(self, me=object, opponent=object):
        self.show_attacks()
        chosen_attack = int(input("Which attack would you like to use? Choose number: "))
        while True:
            match chosen_attack:
                case 1:
                    print(f"{me.name} uses {me.attacks[0][0]} to {opponent.name}!")
                    opponent.update_hitpoints(me.attacks[0][2])
                    me.update_hitpoints(me.attacks[0][3])
                    print(f"{me.name} remaining hit points: {me.hit_points}.")
                    print(f"{opponent.name} remaining hit points: {opponent.hit_points}.")
                    break
                case 2:
                    print(f"{me.name} uses {me.attacks[1][0]} to {opponent.name}!")
                    opponent.update_hitpoints(me.attacks[1][2])
                    me.update_hitpoints(me.attacks[1][3])
                    print(f"{me.name} remaining hit points: {me.hit_points}.")
                    print(f"{opponent.name} remaining hit points: {opponent.hit_points}.")
                    break
                case 3:
                    print(f"{me.name} uses {me.attacks[2][0]} to {opponent.name}!")
                    opponent.update_hitpoints(me.attacks[2][2])
                    me.update_hitpoints(me.attacks[2][3])
                    print(f"{me.name} remaining hit points: {me.hit_points}.")
                    print(f"{opponent.name} remaining hit points: {opponent.hit_points}.")
                    break
                case _:
                    chosen_attack = int(input("Please choose a number from 1 to 3: "))

    def non_player_attack(self, me=object, opponent=object):
        chosen_attack = choice([0, 1, 2])
        opponent.update_hitpoints(me.attacks[chosen_attack][2])
        me.update_hitpoints(me.attacks[chosen_attack][3])
        print(f"{me.name} uses {me.attacks[chosen_attack][0]} to {opponent.name}!")
        print(f"{opponent.name} remaining hit points: {opponent.hit_points}.")
        print(f"{me.name} remaining hit points: {me.hit_points}.")

    def show_attacks(self):
        for index, i in enumerate(self.attacks, start=1):
            print(f"{index}. {i[0]}: {i[1]} type, {i[2]} hit points to opponent, {i[3]} hit points to self.")


class Battle:

    def __init__(self, number=int, pokebot_one=object, pokebot_two=object) -> None:
        self.miss_probability = 0.2
        self.number = number
        self.player = [pokebot_one, pokebot_two]
        self.start_battle()

    def start_battle(self) -> None:
        print("Let's begin the battle!")
        print(f"Battle {self.number}: {self.player[0].name} vs {self.player[1].name}")
        self.exchange_attacks()

    def exchange_attacks(self) -> None:
        i = choice([0, 1]) # moves first
        j = (i+1)%2 # moves second
        while (self.player[i].hit_points > 0 and self.player[j].hit_points > 0):
            if i == 0:
                self.player[i].player_attack(self.player[i], self.player[j])
                if self.player[i].is_dead() or self.player[j].is_dead(): break
                self.player[j].non_player_attack(self.player[j], self.player[i])
                if self.player[i].is_dead() or self.player[j].is_dead(): break
            else:
                self.player[i].non_player_attack(self.player[i], self.player[j])
                if self.player[i].is_dead() or self.player[j].is_dead(): break
                self.player[j].player_attack(self.player[j], self.player[i])
                if self.player[i].is_dead() or self.player[j].is_dead(): break
        if self.player[0].hit_points == 0:
            print(f"{self.player[0].name} fainted.")
            print("Try not losing next time!")
        else: 
            print(f"{self.player[1].name} fainted.")
            print(f"Congratulations for the win!")

    # def show_attacks(self) -> None:


    # def end_battle(self) -> None:



class Game:

    def __init__(self) -> None:
        self.start_game()

    def choose_pokebot(self) -> None:
        chosen_pokebot = int(input("So, which PokeBot is going to be your partner? Choose number: "))
        while True:
            match chosen_pokebot:
                case 1:
                    self.pokebot_1 = pokebot[0][0]
                    pokebot[0][1] = False
                    break
                case 2:
                    self.pokebot_1 = pokebot[1][0]
                    pokebot[1][1] = False
                    break
                case 3:
                    self.pokebot_1 = pokebot[2][0]
                    pokebot[2][1] = False
                    break
                case _:
                    chosen_pokebot = int(input("Please choose a number from 1 to 3: "))
        print(f"Excellent choice! {self.pokebot_1.name} is now your partner.")

    def intro(self) -> None:
        print("This is a solo player game where you start by choosing your PokeBot.")
        print("Here are the PokeBots you can choose from:")
        for j, i in enumerate(pokebot, start=1):
            print(f"{j}. {i[0].name}, the {i[0].element} type PokeBot.")
        self.choose_pokebot()
    
    def start_game(self) -> None:
        print("Welcome to Battle of PokeBots!")
        self.intro()
        print("You are now going to battle other PokeBots.")
        possible_opponent = []
        for j, i in enumerate(pokebot, start=0):
            if i[1] == False:
                me = j
            else:
                possible_opponent.append(j)
        opp = choice(possible_opponent)
        battle = Battle(1, pokebot[me][0], pokebot[opp][0])


# CREATE POKEBOT OBJECTS

bulbabot = Robot(
    "Bulbabot", "Grass", 50,[
        ["Floral Healing", "Healing", 0, -15],
        ["Cut", "Normal", 20, 0],
        ["Leaf Blade", "Grass", 15, 0]
    ]
    )

squirbot = Robot(
    "Squirbot", "Water", 50,[
        ["Absorb", "Healing", 10, -10],
        ["Tackle", "Normal", 20, 0],
        ["Aqua Tail", "Water", 15, 0]
    ]
    )

charmenbot = Robot(
    "Charmenbot", "Fire", 50,[
        ["Heal Pulse", "Healing", -5, -20],
        ["Quick Attack", "Normal", 20, 0],
        ["Fire Spin", "Fire", 25, 5]
    ]
    )

pokebot = [[bulbabot, True], [squirbot, True], [charmenbot, True]]
game = Game()