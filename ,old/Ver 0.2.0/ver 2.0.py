# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:22:07 2016

@author: Eduardo
"""
import sys
sys.path.append(".")

import numpy.random as ran
import time									#possibilita delays para dar tempo de ler---------------------------------------------------- delay
import math

import pickle

class player:  # -----------------------------------------------------------------------------------------------------  personagens
    def __init__(self, name, money, vitality, health, endurance, dexterity,  strenght, level, exppoints):
        self.name = name
        self.level = level
        self.money = money
        self.vitality = vitality
        self.endurance = endurance
        self.dexterity = dexterity
        self.strenght = strenght
        self.exppoints = exppoints
        self.health = health
      
    def Start_health(player):
        return int(player.vitality)
        
    def DamageGiven(player, weapon, classe):
        if classe == 1:
            return ((weapon.damage*player.dexterity)/100) 
        if classe == 2:
            return ((weapon.damage*player.dexterity*(player.strenght))/(100*100))
        if classe == 3:
            return ((weapon.damage*(player.strenght))/(100))
    
    def Staminaloss(player):
        return player.endurance*100/equipped.total_weight()
        
    def damage_percent_taken(player):
        return (player.endurance*equipped.total_armor(equipped))/(100*50)
        
    def miss_chance(player):
        return (player.dexterity-equipped.total_weight(equipped))
        
    def print_stats(player):
        print(player.name, "you are level:", player.level)
        print("you have", player.exppoints, "experience")
        print("Dexterity:", player.dexterity)
        print("Strength:", player.strenght)
        print("Endurance:", player.endurance)
        print("Vitality:", player.vitality)
        print("Life", player.health)
        
    def needed_exp(player, level):
        points = 0
        for level in range(1,100):
            diff = int(level + 300 * math.pow(2, float(level)/7) )
            points += diff
            return points/4 
            
    def level_up(player):
        if player.exppoints >= player.needed_exp(player.level):
            player.level += 1
            print("you leveled up, now you are level:", player.level)
            print("distribute your new atribute points, you have five of them")
            print("1 for Dexterity, you already have", player.dexterity, "points")
            print("2 for Strength, you already have", player.strenght, "points")
            print("3 for Endurance, you already have", player.endurance, "points")
            print("4 for Vitality, you already have", player.vitality, "points")
            for i in range(0,5)    :        
                Level = Intinput("choose:", 1, 5)
                if Level == 1:
                    player.dexterity += 1
                    print("point added")
                if Level == 2:
                    player.strenght += 1
                    print("point added")
                if Level == 3:
                    player.endurance += 1
                    print("point added")
                if Level == 4:
                    player.vitality += 1
                    print("point added")
            city.city()
        else:
            print("you dont have enought experience points")
            city.city()

class creatures:
    def __init__(self, name, money, vitality, health, endurance, dexterity, strenght, level, exppoints, weapon, feet, legs, chest, arm, hand, head):

        self.name = name
        self.money = money
        self.vitality = vitality
        self.health = health
        self.endurance = endurance
        self.dexterity = dexterity
        self.strenght =strenght
        self.level = player.level
        self.exppoints = exppoints
        self.weapon = weapon        
        self.head=head        
        self.chest=chest
        self.arm=arm
        self.hand=hand
        self.legs = legs
        self.feet = feet
        
class equipped:
    def __init__(self, weapon, head, chest, arm, hand, legs, feet):
        self.weapon = weapon        
        self.head = head
        self.chest = chest        
        self.arm = arm
        self.hand = hand
        self.legs = legs
        self.feet = feet
    
    def print_equiped():
        print("weapon", equipped.weapon)
        print("head", equipped.head)
        print("chest", equipped.chest)
        print("arm", equipped.arm)
        print("hand", equipped.hand)
        print("legs", equipped.legs)
        print("feet", equipped.feet)
        
    def total_armor(equipped):
        totalarmor = (equipped.head.defense)+(equipped.chest.defense)+(equipped.arm.defense)+(equipped.hand.defense)+(equipped.legs.defense)+(equipped.feet.defense)        
        if totalarmor == 0:
            return 1
        else:
            return totalarmor
        
    def total_weight(equipped):
        totalweight = (equipped.head.defense)+(equipped.chest.defense)+(equipped.arm.defense)+(equipped.hand.defense)+(equipped.legs.defense)+(equipped.feet.defense)
        if totalweight == 0:
            return 1
        else:
            return totalweight
    
    def equip(item):
        if item is armor:
            if item.type == "head":
                equipped.head = item
            if item.type == "arm":
                equipped.arm = item
            if item.type == "leg":
                equipped.leg = item
            if item.type == "feet":
                equipped.feet = item
            if item.type == "hand":
                equipped.hand = item
            if item.type == "chest":
                equipped.chest = item            
        if item is weapon:
            equipped.weapon = item
        else:
            print("cant equip this item")
            

class itens:
    def __init__(self, name, weight, Type, value, quality, stackable):
         self.name = name
         self.weight = weight
         self.Type = Type
         self.value = value
         self.quality = quality
         self.stackable = stackable
         
    def itemstatus(item):
        if item is armor:
            print(item.name)
            print("armor:", item.defense)
            print("weight:", item.weight)
            print("durability:", item.used, "/", item.durability)
            print("value", item.value)
        if item is weapon:
            print(item.name)
            print("damage:", item.damage)
            print("weight:", item.weight)
            print("durability:", item.durability)
            print("value", item.value)
        else:
            print(item.name)
            print("weight:", item.weight)
            print("value", item.value)
        
class armor(itens):
    def __init__(self, name, weight, Type, value, durability, used, quality, defense, enchantment, stackable):
        itens.__init__(self, name, weight, Type, value, quality, stackable)
        self.defense = defense
        self.enchantment = enchantment
        self.durability = durability   
        self.used = used
        
class weapons(itens):
    def __init__(self, name, damage, weight, Type, Range, value, durability, used, quality, stackable):
        itens.__init__(self, name, weight, Type, value, quality, stackable)
        self.damage = damage
        self.Range = Range
        self.durability = durability  
        self.used = used
            
class inventory: #  -------------------------------------------------------------------------------------------------------- inventario
    
    def __init__(self, form, maxitens):
        self.form = form
        self.maxitens = maxitens
    
    def show_inventory(player, inventory):
        for i in (inventory.form):
            print(i.name)
        print("1 to drop item" "\n" "2 to see item stats" "\n" "3 to equip item" "\n" "4 to go back")
        inv = Intinput("choose a option", 1, 5)
        if inv == 1:
            Iten = inventory.string_to_object()
            if  Iten.stackable > 1:
                amount = Intinput("how many?" "\n" "0 to all" "x for amount", 1, 10)
                if amount == 0:
                    inventory.removeinventory(Iten, 0)
                if amount != 0:
                    inventory.removeinventory(Iten, amount)
            if Iten.stackable == 0:
                inventory.removeinventory(Iten, 0)
        if inv == 2:
            Iten = inventory.string_to_object()
            itens.itemstatus(Iten)
        if inv == 3:
            Iten = inventory.string_to_object()
            equipped.equip()
            
    def string_to_object(itens):
        Iten = input("choose, name of item")
        Iten = eval(Iten)
        return Iten
                                           
    def addinventory(player, itemname, amount):
        if len(inventory.form) < inventory.maxitens:
            if itemname in inventory.form:
                inventory.form[itemname]+=amount
            else:
                inventory.form[itemname]=amount
        else:
            loaded = ran.randint(0,1)
            if loaded == 0:
                print("You are overburned")
            else:
                print("I can´t carry anything else or I might faint...")
    
    def removeinventory(player, itemname, amount):
        if amount == 0:
            if itemname in inventory.form:
                del inventory.form[itemname]
        if amount != 0:
            if itemname in inventory.form:
                inventory.form[itemname] -= amount
        else:
            print("You don't have enough of this item!")
            
class home:
    def __init__(self, storage):
        self.storage = storage
        
    def home(player):
        print("you got to your home")
        print()
        main = Intinput("what would you like to do?" "\n" "1 go sleep" "\n" "2 storage itens" "\n" "3 character related stuff" "\n" "4 game menu" "\n" "5 - go back", 1,6)
        if main == 1:
            print("its morning")
        if main == 2:
            home.usestorage()
        if main == 3:
            home.char()
        if main == 4:
            Menu.Main()                  
        if main == 5:
            city.city()
        
    def usestorage(player):
        print()
        print("you have in your inventory")
        for i in (inventory.form):
            print(i.name)
        print()
        print("you have stored")
        for i in (home.storage):
            print(i.name)
        print()
        print("1 to store item" "\n" "2 to take item" "\n" "3 to go back")
        inv = Intinput("choose a option", 1, 4)
        if inv == 1:
            Iten = inventory.string_to_object()
            home.addstorage(Iten)
            home.home()
        if inv == 2:
            Iten = inventory.string_to_object()
            home.pickitem(Iten)
            home.home()
        if inv == 3:
            home.home()

    def addstorage(player, Iten):
       if  Iten.stackable > 1:
           amount = Intinput("how many?" "\n" "0 to all" "x for amount", 1, 10)
           if amount == 0:
               home.storage[Iten] = (inventory.form[Iten])
               inventory.removeinventory(Iten, 0)
           if amount != 0:
               home.storage[Iten] = (amount)
               inventory.removeinventory(Iten, amount)
       if Iten.stackable == 0:
           home.storage[Iten] = 1
           inventory.removeinventory(Iten, 0)
           
    def pickitem(itens, Iten):
        if  Iten.stackable > 1:
           amount = Intinput("how many?" "\n" "0 to all" "x for amount", 1, 10)
           if amount == 0:
               inventory.addinventory(Iten, home.storage[Iten])
               del((home.storage)[Iten])
           if amount != 0:
               home.storage[Iten] -= (amount)
               inventory.addinventory(Iten, amount)
        if Iten.stackable == 0:
            del((home.storage)[Iten])
            inventory.addinventory(Iten, 1)
 
        
    def char(home):
        print("what do you want to know?")
        Char = Intinput("1 - Stats" "\n" "2- equiped itens" "\n" "3 - inventory" "\n" "4 - go back", 0 , 5)
        if Char == 1:
            player.print_stats()
            home.char()
        if Char == 2:
            equipped.print_equiped()
            home.char()
        if Char == 3:
            inventory.show_inventory(inventory)
            home.char()
        if Char == 4:
            home.home()
            
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
        main = Intinput("what would you like to do?" "\n" "1 go to blacksmith" "\n" "2 go to market" "\n" "3 go to fountain" "\n" "4 go to sorcerer" "\n" "5 go explore" "\n" "6 go home", 1,7)
        if main == 1:
            city.blacksmith()
        if main == 2:
            city.market()
        if main == 3:
            city.fountain()
        if main == 4:
            city.sorcerer()
        if main == 5: 
            want = 1
            while want == 1:
                batalha()
                want = Intinput("Do you want to explore more? " "\n" "1 = yes" "\n" "2 = no", 1,3)
            city.city()
        if main == 6:
            home.home()
            

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
            city.city
            
        if market == 2:
            print("sure") #agr com vc jean
            city.city
            
        if market == 3:
            city.city()
        
    def fountain():
        print("All your wounds are healed!")
        player.health = player.vitality
        city.city()
        
    def sorcerer():
        print("I sense a soul in search of answers...")
        print("1 - Redeme your Experience (level up)")
        print("2 - Buy itens")
        print("3 - Sell itens")
        print("4 - go back")
        Sorc = Intinput("Choose: ", 1,5)
        if Sorc == 1:
            player.level_up()
            city.city()
        if Sorc == 2:
            print("sure") #agr com vc jean
            city.city()
        if Sorc == 3:
            print("sure") #agr com vc jean
            city.city()
        if Sorc == 4:
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
    tupla = [0,0]    
    goblin.health = goblin.vitality
    centaur.health =centaur.vitality
    minotaur.helath = minotaur.vitality
    orc.health = orc.health
    if a == 0:
        while (float(player.health) > 0) and (float(fighter.health) > 0):
            tupla = AI(fighter, tupla[1])
            if tupla[1] == 1:
                print("It protects itself against you!")
            else:
                player.health = round(tupla[0])
                print('It attacks you!')
            print()
            print("health:", player.health)
            print("enemy health", round(fighter.health))
            tupla[1] = choose(player,fighter, (tupla[1]))
            print("health:", player.health)
            print("enemy health", round(fighter.health))
        player.money += fighter.money
        player.exppoints += ran.randint(20,30)
        inventory.addinventory(fighter.weapon, 1)
    if a == 1:
        while (float(player.health) > 0) and (float(fighter.health) > 0):
            tupla = AI(fighter, tupla[1])
            if int(tupla[1]) == 1:
                print("It protects itself against you!")
            else:
                player.health = round(tupla[0])
                print('It attacks you!')
            print()
            print("health:", player.health)
            print("enemy health", round(fighter.health))
            tupla[1] = choose(player,fighter, (tupla[1]))
            print("health:", player.health)
            print("enemy health", round(fighter.health))
        player.money += fighter.money
        player.exppoints += ran.randint(20,30)
        inventory.addinventory(fighter.weapon, 1)
        
def choose(player, fighter, defend):
    print("what will you do? ")
    print("1 = attack")
    print("2 = defend")
    choose = Intinput("choose: ", 1,3)
    if choose == 1:
        return attack(player, fighter, defend, equipped.weapon, classe)
    else:
        return 1
    
def attack(player, fighter, defend, weapon, classe):
    miss = ran.randint(0,100)
    if miss <= 1:
        print("missed!")
        return 0
    if defend == 0:
        fighter.health -= player.DamageGiven(weapon, classe)
        return 0
    else:
        fighter.health -= (player.DamageGiven(weapon, classe)/2)
        return 0
    
def AI(fighter, defense):
    AI = ran.randint(0,10)
    if AI <= 7:
        fighterdamage = fighter.weapon.damage
        yourresistence = (player.damage_percent_taken())
        if defense == 0:
            player.health -= (1-yourresistence)*fighterdamage
            return [player.health, 0]
        else:
            player.health -= ((1-yourresistence)*fighterdamage)/2
            return [player.health, 0]
    else: 
        return [player.health, 1]
        
    
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
           
#cria armas ( name, damage, weight, Type, Range, value, durability, used, quality, stackable)
sword =  weapons("sword", 7, 7, "slash", 5 , 20, 100, 100, "b", 0)
dagger = weapons("dagger", 4, 1, "piercing", 2 , 10, 25, 25, "b", 0)
hammer = weapons("hammer", 8, 10, "blunt", 6, 40, 200, 200, "b", 0)
pistol = weapons("pistol", 9, 2, "ranged", 60, 100, 50, 50, "b", 0)

#cria roupas iniciais do player name, weight, Type, value, durability, used, quality, defense, enchantment, stackable)
head_naked = armor("head_naked", 0, "Head", 0, -1, -1, "b", 0, "none", 0)
chothshirt =  armor("chothshirt", 0, "Chest", 0, -1, -1,"b", 0, "none", 0)
clothttrousers =  armor("clothttrousers", 0, "Leg", 0, -1, -1, "b", 0, "none", 0)
feet_naked =  armor("feet_naked", 0, "Feet", 0, -1, -1, "b", 0, "none", 0)
arm_naked =  armor("arm_naked", 0, "Arm", 0, -1, -1, "b", 0, "none", 0)
hand_naked =  armor("hand_naked", 0, "Habd", 0, -1, -1, "b", 0, "none", 0)


#cria a lista de armas do jogo
weapon = [sword, dagger, hammer, pistol]


#cria itens escenciais player
home = home({})
inventory = inventory({}, 10)
#--------------------------------------------MENU--------------------

#------------------------------------------GAMEPLAY-------------------------------------------------
#first print (decisões iniciais)
print('+-----------------------------+')
print('| Welcome to Panau, traveler! |')
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

#inicializa player:
player = player(nome, 0, vitality, vitality, endurance, dexterity,  strenght, 1, 30)

#equip various armors
equipped.head = head_naked
equipped.chest = chothshirt
equipped.legs = clothttrousers
equipped.feet = feet_naked
equipped.arm = arm_naked
equipped.hand = hand_naked

#equip weapon
equipped.weapon = weapon1

#cria criaturas (name, money, vitality, health, endurance, dexterity,  strenght, level, exppoints, weapon, feet, legs, chest, arm, hand, head)
goblin = creatures("goblin", 50, 40, 40, 20, 100, 50, 1, ran.randint(30,50)*player.level/2, dagger, feet_naked, clothttrousers, chothshirt, arm_naked, hand_naked,head_naked)
minotaur = creatures("minotaur", 10, 100, 100, 60, 20, 70, 1, ran.randint(30,50)*player.level/2, hammer, feet_naked, clothttrousers, chothshirt, arm_naked, hand_naked,head_naked)
centaur = creatures("centaur", 25, 70, 70, 60, 40, 60, 1, ran.randint(30,50)*player.level/2, sword, feet_naked, clothttrousers, chothshirt, arm_naked, hand_naked,head_naked)
orc = creatures("orc", 40, 80, 80, 60, 20, 80, 1, ran.randint(30,50)*player.level/2, hammer, feet_naked, clothttrousers, chothshirt, arm_naked, hand_naked,head_naked)

#cria a lista de enemigos do jogo
enemies = [goblin, minotaur, centaur, orc]

if nome == "dev":
    player.money = 300
    player.exppoints = 100
    inventory.addinventory(hammer, 1)
    inventory.addinventory(dagger, 1)    
    city.city()
    
else:
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
    

