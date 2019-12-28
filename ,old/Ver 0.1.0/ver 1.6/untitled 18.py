# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:09:47 2016

@author: edufe
"""

class itens:
    def __init__(self, name, weight, Type, value, durability, quality):
         self.name = name
         self.weight = weight
         self.Type = Type
         self.value = value
         self.durability = durability
         self.quality = quality
        
class armor(itens):
    def __init__(self, name, damage, weight, Type, Range,  defense, enchantment, quality):
        armor.__init__(self, name, damage, weight, Type, Range, quality)
        self.defense = defense
        self.enchantment = enchantment

class weapons(itens):
    def __init__(self, name, damage, weight, Type, Range):
        weapons.__init__(damage, Range)
        self.damage = damage
        self.Range = Range
        

        