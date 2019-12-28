class city: # -------------------------------------------------------------------------------------------------------- cidade
    def __init__(self):
        self.form = []
        
    def city():
        print("in this small town you have a blacksmith, a market and a fountain") 
        #e mais o que vcs quisrem
        main = int(input("what would you like to do?" "\n" "1 go to blacksmith" "\n" "2 go to market" "\n" "3 go to fountain" "\n" "4 go explore" "\n" "5 Save Game" "\n" "6 exit" "\n"))
        if main == 1:
            city.blacksmith()
        if main == 2:
            city.market()
        if main == 3:
            city.fountain()
        if main == 4: 
            batalha()
        if main == 5: 
#socorro        
        if main == 6:
            Exit()

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
        
    def Exit():
        EX = int(input("this game does not save game automatically are u sure you wnat to exit?", "\n", "1 = no", "\n", "2 = maybe"))
        if EX == 1:
            city.city()
        if EX == 2: