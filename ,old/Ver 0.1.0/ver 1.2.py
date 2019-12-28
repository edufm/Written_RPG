
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:22:07 2016

@author: Eduardo
"""

import numpy.random as ran
import time									#possibilita delays para dar tempo de ler---------------------------------------------------- delay

class character:  # -----------------------------------------------------------------------------------------------------  personagens
    def __init__(self, name, health, money, stamina, miss_chance, weapon):
        self.name = name
        self.health = health
        self.money = money
        self.stamina = stamina
        self.miss_chance = miss_chance
        self.weapon = weapon
        
class player(character):
    def __init__(self, name, health, money, stamina, miss_chance,  weapon, knightlevel, warriorlevel, marksmanlevel):
        character.__init__(self, name, health, money, stamina, miss_chance, weapon)
        self.knightlevel = knightlevel
        self.warriorlevel = warriorlevel
        self.marksmanlevel = marksmanlevel

class weapon:
    def __init__(self, name, damage, weight, Type, Range, value):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.Type = Type
        self.Range = Range
        self.value = value
        
class inventory: #  -------------------------------------------------------------------------------------------------------- inventario
    
    def __init__(self, maxitens):
        self.form = {}
        self.maxitens = maxitens
    
    def show_inventory():
        print(inventory.form)
        
    def addinventory(itemname, amount):
        if len(inventory.form) < inventory.maxitens:
            if itemname in inventory.form:
                inventory.form[itemname]+=amount
            else:
                inventory.form[itemname]+=amount
        else:
            loaded = ran.randint(0,1)
            if loaded == 0:
                print("you are overburned")
            else: 
                print("i can´t carry anymore")
    
    def removeinventory(itemname, amount):
        if itemname in inventory.form:
            inventory.form[itemname]-=amount
        else:
            print("you dont have enouth of this item")
            
class city: # -------------------------------------------------------------------------------------------------------- cidade
    def __init__(self):
        self.form = []
        
    def city():
        print("in this small town you have a blacksmith, a market and a fountain") 
        #e mais o que vcs quisrem
        main = int(input("what would you like to do?" "\n" "1 go to blacksmith" "\n" "2 go to market" "\n" "3 go to fountain" "\n" "4 go explore" "\n" "5 game menu"))
        if main == 1:
            city.blacksmith()
        if main == 2:
            city.market()
        if main == 3:
            city.fountain()
        if main == 4: 
            want = 1
            while want == 1:
                goblin = goblinrespawn()
                minotaur = minotaurrespawn()
                centaur = centaurrespawn()
                orc = orcrespawn()
                batalha()
                want = int(input("do you want to explore more?" "\n" "1 = yes" "\n" "2 = no"))
            city.city()
        if main == 5:
            Menu.Main()

    def blacksmith():
        print("greetings, are you looking to buy new items?")
        black = int(input("choose" "\n" "1 to buy" "\n" "2 to sell" "\n" "3 to go away"))
        if black == 1:
            print("sure") #agr com vc jean
            
        if black == 2:
            print("why would i buy your itens? if you want to sell them go to the market")
            city.city()
        if black == 3:
            city.city()
        
    def market():
        print("hey, are you looking to sell some itens?")
        market = int(input("choose" "\n" "1 to buy" "\n" "2 to sell" "\n" "3 to go away"))
        if market == 1:
            print("sure") #agr com vc jean
            
        if market == 2:
            print("sure") #agr com vc jean
            
        if market == 3:
            city.city()
        
    def fountain():
        print("all your wounds are healed")
        if classe == 1:
            player.health = 60
        if classe == 2:
            player.health = 80
        if classe == 3:
            player.health = 100
        city.city()
        
class Menu:
    def __init__(self):
        self.form = []
    
    def Main():
        main = int(input("Menu" "\n" "1 back to game" "\n" "2 save game" "\n" "3 load game" "\n" "4 options" "\n" "5 exit"))
        if main == 1:
            city.city()
        if main == 4:
            Menu.opitions()
        if main == 5:
            Menu.Exit()
             
    def options():
        print("sorry, no options so far")
        
    def Exit(): #-----------------------------------------------------------------------------------------------------------------------------elegante n ta mas funciona
        EX = int(input("this game does not save game automatically are u sure you wnat to exit?", "\n", "1 = no", "\n", "2 = maybe"))
        if EX == 1:
            city.city()
#aqui é nada mesmo ta certo
#-------------------------------------------------------------------------------------------------------- fim classes
#funções de combate 
def cenario(cenario, inimigo):
    print('you are in a', cenarios[cenario], ', here you found an aggressive', inimigos[inimigo], 'get ready to fight')
    enemy = inimigos[inimigo]    
    if enemy == goblin.name:
        return 0
    if enemy == minotaur.name:
        return 1
    if enemy == centaur.name:
        return 2
    if enemy == orc.name:
        return 3
        
def batalha():
    enemy = cenario(ran.randint(0,3),ran.randint(0,3))
    print('------------Batalha-------------')
    fighter = enemies[enemy]
    a = ran.randint(0,1)
    defend = 0
    if a == 0:
        print("the", fighter.name, "caught you off guard so he will start attacking")
        while (player.health > 0) and (fighter.health > 0):
            defend = AI(player,fighter, defend)
            if defend == 1:
                print("he defended")
            else:
                print('he atacked')
            print()
            print("health:", player.health)
            print("enemy health", fighter.health)
            defend = choose(player,fighter, defend)
            print("health:", player.health)
            print("enemy health", fighter.health)
    if a == 1:
        print("great, you managed to ambush the", fighter.name, "you start attacking")
        while (player.health > 0) and (fighter.health > 0):
            defend = AI(player,fighter, defend)
            if defend == 1:
                print("he defended")
            else:
                print('he atacked')
            print()
            print("health:", player.health)
            print("enemy health", fighter.health)
            defend = choose(player,fighter, defend)
            print("health:", player.health)
            print("enemy health", fighter.health)        
        
def choose(player, fighter, defend):
    print("what will you do? ")
    print("1 = attack")
    print("2 = defend")
    choose = int(input("choose "))
    if choose == 1:
        attack(fighter, player, defend)
    else:
        return Defend()

def Defend():
    return 1
    
def attack(defender, atacker, defend):
    miss = ran.randint(0,100)
    if miss <= defender.miss_chance:
        print("missed")
    if defend == 0:
        defender.health -= (atacker.weapon).damage
    else:
        defender.health -= ((atacker.weapon).damage/2)
        defend = 0
    
def AI(player,fighter, defend):
    AI = ran.randint(0,10)
    if AI <= 6:
        attack(player,fighter, defend)
    else: 
        return Defend()
        
def goblinrespawn():
    return character("goblin", ran.randint(30,50), ran.randint(20,40), 1000, 10, random_weapon())

def minotaurrespawn():
    return character("minotaur", ran.randint(30,50), ran.randint(20,40), 1000, 1, random_weapon())

def centaurrespawn():
    return character("centaur", ran.randint(30,50), ran.randint(20,40),1000, 1, random_weapon())

def orcrespawn():    
    return character("orc", ran.randint(30,50), ran.randint(20,40),1000, 2, random_weapon())
    
#funções iniciais
def escolha_classe():
    print('classes')
    print('1 = Marksman, You will handle ranged weapons extremely well')
    print('2 = Knight, You will handle light weapons extremely well')
    print('3 = Warrior, You will handle heavy weapons extremely well')
    return(int(input('Your choice: ')))
      
def random_weapon():
    return (weapons[ran.randint(0,3)])
    
#cria as listas de itns do jogo (TUDO STRING)
cenarios = ["swamp", "forest", "plain", "mountain"]
inimigos = ["goblin", "minotaur", "centaur", "orc"]
classes = ["Marksman", "Knight", "Warrior"]
           
#cria armas (name, damage, weight, Type, Range, value)
sword = weapon("sword", 7, 7, "slash",5, 20)
dagger = weapon("dagger", 4, 1, "piercing",2, 10)
hammer = weapon("hammer", 8, 10, "blunt", 6, 40)
pistol = weapon("pistol", 9, 2, "ranged", 60, 100)

#cria a lista de armas do jogo
weapons = [sword, dagger, hammer, pistol]

#cria criaturas (1st)
goblin = goblinrespawn()
minotaur = minotaurrespawn()
centaur = centaurrespawn()
orc = orcrespawn()

#cria a lista de enemigos do jogo
enemies = [goblin, minotaur, centaur, orc]

#------------------------------------------GAMEPLAY-------------------------------------------------
#first print (decisões iniciais)
print('welcome to panau, explorer’')
nome = input("what’s your name? ")
print('You are an apprentice and lately you have been working to become a:')
#escolher classe(equipamento inicial)
classe = escolha_classe()
if classe == 1:
   weapon1 = pistol
   health = 60
   miss_chance = 5
   stamina = 40
   marksmanlevel = 1
   knightlevel = 0
   warriorlevel = 0
   
if classe == 2:   
   weapon1 = sword
   health = 80
   miss_chance = 3
   stamina = 60
   marksmanlevel = 0
   knightlevel = 1
   warriorlevel = 0
   
if classe == 3:
   weapon1 = hammer
   health = 100
   miss_chance = 1
   stamina = 50
   marksmanlevel = 0
   knightlevel = 0
   warriorlevel = 1

#inicializa player e inventario
inventory = inventory(10)
player = player(nome, health, 0, stamina, miss_chance, weapon1, knightlevel, warriorlevel, marksmanlevel)

#começa o jogo
print("what a coincidence, you just said you want to become a", classes[classe-1], "and a", weapon1.name, 'fell from the sky to your hands!')
print("weird, anyway let’s go to the city")
time.sleep(1)

#-----tutorial:
print('oh no, it seems you stumbled upon an enemy')
time.sleep(1)
batalha()
print("great you survived")
time.sleep(1)
print("well that´s getting weird, weapon from the sky a convenient introductory battle...")
time.sleep(1)
print("lets get to the city already")
time.sleep(1)
print("here we are")
city.city()