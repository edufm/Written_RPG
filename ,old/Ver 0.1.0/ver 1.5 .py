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
        
    def goblinrespawn(weapon):
        return character("goblin", ran.randint(30,50), ran.randint(20,40), 1000, 10, random_weapon(weapon))
    
    def minotaurrespawn(weapon):
        return character("minotaur", ran.randint(30,50), ran.randint(20,40), 1000, 1, random_weapon(weapon))
    
    def centaurrespawn(weapon):
        return character("centaur", ran.randint(30,50), ran.randint(20,40),1000, 1, random_weapon(weapon))
    
    def orcrespawn(weapon):    
        return character("orc", ran.randint(30,50), ran.randint(20,40),1000, 2, random_weapon(weapon))
        

class player:
    def __init__(self, name, money, vitality, endurance, dexterity,  strenght):
        self.name = name
        self.money = money
        self.vitality = vitality
        self.endurance = endurance
        self.dexterity = dexterity
        self.strenght = strenght
      
    def Start_health():
        return player.vitality
        
    def DamageGiven(weapon, classe):
        if classe == 1:
            return ((weapon.damage*player.dexterity)/100) 
        if classe == 2:
            return ((weapon.damage*player.dexterity*player.stregth)/(100*100))
        if classe == 3:
            return ((weapon.damage*player.stregth)/(100))
    
    def Staminaloss():
        return player.endurance*100/equipped.total_weight()
        
    def damage_percent_taken():
        return (player.endurance*equipped.total_armor())/100
        
    def miss_chance():
        return (player.dexterity-equipped.total_weight())
    
class equipped:
    def __init__(self, weapon, head, chest, arm, hand, legs, feet):
        self.weapon = weapon        
        self.head = head
        self.chest = chest        
        self.arm = arm
        self.hand = hand
        self.legs = legs
        self.feet = feet
        
    def total_armor(equipped):
        return (equipped.head.armor)+(equipped.chest.armor)+(equipped.arm.armor)+(equipped.hand.armor)+(equipped.legs.armor)+(equipped.feet.armor)        
        
    def total_weight(equipped):
        return (equipped.head.weight)+(equipped.chest.weight)+(equipped.arm.weight)+(equipped.hand.weight)+(equipped.legs.weight)+(equipped.feet.weight)

class itens:
    def __init__(self, name, weight, Type, value, durability, quality):
         self.name = name
         self.weight = weight
         self.Type = Type
         self.value = value
         self.durability = durability
         self.quality = quality
        
class armor(itens):
    def __init__(self, name, weight, Type, Range,  defense, enchantment, value, durability, quality):
        itens.__init__(self, name, weight, Type, value, durability, quality)
        self.defense = defense
        self.enchantment = enchantment

class weapons(itens):
    def __init__(self, name, damage, weight, Type, Range, value, durability, quality):
        itens.__init__(self, name, weight, Type, value, durability, quality)
        self.damage = damage
        self.Range = Range
            
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
                print("You are overburned")
            else: 
                print("I can´t carry anything else or I might faint...")
    
    def removeinventory(itemname, amount):
        if itemname in inventory.form:
            inventory.form[itemname]-=amount
        else:
            print("You don't have enough of this item!")
            
class city: # -------------------------------------------------------------------------------------------------------- cidade
    def __init__(self):
        self.form = []
        
    def city():
        print("In this small town you have a blacksmith, a market and a fountain")
        print()
        #e mais o que vcs quisrem
        print("you have", player.money, "Erens")
        if player.money > 300:
            print("you really should spend this")
            print()
        main = Intinput("what would you like to do?" "\n" "1 go to blacksmith" "\n" "2 go to market" "\n" "3 go to fountain" "\n" "4 go explore" "\n" "5 game menu", 1,6)
        if main == 1:
            city.blacksmith()
        if main == 2:
            city.market()
        if main == 3:
            city.fountain()
        if main == 4: 
            want = 1
            while want == 1:
                batalha()
                want = Intinput("Do you want to explore more? " "\n" "1 = yes" "\n" "2 = no", 1,3)
            city.city()
        if main == 5:
            Menu.Main()

    def blacksmith():
        print("Greetings traveler, are you looking to buy new items?")
        black = int(input("choose" "\n" "1 to buy" "\n" "2 to sell" "\n" "3 to go away"))
        if black == 1:
            print("sure") #agr com vc jean
            input("press something plea;se")
            blacks_inventory()
            
        if black == 2:
            print("Why would i buy your items? if you want to sell them go to the market")
            city.city()
        if black == 3:
            city.city() 
            
    def market():
        print("Hello there young one, are you looking to sell some items? ")
        market = Intinput("choose" "\n" "1 to buy" "\n" "2 to sell" "\n" "3 to go away", 1,4)
        if market == 1:
            print("sure") #agr com vc jean
            
        if market == 2:
            print("sure") #agr com vc jean
            
        if market == 3:
            city.city()
        
    def fountain():
        print("All your wounds are healed!")
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
        main = Intinput("Menu" "\n" "1 back to game" "\n" "2 save game" "\n" "3 load game" "\n" "4 options" "\n" "5 exit",1,6)
        if main == 1:
            city.city()
        if main == 4:
            Menu.options()
        if main == 5:
            Menu.Exit()
             
    def options():
        print("Sorry, no options so far")
        Menu.Main
        
    def Exit(): #----------------------------------------------------------------------------------------elegante n ta mas funciona
        EX = Intinput("This game does not save game automatically are you sure you want to exit? " "\n" "1 = no" "\n" "2 = maybe",1,3)
        if EX == 1:
            city.city()
        else:
            Intinput("Are you sure? " "\n" "1 = no" "\n" "2 = yes, LET ME GO!!!",1,3)
            if EX == 1:
                city.city()
#aqui é nada mesmo ta certo
#-------------------------------------------------------------------------------------------------------- fim classes
#funções de combate 
def cenario(cenario, inimigo):
    print('You are in a', cenarios[cenario], ', here you found an aggressive', inimigos[inimigo], 'get ready to fight')
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
    a = ran.randint(0,2)
    defend = 0
    goblin.health = ran.randint(30,50)
    centaur.health = ran.randint(30,50)
    minotaur.helath = ran.randint(30,50)
    orc.health = ran.randint(30,50)
    if a == 0:
        print("Oh no! The", fighter.name, "caught you off guard so it will start attacking!")
        while (float(player.health) > 0) and (float(fighter.health) > 0):
            defend = AI(player,fighter, defend)
            if defend == 1:
                print("It protects itself against you!")
            else:
                print('It attacks you!')
            print()
            print("health:", player.health)
            print("enemy health", fighter.health)
            defend = choose(player,fighter, defend)
            print("health:", player.health)
            print("enemy health", fighter.health)
        player.money += fighter.money
    if a == 1:
        print("Great, you managed to ambush the", fighter.name, "you start attacking!")
        while (float(player.health) > 0) and (float(fighter.health) > 0):
            defend = AI(player,fighter, defend)
            if defend == 1:
                print("It protects itself against you!")
            else:
                print('It attacks you!')
            print()
            print("health:", player.health)
            print("enemy health", fighter.health)
            defend = choose(player,fighter, defend)
            print("health:", player.health)
            print("enemy health", fighter.health)        
        player.money += fighter.money
        
def choose(player, fighter, defend):
    print("what will you do? ")
    print("1 = attack")
    print("2 = defend")
    choose = Intinput("choose: ", 1,3)
    if choose == 1:
        attack(fighter, player, defend)
    else:
        return Defend()

def Defend():
    return 1
    
def attack(defender, atacker, defend):
    miss = ran.randint(0,100)
    if miss <= defender.miss_chance:
        print("missed!")
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
        
    
def Intinput(text, ini,end):
    Test = input(text)
    listoftest = []
    for i in range(ini,end):
        listoftestappend = str(i)
        listoftest.append(listoftestappend)
    while not Test in listoftest:
        print("Not a valid option")
        Test = input("Try again, because you are too good to read the text above right??? ")
    return int(Test)
    
    #----------------------
def blacks_inventory():   
    bs_money = ran.randint(400,3000)
    print('blacksmith store money' , bs_money)
    print('currency:' , player.money, "Erens")
    print('no momento o jean não fez coisas uteis aki, mas voce pode gastar seu dineiro a vontade :)')
    print('choose a weapon kid: ','\n','1 - spend 50 ','\n','2 - spend 150' , '\n', '3 - spend all', '\n' ,'4 - go back' )
    x = input("how much you can waste now?")
    if x == "1":
        if player.money >= 50:
            player.money -= 50
            bs_money += 50
            print("all done pal, gimme money for being incomplete", '\n')
        else:
            print("sorry pal, go get some gold from the goblins kidneys", '\n')
        blacks_inventory()
    if x == "2":
        if player.money >= 150:
            player.money -= 150
            bs_money += 150
            print("all done pal, gimme money for being incomplete")
        else:
            print("sorry pal, go get some gold from the goblins kidneys")
        blacks_inventory()
    if x == "3":
        print("are you sure kid?")
        print('"he did not wait for you to think about it and the programmers already removed all your money...')
        print('sorry if you would reconsider, at least he is happy')
        bs_money += player.money
        player.money = 0
        print("all done pal, gimme money for being incomplete")
        blacks_inventory()
    if x == '4':
        city.blacksmith()
        
        #---------------------
   
#funções iniciais
def escolha_classe():
    print()
    print('Classes:')
    print('1 = Marksman, You will handle ranged weapons extremely well')
    print('2 = Knight, You will handle light weapons extremely well')
    print('3 = Warrior, You will handle heavy weapons extremely well')
    return Intinput('Your choice: ', 1,4)
      
def random_weapon(weapon):
    return (weapon[ran.randint(0,3)])
    
#cria as listas de itns do jogo (TUDO STRING)
cenarios = ["swamp", "forest", "plain", "mountain"]
inimigos = ["goblin", "minotaur", "centaur", "orc"]
classes = ["Marksman", "Knight", "Warrior"]
           
#cria armas (name, damage, weight, Type, Range, value)
sword =  weapons("sword", 7, 7, "slash",5, 20, 100, "b")
dagger = weapons("dagger", 4, 1, "piercing",2, 10, 25, "b")
hammer = weapons("hammer", 8, 10, "blunt", 6, 40, 200, "b")
pistol = weapons("pistol", 9, 2, "ranged", 60, 100, 50, "b")

#cria a lista de armas do jogo
weapon = [sword, dagger, hammer, pistol]

#cria criaturas (1st)
goblin = character.goblinrespawn(weapon)
minotaur = character.minotaurrespawn(weapon)
centaur = character.centaurrespawn(weapon)
orc = character.orcrespawn(weapon)

#cria a lista de enemigos do jogo
enemies = [goblin, minotaur, centaur, orc]

#cria variaveis necessarias
playerhealth = 0
playerstamina = 0

#------------------------------------------GAMEPLAY-------------------------------------------------
#first print (decisões iniciais)
print('+-----------------------------+')
print('| Welcome to panau, traveler! |')
print('+-----------------------------+')
nome = input("What's your name? ")
print('It looks like you are one of those youngsters who have been traveling around lately in order to become a hero are you not? Oh? It looks like you already started your quest in becoming a:')
#escolher classe(equipamento inicial)
classe = escolha_classe()
if classe == 1:
   weapon1 = pistol
   vitality = 70
   dexterity = 100
   endurance = 60
   strenght = 40
      
if classe == 2:   
   weapon1 = sword
   vitality = 80
   dexterity = 80
   endurance = 60
   strenght = 60
   
if classe == 3:
   weapon1 = hammer
   vitality = 100
   dexterity = 40
   endurance = 60
   strenght = 80

#inicializa player e inventario
inventory = inventory(10)
player = player(nome, 0, vitality, endurance, dexterity,  strenght)

#começa o jogo
print("And it looks like you already obtained a", weapon1.name, ', good for you!')
print("Anyway we should head to the city so you can establish youself and rest.")
time.sleep(1)

#-----tutorial:
print('Oh no, it seems you stumbled upon an enemy!')
time.sleep(1)
batalha()
print("Great! you survived!")
time.sleep(1)
print("Well you are quite the lucky one, managing to survive that.")
time.sleep(1)
print("We should hurry to the city or else more weird stuff might appear.")
print('...')
time.sleep(1)
print("Here we are!")
city.city()