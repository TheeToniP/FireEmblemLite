#Description: Character Class
import random 

class Character: 
    def __init__(self,name,weapon): 
        self.name = name 
        self.weapon = weapon
        #self.inventory = [] 

    def get_name(self): 
        return self.name

    def get_weapon(self): 
        return self.weapon

    #Each function happens to charcters, hence their placement in the character class
    '''def create_characters(self):
        #Characters
        Malik = Character("Malik", "Sword")
        Lucina = Character ("Lucina", "Sword")
        Vaike = Character("Vaike", "Axe")
        Bob = Character("Bob","Axe")
        Tera = Character("Tera", "Lance")
        Sumia = Character("Sumia", "Lance")
        character_list = [Malik, Lucina,Vaike,Bob,Tera,Sumia]
        return character_list'''
    
    #We use self b/c the object is referring to itself 
    def start_battle(self):
        character_list = self.create_characters()
        #Set teams later! 
        #COPIED AND PASTED!!! characters_chosen = random.choices(character_list, k=2)
        pass 
        #return characters_chosen #just an experiment 

def main():
    Malik = Character("Malik", "Sword")
    Lucina = Character ("Lucina", "Sword")
    Vaike = Character("Vaike", "Axe")
    Bob = Character("Bob","Axe")
    Tera = Character("Tera", "Lance")
    Sumia = Character("Sumia", "Lance")

    #saying hi :) 
    print("WELCOME TO FIRE EMBLEM LITE *IMAGINE SOUND EFFECTS*")
    character_list = [Malik, Lucina,Vaike,Bob,Tera,Sumia]
    char_1, char_2  = random.choices(character_list, k=2)
    while char_1 == char_2:
        char_1, char_2  = random.choices(character_list, k=2)
    print("characters chosen: {} & {}".format(char_1.get_name(), char_2.get_name()))

if __name__ == "__main__":
    main()


'''
Old random Player Selection

def players():
    "selects a character at random"
    characters = ["Malik","Bob","Tera"]
    rand1 = random.randint(0,2) 
    rand2 = random.randint(0,2)
   
    #note: A person can't fight themselves 
    if rand1 != rand2:
        player1 = characters[rand1]
        player2 = characters[rand2]
    else: 
        rand1 = random.randint(0,2) 
        rand2 = random.randint(0,2)
        player1 = characters[rand1]
        player2 = characters[rand2]

    return player1, player2  
'''