import random
fastlist = ["In-N-Out", "McDonald's", "Wingstop", "Domino's"]
ininoutmenu = ["Double Double", "Animal Style Fries", "Milkshake"]
mcdonaldsmenu = ["Quarter Pounder", "Fries", "Mcnuggets"]
wingstopmenu = ["Chicken tenders", "Loaded fries", "Barbeque wings"]
dominosmenu = ["Pepperoni Pizza", "Breadsticks", "Alfredo Pasta"]

print(fastlist)
pick = input("Pick a resturaunt to dine at: ")
if pick == "In-N-Out":
    print(ininoutmenu)
    print(ininoutmenu[random.randrange(0,3)])
elif pick == "McDonald's":
    print(mcdonaldsmenu)
    print(mcdonaldsmenu[random.randrange(0,3)])
elif pick == "Wingstop":
    print(wingstopmenu)
    print(wingstopmenu[random.randrange(0,3)])
elif pick == "Domino's":
    print(dominosmenu)
    print(dominosmenu[random.randrange(0,3)])
    