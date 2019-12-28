import numpy.random as ran

class character:
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
        
class inventory:
    
    I = {}
    
    def __init__(self, maxitens):
        self.maxitens = maxitens
    
    def show_inventory():
        print(I)
        
    def addinventory():
        
        
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
    
#def defend(defender, atacker):           


#----------------------------------------------------------------------------------------------------------------------
def escolha_classe():
    print('classes')
    print('1 = Marksman, You will handle ranged weapons extremely well')
    print('2 = Knight, You will handle light weapons extremely well')
    print('3 = Warrior, You will handle heavy weapons extremely well')

    return(int(input('Your choice: ')))

 
    return(int(input('sua escolha')))
    
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
        
def random_weapon():
    return (weapons[ran.randint(0,3)])
    
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

#cria criaturas
goblin = character("goblin", ran.randint(30,50), ran.randint(20,40), 1000, 10, random_weapon())
minotaur = character("minotaur", ran.randint(30,50), ran.randint(20,40), 1000, 1, random_weapon())
centaur = character("centaur", ran.randint(30,50), ran.randint(20,40),1000, 1, random_weapon())
orc = character("orc", ran.randint(30,50), ran.randint(20,40),1000, 2, random_weapon())

#cria a lista de enemigos do jogo
enemies = [goblin, minotaur, centaur, orc]

#------------------------------------------GAMEPLAY-------------------------------------------------
#first print
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
   
player = player(nome, health, 0, stamina, miss_chance, weapon1, knightlevel, warriorlevel, marksmanlevel)

print("what a coincidence, you just said you want to become a", classes[classe-1], "and a", weapon1.name, 'fell from the sky to your hands!')
print("weird, anyway let’s go to the city")

#-----tutorial:
print('oh no, it seems you stumbled upon an enemy')
batalha()
