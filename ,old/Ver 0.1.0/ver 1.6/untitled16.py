# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:08:34 2016

@author: edufe
"""
import numpy.random as ran

class quests:
    
    
    def __init___(self, NPC1, Giver, battles, reward):
        self.NPC1 = NPC1
        self.Giver = Giver
        self.battles = battles
        self.reward = reward
    
    def pick_random_name(listnomes, listnomes1):
        a = ran.randint(0,100)
        if a < 50:
            return listnomes(ran.randint(len(listnomes)))
        if a > 50:
            return listnomes(ran.randint(len(listnomes)))
        if a == 50:
            return "Taylor"
    
    def pick_random_NPC(Blacksmith, MarketMan, listnomes, listnomes1):
        a = ran.randint(0,3)
        if a == 1:
            return Blacksmith
        if a == 2:
            return MarketMan
        if a == 3:
            return quests.pick_random_name(listnomes, listnomes1)
            
    def generate_random_quest(Blacksmith, MarketMan, listnomes, listnomes1):
        name = quests.pick_random_name(listnomes, listnomes1)
        Giver = quests.pick_random_NPC(Blacksmith, MarketMan, listnomes, listnomes1)
        battles = ran.randint(1,4)
        reward = ((ran.randint(40,100))*battles)
        return quests(name, Giver, battles, reward)
        
    
listnomes = ['Jack', 'Lewis', 'James', 'Logan', 'Daniel', 'Ryan', 'Aaron', 'Oliver', 'Liam', 'Jamie', 'Ethan', 'Alexander', 'Cameron', 'Harrison', 'Kyle', 'Adam', 'Harry', 'Matthew', 'Callum', 'Lucas', 'Nathan', 'Aiden', 'Dylan', 'Charlie', 'Connor', 'Thomas', 'Alfie', 'Joshua', 'William', 'Jayden', 'Andrew', 'Kai', 'Max', 'Ben', 'Samuel', 'Luke', 'Tyler', 'Rory', 'David', 'Michael', 'Riley', 'Noah', 'Cole', 'Joseph', 'John', 'Archie', 'Jacob', 'Fraser', 'Rhys', 'Ross', 'Calum', 'Jay', 'Josh', 'Euan', 'Mason', 'Owen', 'Sam', 'Leo', 'Robert', 'Scott', 'Leon', 'Robbie', 'Benjamin', 'Caleb', 'Oscar', 'Harris', 'Murray', 'Sean', 'Christopher', 'Kieran', 'Aidan', 'Jake', 'Evan', 'Kayden', 'Alistair', 'Elliot']
listnomes1 = ['Arran', 'Angus', 'Brodie', 'Ewan', 'Muhammad', 'Alex', 'Declan', 'Finn', 'Blair', 'Ollie', 'Reece', 'Corey', 'Kian', 'Finlay', 'Kaiden', 'Kenzie', 'Cody', 'Craig', 'Mohammed', 'Calvin', 'Mark', 'Jude', 'Luca', 'Ciaran', 'George', 'Zak', 'Zac', 'Charles', 'Gregor', 'Hamish', 'Isaac', 'Harvey', 'Shay', 'Struan', 'Lee', 'Steven', 'Joe', 'Lennon', 'Patrick', 'Jason', 'Louis', 'Olly', 'Bailey', 'Marcus', 'Peter', 'Sebastian', 'Gabriel', 'Jackson', 'Zack', 'Ashton', 'Brandon', 'Reuben', 'Theo', 'Paul', 'Conor', 'Hayden', 'Lachlan', 'Ruaridh', 'Innes', 'Stuart', 'Jordan', 'Sonny', 'Alan', 'Blake', 'Zachary', 'Cooper', 'Ellis', 'Caiden', 'Fergus', 'Jakub', 'Zach', 'Findlay']
SpecialNPC = 'Taylor'

Blacksmith = "Charles"
MarketMan = "Godless"

quest = quests.generate_random_quest(Blacksmith, MarketMan, listnomes, listnomes1)


