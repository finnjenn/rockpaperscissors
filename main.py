import random
import time

rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# while true loop
  # asks user if they would like to play the game
  # if yes while loop to play best two out of three?
    # computer_wins = 0, hero_wins = 0
    # while computer_wins < 2 or hero_wins is < 2
      # game count variable to increment with amount of games
      # f'Game number {game_count}!'
      # ask user to choose their weapon
      # randomly generate a weapon for the computer
      # outputs computer choice and hero choice with art 
      # compare weapon_cp to weapon_hero
        # if cp wins, add one to win variable and add one to game count 
        # if hero wins, add one to win variable and add one to gane count
        # if it is a tie, print that it is a tie. I think a continue will work to simulate a redo 
        # maybe add some art for a tie??
      # 
  # else (no they dont want to play)
    # print 'terminating game...'
    # python sleep 2 seconds
    # break loop 



while True:
  print(f'Welcome to Rock, Paper, Scissors!')
  response = input('Would you like to play the game?\nType yes or no.\n>>> ').lower()

  if response == 'yes':
    computer_wins = 0
    hero_wins = 0
    # Main game
    while True:
      if computer_wins == 2:
        print('\nThe computer has won the best 2 out of 3 games.')
        print('Game restarting...')
        time.sleep(1)
        break
      if hero_wins == 2:
        print('\nYou have won the best 2 out of 3 games! Congratulations!')
        print('Game restarting...')
        time.sleep(1)
        break
       
      weapon_cp = random.randint(1,3)
      print(f'Game begin!\n')
      time.sleep(1)
      print('What weapon will you choose?\n')
      time.sleep(1)
      weapon_hero = int(input('To choose Rock, enter 1\nTo choose Paper, enter 2\nTo choose Scissors, enter 3\n'))
      if weapon_cp == 1:
        print(rock_art)
        print('Computer chose Rock!\n\n')
      elif weapon_cp == 2:
        print(paper_art)
        print('Computer chose Paper!\n\n')
      else:
        print(scissors_art)
        print('Computer chose Scissors!\n\n')

      if weapon_hero == 1:
        print(rock_art)
        print('You chose Rock!\n\n')
      elif weapon_hero == 2:
        print(paper_art)
        print('You chose Paper!\n\n')
      else:
        print(scissors_art)
        print('You chose Scissors!\n\n')
      if weapon_cp == weapon_hero:
        print('Tie\n')
        
      # Wins
      elif (weapon_cp == 1 and weapon_hero == 2) or (weapon_cp == 2 and weapon_hero == 3) or (weapon_cp == 3 and weapon_hero == 1):
        print('You won against the computer!\n')
        hero_wins += 1
        
      
      else:
        print('I\'m sorry. You lost against the computer.\n')
        computer_wins += 1
      print('Computer wins: ' + str(computer_wins) +'\nHero wins: ' + str(hero_wins))

    
          
    
  elif response == 'no':
    print('Terminating game...')
    time.sleep(2)
    break

  else:
    print('Invalid entrance')
    continue

print('Game has ended. Run program agan.')
