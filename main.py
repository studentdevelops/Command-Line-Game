from random import randint, randrange

from colorama import Fore, Style, init

from time import sleep

from os import system, name 

from classes.game import person
from classes.magic import spell
from classes.items import items

init(autoreset=True)


# ATTACK SPELLS
thunder = spell("Thunder", 55, 10, "Attack")
quake = spell("EarthQuake", 70, 15, "Attack")
explosion = spell("Explosion", 100, 20, "Attack")
blizzard = spell("Blizzard", 70, 15, "Attack")
firecanon = spell("FireCanon", 120, 25, "Attack")
firespin = spell("FireSpin", 150, 25, "Attack")

# NON ATTACK SPELLS
cure = spell("Cure", 80, 15, "Heal")
supercure = spell("Super-Cure", 180, 30, "Heal")

magic_spells = [thunder, quake, explosion,
                blizzard, firecanon, firespin, cure, supercure]

# Potion Items
potion = items("Potion", "Heals 80 HP", 5, "heal", 80)
super_potion = items("Super Potion", "Heals 180 HP", 3, "heal", 180)
ultra_potion = items("Ultra Potion", "Heals to Max HP", 1, "heal", 999)

# Retore Items
retore = items("Retore", "Retores 80HP and 80MP", 3, "retore", 80)
super_restore = items(
    "Super Retore", "Retores 150HP and 150MP", 2, "retore", 150)
ultra_retore = items(
    "Ultra Retore", "Retores to Max HP and Max MP", 1, "retore", 999)

# Attck Items
bomb = items("Bomb", "Deals 250 Damage to Opponet", 1, "attack", 250)


player_items = [potion, super_potion, ultra_potion,
                retore, super_restore, ultra_retore, bomb]
 
# function to clear the terminal
# for setting up enviroment
def clear():
      # for windows 
      if name == 'nt': 
            _ = system('cls') 

      # for mac and linux(here, os.name is 'posix') 
      else: 
            _ = system('clear') 

print(Fore.GREEN + Style.BRIGHT + "\n                          " + "Welcome to the beta test of the game \n" + Fore.RESET + Style.RESET_ALL)

defeated = 0
name =  Fore.GREEN +  input("Enter Your Name Gamer: ") + Fore.RESET + Style.RESET_ALL
# name = Fore.GREEN + "Apple" + Fore.RESET (default testing name)
player = person(name, 250, 40, 100, player_items, magic_spells)
# starting scene of game
player.start_scene()

# defining enemies
enemy = person(Fore.RED + "Destroyer" + Fore.RESET, 500, 60, 150, [], magic_spells)
enemy2 = person(Fore.RED + "Lumos" + Fore.RESET, 600, 80, 200, [], magic_spells)
enemy3 = person(Fore.RED + "Alipsh" + Fore.RESET, 450, 120, 120, [], magic_spells)
enemies = [enemy2, enemy3]
running = True
while running:
      try:
            player.choose_Action()
            choice = int(input("Enter Your Choice: ")) - 1

            # player choices
            if choice == 0:

                  # player dmg
                  playerdmg = player.gen_dmg()

                  # enemy dmg updating
                  enemy.up_hp(playerdmg)

                  print(Style.BRIGHT + Fore.RED +
                        "==============================" + Fore.RESET + Style.RESET_ALL)
                  print(f"{name} dealth " + Fore.GREEN +
                        str(playerdmg) + Fore.RESET + f" to {enemy.name}")

            elif choice == 1:
                  print(Fore.BLUE + f"You choice to use Magic" +
                        Fore.RESET + Style.RESET_ALL)

                  # calling the function which prints all the avaiable magic
                  player.choose_magic()
                  # adjusting choice according to index of magic in the dictionary since they start with 0
                  choice = int(input("Select Your Spell: ")) - 1
                  if choice <= len(magic_spells) - 1:
                        # current mp of player is transfered to 'currentmp' variable
                        currentmp = player.get_mp()

                        # getting spell out of the [fire, thunder, quake, explosion, blizzard, cure] part of player.magic now
                        spell = player.magic[choice]

                        # taking spell damage from spell
                        spelldmg = spell.spell_dmg()

                        # checks for if cost of magic is more than current player magic points
                        # if yes the msg is displayed and the rest of the code is skipped
                        if spell.cost > currentmp:
                              print(f"You Dont Have enough MP to perform the spell " + Fore.GREEN +
                                    str(player.get_mp()) + "/" + str(player.get_max_mp()) + Fore.RESET)
                              continue

                        # if the cost is less than player's current magic point the
                        # spell is executed on the enemy
                        else:

                              if spell.tpe == "Attack":
                                    spell = player.magic[choice]
                                    # Generating spell dmg
                                    spelldmg = spell.spell_dmg()

                                    enemy.up_hp(spelldmg)

                                    # player mp is updated
                                    player.up_mp(spell.cost)

                                    # stats is displayed
                                    print(Style.BRIGHT + Fore.RED +
                                          "==============================" + Fore.RESET + Style.RESET_ALL)
                                    print(f"{name} used {spell.name} to deal " + Fore.GREEN +
                                          str(spelldmg) + Fore.RESET + Style.RESET_ALL + f" to {enemy.name}")

                              else:
                                    spell = player.magic[choice]
                                    # Generating spell dmg
                                    spelldmg = spell.spell_dmg()

                                    player.heal(spelldmg)

                                    # player mp is updated
                                    player.up_mp(spell.cost)

                                    # stats is displayed
                                    print(Style.BRIGHT + Fore.RED +
                                          "==============================" + Fore.RESET + Style.RESET_ALL)
                                    print(f"{name} used {spell.name} to heal " + Fore.GREEN +
                                          str(spelldmg) + Fore.RESET + Style.RESET_ALL )
                  else:
                        print(Fore.RED + Style.BRIGHT + "invalid input\n" + Fore.RESET + Style.RESET_ALL)
                        continue

            elif choice == 2:
                  player.choose_items()
                  choice = int(input("Select a Item: ")) - 1
                  item = player.item[choice]
                  if item.quentity > 0:
                        item_name = item.name
                        damg = item.dmg
                        if item.tpe == "heal":
                              player.heal(damg)
                              print(f"{name} used {item_name} to heal {damg} HP")
                        elif item.tpe == "retore":
                              player.mp_heal(damg)
                              print(f"{name} used {item_name} to heal {damg} HP and MP")
                        elif item.tpe == "attack":
                              enemy.up_hp(damg)
                              print( f"{name} used {item_name} on {enemy.name} for {damg}")
                        item.quentity -= 1
                  else:
                        print( "     " + Fore.RED + Style.BRIGHT + "\nNo More " + str(item.name) + " left \n" + Fore.RESET + Style.RESET_ALL)
                        continue
            else:
                  print(Fore.RED + Style.BRIGHT + "invalid input\n" + Fore.RESET + Style.RESET_ALL)
                  continue
            
            # enemy tranistions 
            if defeated < 2:
                  if enemy.get_hp() == 0:
                        print(Fore.BLUE + Style.BRIGHT + "_____________________________________________________________" + 
                        Style.RESET_ALL + Fore.RESET)
                        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f"You defeated {enemy.name}\n" + 
                        Style.RESET_ALL + Fore.RESET)
                        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +  "            \nC O N G R A T U L A T I O N S \n" + 
                        Style.RESET_ALL + Fore.RESET)
                        print(Fore.BLUE + Style.BRIGHT + "_____________________________________________________________" + 
                        Style.RESET_ALL + Fore.RESET)
                        enemy = enemies[defeated]
                        enemy.transition(defeated)
                        defeated += 1
                        continue
            
            # checking when the fight is supposed to end via enemy hp
            # that is if the enemy died or not      
            if enemy.get_hp() == 0:
                  print(Fore.BLUE + Style.BRIGHT + "_____________________________________________________________" + 
                  Style.RESET_ALL + Fore.RESET)
                  print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f"You defeated {enemy.name} " +Style.RESET_ALL + Fore.RESET)
                  print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "            C O N G R A T U L A T I O N S " + Style.RESET_ALL + Fore.RESET)
                  print(Fore.BLUE + Style.BRIGHT + "_____________________________________________________________" + 
                  Style.RESET_ALL + Fore.RESET)
                  running = False
                  sleep(3)
                  continue
            
            if enemy.get_hp() < 150:
                  enemy_choice = 1
            else:
                  enemy_choice = randrange(0, 2)
            # enemy_choice
            if enemy_choice == 0:

                  # enemy dmg
                  enemydmg = enemy.gen_dmg() 

                  # player health updating
                  player.up_hp(enemydmg)
                  print(f"{enemy.name} dealth " + Fore.RED +
                        str(enemydmg) + Fore.RESET + f" to {name}")

            elif enemy_choice == 1:
                  if enemy.get_hp() <= 150:
                        enemy_choice = 7
                  elif enemy.get_hp() <= 200:
                        enemy_choice = randrange(6,8)
                  else:
                        enemy_choice = randrange(0,8)
                  # current mp of player is transfered to 'currentmp' variable
                  currentmp = enemy.get_mp()

                  # getting spell out of the [fire, thunder, quake, explosion, blizzard, cure] part of player.magic now
                  spell = enemy.magic[enemy_choice]
                  # checks for if cost of magic is more than current player magic points
                  # if yes the msg is displayed and the rest of the code is skipped
                  if spell.cost > currentmp:
                        print(f"\n" + "Enemy does not enough MP to perfrom the magic spell " +
                              str(enemy.get_mp()) + "/" + str(enemy.get_max_mp()) + "\n")
                        continue

                  # if the cost is less than player's current magic point the
                  # spell is executed on the enemy
                  else:
                        if spell.tpe == "Attack":
                              spell = enemy.magic[enemy_choice]
                              # Generating spell dmg for enemy
                              spelldmg = spell.spell_dmg()

                              # Updating player hp
                              player.up_hp(spelldmg)

                              # enemy mp is updated
                              enemy.up_mp(spell.cost)

                              # stats is displayed
                              print(f"{enemy.name} used {spell.name} dealth " + Fore.RED +
                                    str(spelldmg) + Fore.RESET)

                        elif spell.tpe == "Heal":
                              spell = enemy.magic[enemy_choice]
                              # Generating spell dmg for enemy
                              spelldmg = spell.spell_dmg()

                              # Updating player hp
                              enemy.heal(spelldmg)

                              # enemy mp is updated
                              enemy.up_mp(spell.cost)
                              print

                              # stats is displayed
                              print(f"{enemy.name} healed for " + Fore.GREEN +
                                    str(spelldmg) + Fore.RESET + Style.RESET_ALL + f" HP ")

            player.player_stats()
            enemy.enemy_stats()

            # checking when the fight is supposed to end via player hp
            # that is if the player died or not
            if player.get_hp() == 0:
                  print(Fore.BLUE + Style.BRIGHT + "_____________________________________________________________" + 
                  Style.RESET_ALL + Fore.RESET)
                  print(Fore.RED + Style.BRIGHT + f"{enemy.name} has defeated you " + Fore.RESET + Style.RESET_ALL)
                  print(Fore.BLUE + Style.BRIGHT + "_____________________________________________________________" + 
                  Style.RESET_ALL + Fore.RESET)
                  running = False
                  sleep(3)

            
                  
      except ValueError:
            print(Fore.RED + Style.BRIGHT + "\ninvalid input\n" + Fore.RESET + Style.RESET_ALL)
