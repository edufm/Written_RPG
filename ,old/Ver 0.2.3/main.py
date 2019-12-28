
import sys
sys.path.append(".") 				# possibilita dar import em coisas do mesmo diretório

import numpy.random as ran
import time									#possibilita delays para dar tempo de ler---------------------------------------------------- delay
import math

import pickle 							# vai possibilitar salvar jogos

class player:  # -----------------------------------------------------------------------------------------------------  personagens
    def __init__(self, name, money, vitality, health, endurance, stamina, dexterity,  strenght, level, exppoints):
        self.name = name
        self.level = level
        self.money = money
        self.vitality = vitality
        self.endurance = endurance
        self.dexterity = dexterity
        self.strenght = strenght
        self.exppoints = exppoints
        self.health = health
        self.stamina = stamina
      
    def Start_health(player):
        return int(player.vitality)
        
    def DamageGiven(player, weapon, classe):
        if classe == 1:
            return ((weapon.damage*player.dexterity)/100) 
        if classe == 2:
            return ((weapon.damage*player.dexterity*(player.strenght))/(100*100))
        if classe == 3:
            return ((weapon.damage*(player.strenght))/(100))
    
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
    def __init__(self, name, money, vitality, health, endurance, stamina, dexterity, strenght, level, exppoints, weapon, feet, chest, hand, head):

        self.name = name
        self.money = money
        self.vitality = vitality
        self.stamina = stamina
        self.health = health
        self.endurance = endurance
        self.dexterity = dexterity
        self.strenght =strenght
        self.exppoints = exppoints
        self.weapon = weapon        
        self.head=head        
        self.chest=chest
        self.hand=hand
        self.feet = feet
        
class equipped:
    def __init__(self, weapon, head, chest, hand, feet):
        self.weapon = weapon        
        self.head = head
        self.chest = chest        
        self.hand = hand
        self.feet = feet
    
    def print_equiped():
        print("weapon", equipped.weapon)
        print("head", equipped.head)
        print("chest", equipped.chest)
        print("hand", equipped.hand)
        print("feet", equipped.feet)
        
    def total_armor(equipped):
        totalarmor = (equipped.head.defense)+(equipped.chest.defense)+(equipped.hand.defense)+(equipped.feet.defense)        
        if totalarmor == 0:
            return 1
        else:
            return totalarmor
        
    def total_weight(equipped):
        totalweight = (equipped.head.weight)+(equipped.chest.weight)+(equipped.hand.weight)+(equipped.feet.weight)
        if totalweight == 0:
            return 1
        else:
            return totalweight
    
    def equip(item):
        if item is armor:
            if item.type == "head":
                equipped.head = item
            if item.type == "feet":
                equipped.feet = item
            if item.type == "hand":
                equipped.hand = item
            if item.type == "chest":
                equipped.chest = item            
        if item is weapons:
            equipped.weapon = item
        else:
            print("can't equip this item")
            

class itens:
    def __init__(self, name, weight, Type, value, stackable):
         self.name = name
         self.weight = weight
         self.Type = Type
         self.value = value
         self.stackable = stackable
         
    def itemstatus(item):
        if item is armor:
            print(item.name)
            print("armor:", item.defense)
            print("weight:", item.weight)
            print("durability:", item.used, "/", item.durability)
            print("value", item.value)
        if item is weapons:
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
    def __init__(self, name, defense, weight, value, material, Type, durability, used, stackable):
        itens.__init__(self, name, weight, Type, value, stackable)
        self.defense = defense
        self.durability = durability   
        self.used = used
        
class weapons(itens):
    def __init__(self, name, damage, weight, value, material, Type, durability, used, stackable):
        itens.__init__(self, name, weight, Type, value, stackable)
        self.damage = damage
        self.material = material
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
        main = Intinput("What would you like to do?" "\n" "1 go sleep" "\n" "2 storage itens" "\n" "3 character related stuff" "\n" "4 game menu" "\n" "5 - go back", 1,6)
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
        print("You have in your inventory")
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
           amount = Intinput("How many?" "\n" "0 to all" "x for amount", 1, 10)
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
        print("What do you want to know?")
        Char = Intinput("1 - Stats" "\n" "2- equipped items" "\n" "3 - inventory" "\n" "4 - go back", 0 , 5)
        if Char == 1:
            player.print_stats()
            home.char()
        if Char == 2:
            equipped.print_equipped()
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
        print("In this small town you have a blacksmith, a market and a fountain.")
        print()
        #e mais o que vcs quisrem
        print("You have", player.money, "Erens")
        if player.money > 300:
            print("You really should spend this")
            print()
        main = Intinput("What would you like to do?" "\n" "1 go to blacksmith" "\n" "2 go to market" "\n" "3 go to fountain" "\n" "4 go to sorcerer" "\n" "5 go explore" "\n" "6 talk to Kid" "\n" "7 go home", 1, 8)
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
            city.kid()
        if main == 7:
            home.home()
            
    def blacksmith():
        print("Greetings traveler, are you looking to buy new items?")
        black = int(input("choose" "\n" "1 to buy" "\n" "2 to sell" "\n" "3 to go away"))
        if black == 1:
            print("sure") #agr com vc jean
            input("press something plea;se")
            blacks_inventory()
            
        if black == 2:
            print("Why would I buy your items? if you want to sell them go to the market")
            city.city()
        if black == 3:
            city.city() 
            
    def market():
        print("Hello there young one, are you looking to sell some items? ")
        market = Intinput("choose" "\n" "1 to buy" "\n" "2 to sell" "\n" "3 to go away", 1,4)
        if market == 1:
            print("sure") #agr com vc jean
            market_inventory()
            
        if market == 2:
            print("huhu...sorry pal, I'm not buying your low grade equipment huhuhu, no money income 'youknoun'") #agr com vc jean
            city.city
            
        if market == 3:
            city.city()
        
    def fountain():
        print("All your wounds are healed!")
        player.health = player.vitality
        city.city()
        
    def sorcerer():
        print("I sense a soul in search of answers...")
        print("1 - Redeem your Experience (level up)")
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
            
    def kid():
        print("hey youre back")
        
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
            else:
                sys.exit("The hell´s awating")
                
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
            print("All done pal, gimme money for being incomplete", '\n')
        else:
            print("Sorry pal, go get some gold from the goblins kidneys", '\n')
        blacks_inventory()
    if x == "2":
        if player.money >= 150:
            player.money -= 150
            bs_money += 150
            print("All done pal, gimme money for being incomplete")
        else:
            print("Sorry pal, go get some gold from the goblins kidneys")
        blacks_inventory()
    if x == "3":
        print("Are you sure kid?")
        print('"He did not wait for you to think about it and the programmers already removed all your money...')
        print('Sorry if you would reconsider, at least he is happy')
        bs_money += player.money
        player.money = 0
        print("All done pal, gimme money for being incomplete")
        blacks_inventory()
    if x == '4':
        city.blacksmith()
        
def market_inventory():   
    mk_money = ran.randint(400,3000)
    print('convinience store money' , mk_money)
    print('currency:' , player.money, "Erens")
    print('no momento o jean não fez coisas uteis aki, mas voce pode gastar seu dineiro a vontade :)')
    print('\n' '-What brings you to my little settlement!? huhuhuhu ',"\n", '\n','1 - spend 50 ','\n','2 - spend 150' , '\n', '3 - spend all', '\n' ,'4 - go back' )
    x = input("how much you can waste now?")
    if x == "1":
        if player.money >= 50:
            player.money -= 50
            mk_money += 50
            print("huhuhu thanks 'mahfrien'", '\n')
        else:
            print("WHAT?!, YOU DO NOT HAVE 'MONIIII'...", '\n' , "GET OUT! NOW!!!")
        market_inventory()
    if x == "2":
        if player.money >= 150:
            player.money -= 150
            mk_money += 150
            print("huhuhu thanks 'mahfrien'", '\n')
        else:
            print("WHAT?!, YOU DO NOT HAVE 'MONIIII'...", '\n' , "GET OUT! NOW!!!")
        market_inventory()
    if x == "3":
        print("Are you sure kid?")
        print('He did not wait for you to think about it and the programmers already removed all your money...')
        print('Sorry if you would reconsider, at least he is happy')
        mk_money += player.money
        player.money = 0
        print("All done pal, gimme money for being incomplete")
        market_inventory()
    if x == '4':
        city.market()
        
#aqui é nada mesmo ta certo
#-------------------------------------------------------------------------------------------------------- fim classes
#funções de combate 
def cenario(cenario, inimigo):
    print('You are in a', cenarios[cenario], ', here you found an aggressive', floor[inimigo].name, 'get ready to fight')
    return inimigo
        
def batalha():
    enemy = cenario(ran.randint(0,3), ran.randint(0, len(floor)))
    print('------------Batalha-------------')
    fighter = floor[enemy]
    a = ran.randint(0,2)
    tupla = [0,0]
    
    if a == 0:
        while (float(fighter.health) > 0):
            if player.health <= 0:
                gameover()
            tupla = AI(fighter, tupla[1])
            if tupla[1] == 1:
                print("It protects itself against you!")
            else:
                player.health = round(tupla[0])
                print('It attacks you!')
            print()
            print("Health:", player.health)
            print("Enemy health", round(fighter.health))
            print("Your stamina", player.stamina)
            tupla[1] = choose(player,fighter, (tupla[1]))
            print("Health:", player.health)
            print("Enemy health", round(fighter.health))
            print("Your stamina", player.stamina)
            if player.health <= 0:
                gameover()
            player.stamina += endurance/15
            fighter.stamina += endurance/15
            
        player.money += fighter.money
        player.exppoints += ran.randint(20,30)
        inventory.addinventory(fighter.weapon, 1)
        
    if a == 1:
        while (float(fighter.health) > 0):
            tupla[1] = choose(player,fighter, (tupla[1]))
            print("Health:", player.health)
            print("Enemy health", round(fighter.health))
            print("Your stamina", player.stamina)
            if player.health <= 0:
                gameover()
            tupla = AI(fighter, tupla[1])
            if int(tupla[1]) == 1:
                print("It protects itself against you!")
            else:
                player.health = round(tupla[0])
            print()
            print("Health:", player.health)
            print("Enemy health", round(fighter.health))
            print("Your stamina", player.stamina)
            if player.health <= 0:
                gameover()
            player.stamina += endurance/15
            fighter.stamina += endurance/15

        player.money += fighter.money
        player.exppoints += ran.randint(20,30)
        inventory.addinventory(fighter.weapon, 1)
        
def choose(player, fighter, defend):
    print("What will you do? ")
    print("1 = Attack")
    print("2 = Defend")
    print("3 = Recover")
    choose = Intinput("choose: ", 1,4)
    if choose == 1 and player.stamina > (equipped.weapon).weight:
        return attack(player, fighter, defend, equipped.weapon, classe)
    if choose == 1 and player.stamina > (equipped.weapon).weight:
        print("Not enought stamina, i must recover")
        return 0
    if choose == 2:
        player.stamina -= (equipped.weapon).weight
        return 1
    else:
        return 0
    
def attack(player, fighter, defend, weapon, classe):
    player.stamina -= (equipped.weapon).weight
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
    if fighter.stamina < (fighter.stamina*0.10):
        return[player.health, 0]
        print("it recovered")
    else:
        AI = ran.randint(0,10)
        if AI <= 7:
            print("it atacks you")
            fighter.stamina -= (fighter.weapon).weight
            fighterdamage = fighter.weapon.damage
            yourresistence = (player.damage_percent_taken())
            if defense == 0:
                player.health -= (1-yourresistence)*fighterdamage
                return [player.health, 0]
            else:
                player.health -= ((1-yourresistence)*fighterdamage)/2
                return [player.health, 0]
        else: 
            fighter.stamina -= (fighter.weapon).weight
            return [player.health, 1]
        
    
def Intinput(text, ini, end):
    Test = input(text)
    listoftest = []
    for i in range(ini,end):
        listoftestappend = str(i)
        listoftest.append(listoftestappend)
    while not Test in listoftest:
        print("Not a valid option")
        Test = input("Try again, because you are too good to read the text above right??? ")
    return int(Test)
    
    
def gameover():
    print("You died, your Honor is forever lost")
    print("Sorry kid, but you shoudn't have done that")
    print("Try again?   1-yes    2-no")
    go = Intinput("--->",1,3)
    if go == 1:
        sys.os.execl(sys.executable, sys.executable, *sys.argv)
    if go == 2:
        sys.exit("Only the weak give up")
    
    #----------------------
   
#funções iniciais    
def random_weapon(weapon):
    return (weapon[ran.randint(0,3)])
  
#cria as listas de itns do jogo (TUDO STRING)
cenarios = ["swamp", "forest", "plain", "mountain"]
classes = ["Marksman", "Knight", "Warrior"]
           
#cria armas ( name, damage, weight, Type, Range, value, durability, used, quality, stackable)
MS0100 = itens("Iron Ingot", 1, "Ingot", 5, 10)
MS0101 = itens("Silver Ingot", 1, "Ingot", 30, 10)
MS0102 = itens("Steel Ingot", 1, "Ingot", 10, 10)
MS0103 = itens("Gold Ingot", 1, "Ingot", 50, 10)
MS0104 = itens("Cloran Ingot", 1, "Ingot", 20, 10)
MS0105 = itens("Paldia Ingot", 1, "Ingot", 25, 10)
MS0106 = itens("Miliandric Ingot", 1, "Ingot", 40, 10)
MS0107 = itens("Titanium", 1, "Ingot", 30, 10)
MS0108 = itens("Crystal", 1, "Ingot", 25, 10)
MS0109 = itens("Dranium", 1, "Ingot", 50, 10)
MS0110 = itens("Nightmere", 1, "Ingot", 150, 10)

WE0300 = weapons("Iron Battleaxe", 16, 20, 55, MS0100, "Iron", 400, ran.randint(100,500), 1)
WE0100 = weapons("Hunting Bow", 7, 7, 50, MS0100, "Iron", 250, ran.randint(100,500), 1) #0.937
WE0200 = weapons("Iron Dagger", 4, 2, 10, MS0100, "Iron", 70, ran.randint(100,500), 1)
WE0301 = weapons("Iron Greatsword", 15, 16, 50, MS0100, "Iron", 300, ran.randint(100,500), 1)
WE0201 = weapons("Iron Mace", 9, 13, 35, MS0100, "Iron", 300, ran.randint(100,500), 1)
WE0202 = weapons("Iron Sword", 7, 9, 25, MS0100, "Iron", 150, ran.randint(100,500), 1)
WE0203 = weapons("Iron War Axe", 8, 11, 30, MS0100, "Iron", 300, ran.randint(100,500), 1)
WE0302 = weapons("Iron Warhammer", 18, 24, 60, MS0100, "Iron", 400, ran.randint(100,500), 1)
WE0211 = weapons("Paladin Sword", 10, 12, 135, MS0105, "Paladin", 350, ran.randint(100,500), 1)
WE0212 = weapons("Paladin War Axe", 11, 14, 165, MS0105, "Paladin", 400, ran.randint(100,500), 1)
WE0313 = weapons("Paladin Warhammer", 22, 27, 325, MS0105, "Paladin", 600, ran.randint(100,500), 1)

WE0303 = weapons("Silver Greatsword", 17, 12, 160, MS0101, "Silver", 300, ran.randint(100,500), 1)
WE0204 = weapons("Silver Sword", 8, 7, 100, MS0101, "Silver", 150, ran.randint(100,500), 1)

WE0304 = weapons("Steel Battleaxe", 18, 21, 100, MS0102, "Steel", 400, ran.randint(100,500), 1)
WE0101 = weapons("Steel Bow", 7, 7, 50, MS0102, "Steel", 250, ran.randint(100,500), 1) #0.937
WE0205 = weapons("Steel Dagger", 5, 2.5, 18, MS0102, "Steel", 90, ran.randint(100,500), 1)
WE0305 = weapons("Steel Greatsword", 17, 17, 90, MS0102, "Steel", 300, ran.randint(100,500), 1)
WE0201 = weapons("Steel Mace", 10, 14, 65, MS0102, "Steel", 350, ran.randint(100,500), 1)
WE0202 = weapons("Steel Sword", 8, 10, 45, MS0102, "Steel", 200, ran.randint(100,500), 1)
WE0203 = weapons("Steel War Axe", 9, 12, 55, MS0102, "Steel", 350, ran.randint(100,500), 1)
WE0306 = weapons("Steel Warhammer", 20, 25, 110, MS0102, "Steel", 450, ran.randint(100,500), 1)

WE0307 = weapons("Elder Greatsword", 17, 18, 35, MS0102, "Steel", 260, ran.randint(100,500), 1)
WE0204 = weapons("Elder War Axe", 9, 14, 15, MS0102, "Steel", 260, ran.randint(100,500), 1)

WE0308 = weapons("Clöran Battleaxe", 19, 25, 165, MS0104, "Clöran", 500, ran.randint(100,500), 1)
WE0102 = weapons("Clöran Bow", 10, 9, 150, MS0104, "Clöran", 250, ran.randint(50,250), 1) #0.812
WE0205 = weapons("Clöran Dagger", 6, 3, 30, MS0104, "Clöran", 200, ran.randint(100,500), 1)
WE0309 = weapons("Clöran Greatsword", 18, 18, 75, MS0104, "Clöran", 400, ran.randint(100,500), 1)
WE0206 = weapons("Clöran Mace", 11, 15, 105, MS0104, "Clöran", 350, ran.randint(100,500), 1)
WE0207 = weapons("Clöran Sword", 9, 11, 75, MS0104, "Clöran", 250, ran.randint(100,500), 1)
WE0208 = weapons("Clöran War Axe", 10, 13, 90, MS0104, "Clöran", 300, ran.randint(100,500), 1)
WE0310 = weapons("Clöran Warhammer", 21, 26, 180, MS0104, "Clöran", 300, ran.randint(100,500), 1)

WE0311 = weapons("Paladin Battleaxe", 20, 23, 300, MS0105, "Paladin", 600, ran.randint(100,500), 1)
WE0103 = weapons("Paladin Bow", 12, 10, 270, MS0105, "Paladin", 250, ran.randint(100,500), 1) #0.752
WE0104 = weapons("Paladin Crossbow", 22, 20, 350, MS0105, "Paladin", 400, ran.randint(100,500), 1)
WE0209 = weapons("Paladin Dagger", 7, 3.5, 55, MS0105, "Paladin", 90, ran.randint(100,500), 1)
WE0312 = weapons("Paladin Greatsword", 19, 19, 270, MS0105, "Paladin", 400, ran.randint(100,500), 1)
WE0210 = weapons("Paladin Mace", 12, 16, 190, MS0105, "Paladin", 500, ran.randint(100,500), 1)

WE0314 = weapons("Miliandric Battleaxe", 21, 24, 520, MS0106, "Miliandric", 500, ran.randint(100,500), 1)
WE0105 = weapons("Miliandric Bow", 13, 12, 470, MS0106, "Miliandric", 300, ran.randint(100,500), 1) #0.687
WE0213 = weapons("Miliandric Dagger", 8, 4, 95, MS0106, "Miliandric", 90, ran.randint(100,500), 1)
WE0315 = weapons("Miliandric Greatsword", 20, 20, 470, MS0106, "Miliandric", 400, ran.randint(100,500), 1)
WE0214 = weapons("Miliandric Mace", 13, 17, 330, MS0106, "Miliandric",  400, ran.randint(100,500), 1)
WE0215 = weapons("Miliandric Sword", 11, 13, 235, MS0106, "Miliandric", 250, ran.randint(100,500), 1)
WE0216 = weapons("Miliandric War Axe", 12, 15, 280, MS0106, "Miliandric", 300, ran.randint(100,500), 1)
WE0316 = weapons("Miliandric Warhammer", 23, 28, 565, MS0106, "Miliandric", 450, ran.randint(100,500), 1)

WE0317 = weapons("Titanium Battleaxe", 21, 21, 150, MS0107, "Titanium", 600, ran.randint(100,500), 1)
WE0106 = weapons("Titanium Bow", 13, 11, 270, MS0105, "Titanium", 250, ran.randint(100,500), 1) #0.752
WE0217 = weapons("Titanium Dagger", 8, 2.5, 25, MS0107, "Titanium", 150, ran.randint(100,500), 1)
WE0318 = weapons("Titanium Greatsword", 20, 17, 140, MS0107, "Titanium", 450, ran.randint(100,500), 1)
WE0218 = weapons("Titanium Sword", 11, 10, 70, MS0107, "Titanium", 300, ran.randint(100,500), 1)
WE0219 = weapons("Titanium War Axe", 12, 12, 80, MS0107, "Titanium", 400, ran.randint(100,500), 1)

WE0319 = weapons("Crystalidium Battleaxe", 22, 25, 900, MS0108, "Crystalidium", 150, ran.randint(100,500), 1)
WE0107 = weapons("Crystalidium Bow", 12, 14, 820, MS0108, "Crystalidium", 250, ran.randint(100,500), 1) #0.625
WE0220 = weapons("Crystalidium Dagger", 9, 4.5, 165, MS0108, "Crystalidium", 50, ran.randint(100,500), 1)
WE0320 = weapons("Crystalidium Greatsword", 21, 22, 820, MS0108, "Crystalidium", 125, ran.randint(100,500), 1)
WE0221 = weapons("Crystalidium Mace", 14, 18, 575, MS0108, "Crystalidium", 100, ran.randint(100,500), 1)
WE0222 = weapons("Crystalidium Sword", 12, 14, 410, MS0108, "Crystalidium", 120, ran.randint(100,500), 1)
WE0321 = weapons("Crystalidium Warhammer", 24, 29, 985, MS0108, "Crystalidium", 250, ran.randint(100,500), 1)

WE0322 = weapons("Dranium Battleaxe", 23, 26, 1585, MS0109, "Dranium", 600, ran.randint(100,500), 1)
WE0108 = weapons("Dranium Bow", 17, 16, 1440, MS0109, "Dranium", 400, ran.randint(100,500), 1) #0.562
WE0223 = weapons("Dranium Dagger", 10, 5, 290, MS0109, "Dranium", 300, ran.randint(100,500), 1)
WE0323 = weapons("Dranium Greatsword", 22, 22, 1440, MS0109, "Dranium", 500, ran.randint(100,500), 1)
WE0224 = weapons("Dranium Mace", 16, 19, 1000, MS0109, "Dranium", 450, ran.randint(100,500), 1)
WE0225 = weapons("Dranium Sword", 13, 15, 720, MS0109, "Dranium",350, ran.randint(100,500), 1)
WE0226 = weapons("Dranium War Axe", 15, 17, 865, MS0109, "Dranium", 400, ran.randint(100,500), 1)
WE0324 = weapons("Dranium Warhammer", 25, 30, 1725, MS0109, "Dranium", 600, ran.randint(100,500), 1)

WE0325 = weapons("Night Battleaxe", 25, 27, 2750, MS0110, "Night", 2000, ran.randint(100,500), 1)
WE0109 = weapons("Night Bow", 19, 18, 2500, MS0110, "Night", 1000, ran.randint(100,500), 1) #0.50
WE0227 = weapons("Night Dagger", 11, 6, 500, MS0110, "Night", 500, ran.randint(100,500), 1)
WE0326 = weapons("Night Greatsword", 24, 23, 2500, MS0110, "Night", 1600, ran.randint(100,500), 1)
WE0228 = weapons("Night Mace", 16, 20, 1750, MS0110, "Night", 1200, ran.randint(100,500), 1)
WE0229 = weapons("Night Sword", 14, 16, 1250, MS0110, "Night", 900, ran.randint(100,500), 1)
WE0230 = weapons("Night War Axe", 15, 18, 1500, MS0110, "Night", 800, ran.randint(100,500), 1)
WE0327 = weapons("Night Warhammer", 27, 31, 4000, MS0110, "Night", 2500, ran.randint(100,500), 1)

WE0110 = weapons("Crossbow", 15, 14, 120, MS0101, "Steel",  200, ran.randint(100,500), 1) #0.40
WE0111 = weapons("Enhanced Crossbow", 19, 15, 200,   MS0101, "Steel", 600, ran.randint(100,500), 1) #0.40

WE0328 = weapons("Headsman's Axe", 17, 11, 15, "none", -1, 400, ran.randint(100,500), 1)
WE0231 = weapons("RustyMace", 7, 13, 5, "none", "none", 100, ran.randint(100,500), 1)
WE0232 = weapons("Scimitar", 11, 10, 5,  MS0101, "Steel", 300, ran.randint(100,500), 1)

WE0233 = weapons("Shiv", 5, 2, 10, "none", "none", 10, ran.randint(0,10), 1)
WE0234 = weapons("Fork", 1, 0.5, 5, "none", -1, -1, "none", 1)
WE0235 = weapons("Knife", 2, 0.5, 1, "none", -1, -1, "none", 1)

WE0236 = weapons("Pickaxe", 5, 10, 5,  MS0102, "Steel", 400, ran.randint(100,500), 1)
WE0237 = weapons("Elder Pickaxe", 5, 10, 500,  MS0102, "Steel", 100, ran.randint(100,500), 1)

#cria roupas iniciais do player name, defense, weight, value, material, Type, durability, used, stackable
head_naked = armor("head_naked", 0, 0, 0, "none", "Skin", -1, -1, 1)
chothshirt =  armor("chothshirt", 0, 0, 0, "none", "Cloth", -1, -1, 1)
feet_naked =  armor("feet_naked", 0, 0, 0, "none", "Cloth", -1, -1, 1)
hand_naked =  armor("hand_naked", 0, 0, 0, "none", "Skin", -1, -1, 1)

AR1100 = armor("Iron Armor", 25, 30, 125, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1200 = armor("Iron Boots", 10, 6, 25, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1300 = armor("Iron Gauntlets", 11, 5, 25, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1400 = armor("Iron Helmet", 15, 5, 60, MS0100, " Iron ", 2000, ran.randint(100,500), 1)

AR1101 = armor("Elder Armor", 25, 28, 125, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1201 = armor("Elder Boots", 10, 5, 25, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1301 = armor("Elder Gauntlets", 10, 4, 25, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1401 = armor("Elder Helmet", 15, 4, 60, MS0100, "Iron", 2000, ran.randint(100,500), 1)

AR1102 = armor("Miliandric Light Armor", 26, 4, 125, MS0106, "Miliandric", 2000, ran.randint(100,500), 1)
AR1202 = armor("Miliandric Light Boots", 8, 1, 23, MS0106, "Miliandric", 2000, ran.randint(100,500), 1)
AR1302 = armor("Miliandric Light Gauntlets", 8, 1, 25, MS0106, "Miliandric", 2000, ran.randint(100,500), 1)
AR1402 = armor("Miliandric Light Helmet", 14, 1, 60, MS0106, "Miliandric", 2000, ran.randint(100,500), 1)

AR1103 = armor("City Guard Armor", 27, 8, 35, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1203 = armor("City Guard Officer Boots", 7, 2, 7, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1303 = armor("City Guard Officer Helmet", 12, 2, 12, MS0100, "Iron", 2000, ran.randint(100,500), 1)
AR1403 = armor("City Guard Officer Gauntlets", 7, 1, 7, MS0100, "Iron", 2000, ran.randint(100,500), 1)

AR1104 = armor("Miliandric Armor", 29, 4, 225, MS0106, "Miliandric", 2000, ran.randint(100,500), 1)
AR1204 = armor("Miliandric Boots", 9, 1, 45, MS0106, "Miliandric", 2000, ran.randint(100,500), 1)
AR1304 = armor("Miliandric Gauntlets", 9, 1, 45, MS0106, "Miliandric", 2000, ran.randint(100,500), 1)
AR1404 = armor("Miliandric Helmet", 14, 1, 110, MS0106, "Miliandric", 2000, ran.randint(100,500), 1)

AR1105 = armor("Steel Armor", 31, 35, 275, MS0102, "Steel", 2000, ran.randint(100,500), 1)
AR1205 = armor("Steel Helmet", 17, 5, 125, MS0102, "Steel", 2000, ran.randint(100,500), 1)
AR1305 = armor("Steel Horned Helmet", 17, 5, 125, MS0102, "Steel,", 2000, ran.randint(100,500), 1)
AR1405 = armor("Steel Nordic Gauntlets", 12, 4, 55, MS0102, "Steel", 2000, ran.randint(100,500), 1)

AR1106 = armor("Paladia Armor", 34, 45, 400, MS0105, "Paladia", 2000, ran.randint(100,500), 1)
AR1206 = armor("Paladia Boots", 13, 10, 85, MS0105, "Paladia", 2000, ran.randint(100,500), 1)
AR1306 = armor("Paladia Gauntlets", 13, 8, 85, MS0105, "Paladia", 2000, ran.randint(100,500), 1)
AR1406 = armor("Paladia Helmet", 18, 12, 200, MS0105, "Paladia", 2000, ran.randint(100,500), 1)

AR1107 = armor("Crystalidium Armor", 38, 7, 900, MS0108, "Crystalidium", 2000, ran.randint(100,500), 1)
AR1207 = armor("Crystalidium Boots", 11, 2, 190, MS0108, "Crystalidium", 2000, ran.randint(100,500), 1)
AR1307 = armor("Crystalidium Gauntlets", 11, 2, 190, MS0108, "Crystalidium", 2000, ran.randint(100,500), 1)
AR1407 = armor("Crystalidium Helmet", 16, 2, 450, MS0108, "Crystalidium", 2000, ran.randint(100,500), 1)

AR1108 = armor("Clöran Armor", 40, 35, 1000, MS0104, "Clöran", 2000, ran.randint(100,500), 1)
AR1208 = armor("Clöran Boots", 15, 7, 200, MS0104, "Clöran", 2000, ran.randint(100,500), 1)
AR1308 = armor("Clöran Gauntlets", 15, 7, 200, MS0104, "Clöran", 2000, ran.randint(100,500), 1)
AR1409 = armor("Clöran Helmet", 20, 8, 500, MS0104, "Clöran", 2000, ran.randint(100,500), 1)

AR1110 = armor("Steel Plate Armor", 40, 38, 625, MS0102,"Steel", 2000, ran.randint(100,500), 1)
AR1210 = armor("Steel Plate Boots", 14, 9, 125, MS0102, "Steel", 2000, ran.randint(100,500), 1)
AR1310 = armor("Steel Plate Gauntlets", 14, 6, 125, MS0102, "Steel", 2000, ran.randint(100,500), 1)
AR1410 = armor("Steel Plate Helmet", 19, 6, 300, MS0102, "Steel", 2000, ran.randint(100,500), 1)

AR1111 = armor("Dranium Armor", 43, 38, 1500, MS0109, "Dranium", 2000, ran.randint(100,500), 1)
AR1211 = armor("Dranium Boots", 16, 7, 275, MS0109, "Dranium", 2000, ran.randint(100,500), 1)
AR1311 = armor("Dranium Gauntlets", 16, 7, 225, MS0109, "Dranium", 2000, ran.randint(100,500), 1)
AR1411 = armor("Dranium Helmet", 21, 10, 750, MS0109, "Dranium", 2000, ran.randint(100,500), 1)

AR1112 = armor("Night Armor", 49, 50, 3200, MS0110, "Night", 2000, ran.randint(100,500), 1)
AR1212 = armor("Night Boots", 18, 10, 625, MS0110, "Night", 2000, ran.randint(100,500), 1)
AR1312 = armor("Night Gauntlets", 18, 6, 625, MS0110, "Night", 2000, ran.randint(100,500), 1)
AR1412 = armor("Night Helmet", 23, 15, 1600, MS0110, "Night", 2000, ran.randint(100,500), 1)

#cria criaturas (name, money, vitality, health, endurance, dexterity,  strenght, level, exppoints, weapon, feet, chest, hand, head)
CR0001 = creatures("Deamon Miner", 50, 40, 40, 40, 40, 100, 50, 1, ran.randint(30,50), WE0236, feet_naked, chothshirt, hand_naked, head_naked)
CR0002 = creatures("Rock Carrier", 10, 100, 100, 60, 60, 20, 70, 1, ran.randint(30,50), WE0236, feet_naked, chothshirt, hand_naked, head_naked)
CR0003 = creatures("Mine Leader", 25, 70, 70, 60, 60, 40, 60, 1, ran.randint(30,50), WE0202, feet_naked, chothshirt, hand_naked, head_naked)
CR0004 = creatures("Great Miner", 40, 80, 80, 60, 60, 20, 80, 1, ran.randint(30,50), WE0236, feet_naked, chothshirt, hand_naked, head_naked)

#cria a lista de enemigos do jogo ara cada andar do inferno
firstfloor = [CR0001, CR0002, CR0003, CR0004]

#define que o player está no primeiro andar
floor = firstfloor

#cria itens escenciais player
home = home({})
inventory = inventory({}, 10)
#--------------------------------------------MENU--------------------

#------------------------------------------GAMEPLAY-------------------------------------------------
#first print (decisões iniciais)
print("+----------------+")
print("| Climb of Honor |")
print("+----------------+")
print()
print("You, The Human Army Captain and a Executioner are standing in the edge of a huge wall that surrounds to a very large red whole")
print()
print('Captain - Well, well well, what do we have here?')
print('Captain - So what were you thinking? Breaking a millenary peace treaty')
print()
print("1 Remain silent")
print("2 What do you mean?")
S = Intinput("choose", 1, 3)
print()

if S == 1:
    print("Captain - That was not a retorical question, asshole")
    print("Captain - You commited crimes and now you shall pay")
    print()
    print("1 remain silent")
    print("2 what have i done?")
    S = Intinput("choose", 1, 3)
    if S == 1:
        print("Executioner - I haven't got all day, we must reinforce the wall")
        print("Captain - You are right, enjoy your trip to hell, you bastard")
        print("The Executioner pulls the lever and you start to fall into a hole")
    else:
        print('Captain - Do you even know what you did?, that Kid you "saved", was part of a sacrifice to the demons so we are left in peace...')
        print('Captain - But now, the treat has been broken, we are doomed thanks to you')
        print("Captain - Enjoy your trip to hell, bastard")
        print("The Executioner pulls the lever and you start to fall into the hole")
        
else:
    print('Captain - Do you even know what you did?, that Kid you "saved", was part of a sacrifice to the demons so we are left in peace...')
    print('Captain - But now, the treat has been broken, we are doomed thanks to you')
    print("Executioner - I haven't got all day, we must reinforce the wall Captain")
    print("Captain - You are right, enjoy your trip to hell, bastard")
    print("The Executioner pulls the lever and you start to fall into a hole")

print("It's been a while since started falling, and you can barely see anything")
print("You sudenly hit some cobwebs and slow down, but you keep falling")
print("You are still falling slowly, and you see some wood planks near you, what do you do?")
print()
print("1 Try to grab them")
print("2 dodge them")
S = Intinput("choose", 1, 3)
if S == 1:
    print("You managed to grab them, but they were root and broke, at least you slowed down")
else: 
    print("You dodged them, now you are falling faster")
print("You see another set of planks what do you do?")
print("1 Try to grab them")
print("2 dodge them")
S1 = Intinput("choose", 1, 3)
if S1 == 1 and S == 1:
    print("You managed to grab them, but they were also rooten and broke again, at least you slowed down")
    S2 = 2
elif S1 == 1:
    print("You managed to grab them, but you were too fast and they broke, at least you slowed down")
    S2 = 2
elif S == 1:
    print("You dodged them, now you are falling faster")
    S2 = 2
else: 
    print("You dodged them, now you are falling even faster")
    S2 = 1

print("You fall a couple more meters and see the floor")
if S2 == 2:
    print("Great! You survived the fall, but you passed out")
if S2 == 1:
    print("You were to fast and smashed right into the ground")
    gameover()

print("As you wake up, you feel that something is dragging you through the floor, you can't really describe, but it didn´t notice you are awake")
print("You pass trought a old pickaxe laying in the floor, what do you do?")

print("1 Grab it and attack the thing carrying you")
print("2 Pretend you are dead")
S = Intinput("choose", 1, 3)
if S == 2:
    print("it keeps dragging you")
    print("you see a Kid hidden in a hole offering you a shiv, what do you do?")
    print("1 Grab it and atack the thing carryng you")
    print("2 Still pretend you are dead")
    S = Intinput("choose", 1, 3)
    if S == 1:
        print("It wasnt expecting an attack, you manage to kill it but unfortunately, the creature had nothing usefull")
        inventory.addinventory(WE0233, 1)
        equipped.weapon = WE0233
        print("You go back some steps and thank the Kid")
        print("It asks you to follow him, what do you do?")
    else:
        print("It led you to it's hive where there were many others like it, they ripped you apart and ate your remains")
        gameover()
        
if S == 1:
    print("It wasn't expecting a attack, you managed to kill it but unfortunately, the creature had nothing usefull")
    inventory.addinventory(WE0236, 1)
    equipped.weapon = WE0236
    print("You keep walking ahead with the pickaxe")
    print("After some steps you see a Kid hidden in a hole, and it asks you to come with him, what do you do?")
    
print("1 Follow it")
print("2 Ignore it and keep walking ahead")
S = Intinput("choose", 1, 3)

if S == 2:
    print("You went into a dark big room, in it there were many others creatures like the one that carried you, they ripped you apart and ate your remains")
    gameover()

if S == 1:
    print("Both ou you remain quiet all the way, in the end, he took you to a small vilage into the cave rocks")
    
print("You and the Kid start talking")
nome = input("Kid - So what's your name?")
print("Kid - Thats a weird name, anyway who are you? and how did you got here?")

print("1 I am an Archer, and as for what it seems, i commited a crime in the surface, and was dumped down here")
print("2 I am a Paladin, and as for what it seems, i commited a crime in the surface, and was dumped down here")
print("3 I am a Barbarian, and as for what it seems, i commited a crime in the surface, and was dumped down here")
classe = Intinput("choose, Archers, use ranged weapons, Paladins use light close range weapons and barbarians use heavy close range ones", 0, 3)
if classe == 1:
   vitality = 70
   dexterity = 100
   endurance = 60
   strenght = 40
   tclasse = "Archer"
      
if classe == 2:   
   vitality = 80
   dexterity = 80
   endurance = 60
   strenght = 60
   tclasse = "Paladin"
   
if classe == 3:
   vitality = 100
   dexterity = 40
   endurance = 60
   strenght = 80
   tclasse = "Barbarian"

#inicializa player:
player = player(nome, 0, vitality, vitality, endurance, endurance, dexterity,  strenght, 1, 30)

#equip various armors
equipped.head = head_naked
equipped.chest = chothshirt
equipped.feet = feet_naked
equipped.hand = hand_naked

print("Kid - So you are alive? Long time since I have seen one of your kind")
print("You - What do you mean? Are you dead?")
print("Kid - We all are, you just fell to Hell, didn't you know that?")
print("Kid - We are Damned Souls that escaped the Demons and found this village")
print("Kid - But don't worry, we mean no harm to you, the Demons tought...")
print("Kid - Anyway, you said you are a {0}, but you have no weapon, lets fix that, follow me".format(tclasse))
print("Kid - Here we are, this is Wayland, he is the town blacksmith")
print("Kid - Hey, Wayland we have a newcomer from the surface that need a weapon, can you help?")
print("Metal noises in background")
print("Wayland - Hey kid, sure i can, what does he need?")

if classe == 1:
    print("he is a {0}... so a bow i guess".format(tclasse))
    inventory.addinventory(WE0100, 1)
    equipped.weapon = WE0100
if classe == 2:
    print("he is a {0}... so a sword i guess".format(tclasse))
    inventory.addinventory(WE0202, 1)
    equipped.weapon = WE0202
if classe == 3:
    print("he is a {0}... so a greatsword i guess".format(tclasse))
    inventory.addinventory(WE0301, 1)
    equipped.weapon = WE0301
    
print("Wayland - Sure, here it is... but {0}, can you do me a favor? we are missing some pickaxes in the mines, if you come across any, remeber me ok?".format(tclasse))
print()
print("1 - Sure no problem, thanks for the weapon")
print("2 - Yeah, i guess... no promisses tough")
S = Intinput("choose", 1, 3)

print("Wayland - Ok then, got to go back to work")
print("Kid - So you should get to know the town, after that i will show you some tunels around, wait for me before leaving town ok?")
print("You - Sure")
city.city()
print("Kid - before you leave town i want to show you the training area, we are dead but we must be in form")
print("1 - Ok lets go there")
print("2 - I don´t need training, lets go to the tunnels")
S = Intinput("choose", 1, 3)

if S == 1:
    print("Kid - Here we are, atack that training bot, it wont fight back")
    bot = 25
    while (float(bot) > 0):
            print("You are fighting a straw bot")
            print("health:", player.health)
            print("bot health", round(bot))
            print("Your Stamina", player.stamina)
            print("What will you do? ")
            print("1 = Attack")
            print("2 = Defend")
            print("3 = Recover")
            S = Intinput("choose: ", 1,4)
            if S == 1 and player.stamina > (equipped.weapon).weight:
                bot -= (equipped.weapon).damage
            if S == 1 and player.stamina < (equipped.weapon).weight:
                print("Not enought stamina, i must recover")
            if S == 2:
                player.stamina -= (equipped.weapon).weight
            player.stamina += player.endurance/15
            print("health:", player.health)
            print("bot health", round(bot))
            print("Your Stamina", player.stamina)
    print("Kid, now you are ready to go, follow me")
        
if S == 2:
    print("Kid - If you say so.. Lets go then")
    
print("Kid - This are the Tunnels...")

print("+-----------------+")
print("| To Be Continued |")
print("+-----------------+")
