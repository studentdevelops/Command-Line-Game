import random
from colorama import Fore, Style
from time import sleep
from os import system, name

class person(object):

    def __init__(self, name, hp, atk, mp, item, magic):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.item = item
        self.magic = magic
        self.actions = ["ATTACK", "MAGIC", "ITEMS"]

    # function to generate damage(dmg)
    def gen_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    # function to update health after getting hit by dmg
    def up_hp(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0

    # function to get current hp
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    # function to get the name of the spell choosed from dictonary
    """def get_spell_name(self,i):
        return self.magic[i] ["name"]"""

    # function to get spell dmg
    """def gen_spell_dmg(self,i):
        mdmgl = self.magic[i] ["dmg"] - 5
        mdmgh = self.magic[i] ["dmg"] + 10
        return random.randrange(mdmgl, mdmgh)"""

    # function to get magic points of spell
    """def get_spell_mp(self,i):
        return self.magic[i] ["mpcost"]"""

    # function to get heal points to HP
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    # function to get heal points to MP
    def mp_heal(self, dmg):
        self.mp += dmg
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    # function to update mp of players
    def up_mp(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0
        return self.mp

    # gets current mp of player
    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    # function to print the actions available
    def choose_Action(self):
        print(Fore.MAGENTA + "Select Your Action:" + Fore.RESET)
        i = 1
        for items in self.actions:
            print("     " + str(i)+". ", items)
            i += 1

    # function to print all the magic available
    def choose_magic(self):
        print(Fore.MAGENTA +  "     " + "\n" + "Select Your Magic Spell:" + Fore.RESET)
        i = 1
        for spell in self.magic:
            print("     " + str(i)+". ", spell.name, "( mp", spell.cost, ")")
            i += 1

    # function to print all the items available
    def choose_items(self):
        print(Fore.MAGENTA + "     " + "\n" + "Select a Item:" + Fore.RESET)
        i = 1
        for item in self.item:
            print("     " + str(i)+". ", item.name, "x" + str(item.quentity))
            i += 1

    # Status of Player
    def player_stats(self):
        print(Style.BRIGHT + Fore.RED + "==============================" +
              Fore.RESET + Style.RESET_ALL)
        print(Style.BRIGHT + "HP                                          MP" + Style.RESET_ALL)
        print("           __________________________                ___________")
        dishp = str(self.hp) + "/" + str(self.maxhp)
        dismp = str(self.mp) + "/" + str(self.maxmp)
        # mainting equal space even after chnage in number of digits of HP
        while len(dishp) < 7:
            dishp = dishp + " "
        
        # mainting equal space even after chnage in number of digits of MP
        while len(dismp) < 7:
            dismp = dismp + " "
        hp = ""
        mp = ""
        cur_hp = (self.hp/self.maxhp) * 100 / 4
        cur_mp = (self.mp/self.maxmp) * 100 / 10

        # dynamic HP bar
        while cur_hp > 0:
            hp += "█"
            cur_hp -= 1

        # dynamic MP bar
        while cur_mp > 0:
            mp += "█"
            cur_mp -= 1

        # trying to minatain spacing even after reducing health
        while len(hp) < 25:
            hp += " "

        # trying to minatain spacing even after reducing MP
        while len(mp) < 10:
            mp += " "
            
        print(Fore.YELLOW + str(dishp) +
              Fore.RESET + ": " + " |" + Fore.GREEN + hp + Fore.RESET + "|" + "      " + 
              Fore.YELLOW + str(dismp) + Fore.RESET +  ": |" + Fore.BLUE + mp + Fore.RESET + "|" )

    # Status of Enemy cuz i need different colors for enemy and player

    def enemy_stats(self):
        print(Style.BRIGHT +  "HP" + Style.RESET_ALL)
        print("          ___________________________________________________")
        hp = ""
        cur_hp = (self.hp/self.maxhp) * 100 / 2
        dishp = str(self.hp) + "/" + str(self.maxhp)
        while len(dishp) < 7:
            dishp = dishp + " "

        # dynamic HP bar
        while cur_hp > 0:
            hp += "█"
            cur_hp -= 1

        # trying to minatain spacing even after reducing health
        while len(hp) < 50:
            hp += " "

        print(Fore.YELLOW + str(dishp) +
              Fore.RESET + ": " + "|" + Fore.RED + hp + Fore.RESET + " |")
        print(Style.BRIGHT + Fore.RED + "==============================" +
              Fore.RESET + Style.RESET_ALL)
    
    # transition of enemy
    def transition(self,i):
        about_enemy_lumos = "is a Supreme MAGE, A very powerfull sorcerer"
        about_enemy_Alipsh = "is a demon warrior, A extreme strengthened demon"
        about = [about_enemy_lumos, about_enemy_Alipsh]
        sleep(1.2)
        print("." , end='')
        sleep(1.2)
        print("." , end='')
        sleep(1.2)
        print(".")
        sleep(1)
        input("wait what?\n")
        print(Style.BRIGHT + Fore.RED + "            " + f"Enemy Backup has arrived {self.name}" + Style.RESET_ALL + Fore.RESET)
        sleep(1.5)
        print("            " + f"{self.name} " + Style.BRIGHT + Fore.RED + about[i] + Style.RESET_ALL + Fore.RESET)
        sleep(1.5)
        print(Style.BRIGHT + Fore.RED + "            " + "the fight continued...\n" + Style.RESET_ALL + Fore.RESET)
        sleep(2)

    # Starting Game scene
    def start_scene(self):
      print(Fore.BLUE + Style.BRIGHT + " " * 10 + "_" * 50 + "\n" +
      Style.RESET_ALL + Fore.RESET)
      print("            " + self.name + " was called to the kingdom of dwarfs to ")
      sleep(2)
      print("            " + "for traning the troops for the upcoming war")
      sleep(2)
      print("            " + "But while travelling towards the kingdom he ")
      sleep(2)
      print("            " + "was attacked by the demons who knew ")
      sleep(2)
      print("            " +"he was coming to help dwarfs fight the war")
      sleep(2)
      print("            " + "they jumped on him and the fight was on ", end="")
      sleep(1.8)
      print(".", end="")
      sleep(1.8)
      print(".", end="")
      sleep(1.8)
      print(".")
      print(Fore.BLUE + Style.BRIGHT + " " * 10 + "_" * 50 + "\n" +
      Style.RESET_ALL + Fore.RESET)
      sleep(2)
