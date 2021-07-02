import random 

class Character: 
    #We use self b/c the object is referring to itself
    def __init__(self,name,weapon): 
        self.name = name 
        self.weapon = weapon
        #self.inventory = [] 

    #GETTERS 
    def get_name(self): 
        return self.name

    def get_weapon(self): 
        return self.weapon
    
#Characters
MALIK = Character("Malik", "Sword")
LUCINA = Character ("Lucina", "Sword")
VAIKE= Character("Vaike", "Axe")
BOB = Character("Bob","Axe")
TERA = Character("Tera", "Lance")
SUMIA = Character("Sumia", "Lance")
character_list = [MALIK, LUCINA,VAIKE,BOB,TERA,SUMIA]
     
def character_select():
    char_1, char_2  = random.choices(character_list, k=2)
    while char_1 == char_2:
        char_1, char_2  = random.choices(character_list, k=2)
    print("In this round, {} will fight {}!".format(char_1.get_name(), char_2.get_name()))
    return char_1, char_2

def main():
    #saying hi :) 
    print("WELCOME TO FIRE EMBLEM LITE *IMAGINE SOUND EFFECTS*")

    #character 1 and 2 selected
    char_1, char_2 = character_select()

   # weapon triangle!
    if (char_1.get_weapon() == "Sword") and (char_2.get_weapon() == "Axe"): 
        print (char_1.get_name(), " won!") 
    elif (char_1.get_weapon() =="Axe") and (char_2.get_weapon() == "Lance"): 
        print(char_1.get_name(), " won!")
    elif (char_1.get_weapon() =="Lance") and (char_2.get_weapon() == "Sword"): 
        print(char_1.get_name(), " won!")
    elif (char_2.get_weapon() == "Sword") and (char_1.get_weapon() == "Axe"): 
        print (char_2.get_name(), " won!") 
    elif (char_2.get_weapon() =="Axe") and (char_1.get_weapon() == "Lance"): 
        print(char_2.get_name(), " won!")
    elif (char_2.get_weapon() =="Lance") and (char_1.get_weapon() == "Sword"): 
        print(char_2.get_name(), " won!")
    else:
        print("No one won...It was a draw...")

    #new problem: what if they have the same weapon! --> It's a draw atm :? (Fix when we add levels and health points)
 


if __name__ == "__main__":
    main()