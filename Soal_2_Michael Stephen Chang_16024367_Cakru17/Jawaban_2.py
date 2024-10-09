# THIS PROGRAM TITLED "BATTLE OF ROBOTS"
# IS A GAME THAT USES OOP IN PYTHON
# AS PART OF URO APPLICATION TEST, MODULE 2

from random import choice
import random

# CREATE CLASSES

text_divider = "=========================================================================="

class Robot:

    def __init__(self, name=str, element=str, hit_points=int, attacks=list) -> None:
        self.name = name
        self.element = element
        self.attacks = attacks
        self.hit_points = hit_points
        self.miss_probability = 0.2

    def update_hitpoints(self, damage=int):
        if self.hit_points >= damage:
            self.hit_points = self.hit_points -1*damage
        else:
            self.hit_points = 0

    def is_dead(self):
        return True if self.hit_points <= 0 else False
    
    def player_attack(self, me=object, opponent=object):
        print(f"It's {me.name}'s turn to attack.")
        self.show_attacks()
        chosen_attack = int(input("Which attack would you like to use? Choose number: "))
        while True:
            match chosen_attack:
                case 1:
                    print(text_divider)
                    print(f"{me.name} uses {me.attacks[0][0]} to {opponent.name}!")
                    if random.random() < (1.0-self.miss_probability):
                        damage = me.check_effectiveness(me.attacks[0][1], opponent.element, me.attacks[0][2])
                        if damage > me.attacks[0][2]: print("It's super effective!")
                        elif damage < me.attacks[0][2]: print("It's not super effective...")
                        opponent.update_hitpoints(damage)
                        me.update_hitpoints(me.attacks[0][3])
                    else:
                        print("Oh no! It misses.")
                    break
                case 2:
                    print(text_divider)
                    print(f"{me.name} uses {me.attacks[1][0]} to {opponent.name}!")
                    if random.random() < (1.0-self.miss_probability):
                        damage = me.check_effectiveness(me.attacks[1][1], opponent.element, me.attacks[1][2])
                        if damage > me.attacks[1][2]: print("It's super effective!")
                        elif damage < me.attacks[1][2]: print("It's not super effective...")
                        opponent.update_hitpoints(damage)
                        me.update_hitpoints(me.attacks[1][3])
                    else:
                        print("Oh no! It misses.")
                    break
                case 3:
                    print(text_divider)
                    print(f"{me.name} uses {me.attacks[2][0]} to {opponent.name}!")
                    if random.random() < (1.0-self.miss_probability):
                        damage = me.check_effectiveness(me.attacks[2][1], opponent.element, me.attacks[2][2])
                        if damage > me.attacks[2][2]: print("It's super effective!")
                        elif damage < me.attacks[2][2]: print("It's not super effective...")
                        opponent.update_hitpoints(damage)
                        me.update_hitpoints(me.attacks[2][3])
                    else:
                        print("Oh no! It misses.")
                    break
                case _:
                    chosen_attack = int(input("Please choose a number from 1 to 3: "))
        print(f"> {me.name} remaining hit points: {me.hit_points}.")
        print(f"> {opponent.name} remaining hit points: {opponent.hit_points}.")
        print(text_divider)

    def non_player_attack(self, me=object, opponent=object):
        print(f"It's {me.name}'s turn to attack.")
        chosen_attack = choice([0, 1, 2])
        print(f"{me.name} uses {me.attacks[chosen_attack][0]} to {opponent.name}!")
        if random.random() < (1.0-self.miss_probability):
            damage = me.check_effectiveness(me.attacks[chosen_attack][1], opponent.element, me.attacks[chosen_attack][2])
            if damage > me.attacks[chosen_attack][2]: print("It's super effective!")
            elif damage < me.attacks[chosen_attack][2]: print("It's not super effective...")
            opponent.update_hitpoints(damage)
            me.update_hitpoints(me.attacks[chosen_attack][3])
        else:
            print("Oh no! It misses.")
        print(f"> {opponent.name} remaining hit points: {opponent.hit_points}.")
        print(f"> {me.name} remaining hit points: {me.hit_points}.")
        print(text_divider)


    def show_attacks(self):
        for index, i in enumerate(self.attacks, start=1):
            print(f"{index}. {i[0]}: {i[1]} type, {i[2]} hit points to opponent, {i[3]} hit points to self.")

    def check_effectiveness(self, attack_type=str, opponent_type=str, damage=int) -> int:
        if attack_type == "Fire" and opponent_type == "Grass":
            return (damage+10)
        elif attack_type == "Fire" and opponent_type == "Water":
            return (damage-10)
        elif attack_type == "Water" and opponent_type == "Fire":
            return (damage+10)
        elif attack_type == "Water" and opponent_type == "Grass":
            return (damage-10)
        elif attack_type == "Grass" and opponent_type == "Water":
            return (damage+10)
        elif attack_type == "Grass" and opponent_type == "Fire":
            return (damage-10)
        else: return damage


class Battle:

    def __init__(self, number=int, pokebot_one=object, pokebot_two=object) -> None:
        self.number = number
        self.player = [pokebot_one, pokebot_two]
        self.start_battle()

    def start_battle(self) -> None:
        print("Let's begin the battle!")
        print(f"Battle {self.number}: {self.player[0].name} vs {self.player[1].name}")
        print(text_divider)
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
        print(text_divider)
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
    "Bulbabot", "Grass", 75,[
        ["Floral Healing", "Healing", 0, -15],
        ["Cut", "Normal", 20, 0],
        ["Leaf Blade", "Grass", 15, 0]
    ]
    )

squirbot = Robot(
    "Squirbot", "Water", 75,[
        ["Absorb", "Healing", 10, -10],
        ["Tackle", "Normal", 20, 0],
        ["Aqua Tail", "Water", 15, 0]
    ]
    )

charmenbot = Robot(
    "Charmenbot", "Fire", 75,[
        ["Heal Pulse", "Healing", -5, -20],
        ["Quick Attack", "Normal", 20, 0],
        ["Fire Spin", "Fire", 20, 5]
    ]
    )

pokebot = [[bulbabot, True], [squirbot, True], [charmenbot, True]]
game = Game()