# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:04:47 2016

@author: Eduardo
"""
import numpy.random as ran

from main import itens, weapons

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
WE0211 = weapons("Paladin Sword", 10, 12, 135, MS0105, "Paladin", 350, ran.randint(100,500), 1)
WE0212 = weapons("Paladin War Axe", 11, 14, 165, MS0105, "Paladin", 400, ran.randint(100,500), 1)
WE0313 = weapons("Paladin Warhammer", 22, 27, 325, MS0105, "Paladin", 600, ran.randint(100,500), 1)

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