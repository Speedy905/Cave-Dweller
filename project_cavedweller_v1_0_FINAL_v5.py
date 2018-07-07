#Project Cave Dweller
#------------------------------------------------------
#MAKE SURE YOU CHANGE THE VERSION EVERYTIME YOU EDIT IT 
#Version: 1.0 (FINAL)
#------------------------------------------------------
#Adam, Andres, Antonio Karlo, Peter, Seymour
#------------------------------------------------------

#Imports pygame and other necessities 
import pygame, random, sys, copy, time
from pygame.locals import *


#Sets up the pygame variables and requirements 
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255,255,255)
BACKGROUNDCOLOR = (0,0,0)
FPS = 60
PLAYERMOVERATE = 6
bear_values = [0,4]
bat_food = 0
turtle_food = 0
rabbit_food = 0
fox_food = 0

#Player movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

#Main classes of the game.
class PCanimals(): #all the animals that the user controls 
    pass #nothing but the bear, so everything initialized in the bear class

class bearClass(PCanimals): #only controllable character 
    def __init__(self):
        super(bearClass, self).__init__()
        self.name = 'Bear' #name of animal 
        self.food = 0 #user starts with 0 food
        self.energy = 6 #user starts with 6 energy to use to enter activities
#############################################  
      
class NPCanimals(object): #all the AI that the user will challenge 
    def __init__(self): 
        self.name = 'Animal Name' #only placeholder 
        self.food = 10 # AI has 10 food to give away 
        self.energy = 2 # AI has 2 energy to give away 
        
        
class foxClass(NPCanimals): #class for the fox 
    def __init__(self):
        super(foxClass, self).__init__()
        self.name = 'Fox' #name of animal 
        
class batClass(NPCanimals):
    def __init__(self):
        super(batClass, self).__init__()
        self.name = 'Bat' #name of animal 
        
class turtleClass(NPCanimals):
    def __init__(self):
        super(batClass, self).__init__()
        self.name = 'Turtle' #name of animal   
              
class rabbitClass(NPCanimals):
    def __init__(self):
        super(batClass, self).__init__()
        self.name = 'Rabbit' #name of animal 
        
#############################################  

#Sets up the main functions for the game

#Exits the game
def leave():
    pygame.quit()
    sys.exit()                
                
#Waits for user to press a specific key
def waitForPlayertoPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                leave()
            if event.type == KEYDOWN:
                #Pressing escape or q exits the game
                if event.key == K_ESCAPE or event.key == ord('q') :
                    leave()
                #Pressing h goes to the help menu
                if event.key == ord('h'):
                    showHelp()
                return
            
#Waits for player to press any Key
def anyKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                leave()
            if event.type == KEYDOWN:
                return

#Be able to show text
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#PUZZLE FUNCTIONS
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
def batPuzzle(bear_values): # Creates a function to the name batPuzzle that recieves 1 parameter.
    # Loads an image and makes it into a rect.
    bat_img = pygame.image.load('puzzle images/bat_background.png')
    bat_img_rect = bat_img.get_rect()
    user_chances = 0 # Assigns the value of 0 to user_chances.
    guess_count = 3 # Assigns the value of 3 to user_chances.
    while user_chances < 3: # While user_chances is less than 3, execute the code below.
        # Loads 2 rock images and makes them into rects.
        spriteRock1 = pygame.image.load('puzzle images/rock1.png')
        rock1Rect = spriteRock1.get_rect()
        spriteRock2 = pygame.image.load('puzzle images/rock2.png')
        rock2Rect = spriteRock2.get_rect()
        # Blits the background onto the screen,
        windowSurface.blit(bat_img, bat_img_rect)
        # Draw text to the screen using our drawText function.
        drawText('Hello, there are berries under one of these rocks.', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
        drawText('Guess which one it is under to get your food.', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5) + 30)
        drawText('Press 1 for the first rock or 2 for the second rock.', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5)+ 60)
        drawText('You have ' + str(guess_count) + ' guess(es)', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5) + 90)
        # Moves the position of the rects.
        rock1Rect.top += 300
        rock1Rect.right += 200
        rock2Rect.top += 300
        rock2Rect.right += 400
        # Blits the two rocks onto the screen.
        windowSurface.blit(spriteRock1, rock1Rect)
        windowSurface.blit(spriteRock2, rock2Rect)
        bat_list = [1,0] # Creates a list with two values.
        random.shuffle(bat_list) # Shuffles the list.
        pygame.display.update() # Updates the screen.
        for event in pygame.event.get():
            if event.type == QUIT:  # If the event is the user pressing the x at the top right, execute the code below.
                leave() # Run the leave() function.
            if event.type == KEYDOWN: # If the event is a user pushing a key down, execute the code below.
                if event.key == K_1: # If the key pushed down is 1, execute the code below.
                    rock_1 = bat_list.pop(0) # Pops the list at position 0 and assigns it to rock_1.
                    if rock_1 == 1: # If rock_1 is 1, execute the code below.
                        windowSurface.blit(bat_img, bat_img_rect) # Blits the background onto the screen.
                        # Draws text onto the screen.
                        drawText('Correct, here is your food. Press any key to return.', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                        user_chances = 4 # Assigns user_chances to 4 to stop the while loop.
                        pygame.display.update() # Updates the screen.
                        anyKey() # Allows the user to press any key to continue.
                    else: # If the above if does not run, execute the code below.
                        windowSurface.blit(bat_img, bat_img_rect) # Blits the background onto the screen.
                        # Draws text to the screen.
                        drawText('Wrong, I will shuffle the rocks then try again. Press any key to return', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                        user_chances += 1 # Adds 1 to user_chances.
                        guess_count -= 1 # Subtracts 1 from guess_count.
                        pygame.display.update() # Updates the screen.
                        anyKey() # Allows the user to press any key to continue.
                if event.key == K_2: # If the key pushed down is 2, execute the code below.
                    rock_2 = bat_list.pop(0) # Pops the list at position 0 and assigns it to rock_2.
                    if rock_2 == 1: # If rock_2 is 1, execute the code below.
                        windowSurface.blit(bat_img, bat_img_rect)# Blits the background onto the screen.
                        # Draws text to the screen.
                        drawText('Correct, here is your food. Press any key to return.', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                        user_chances = 4 # Assigns user_chances to 4 to stop the while loop.
                        pygame.display.update() # Updates the screen.
                        anyKey() # Allows the user to press any key to continue.
                    else: # If the above if does not run, execute the code below.
                        windowSurface.blit(bat_img, bat_img_rect) # Blits the background onto the screen.
                        # Draws text to the screen.
                        drawText('Wrong, I will shuffle the rocks then try again. Press any key to return.', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                        user_chances += 1 # Adds 1 to user_chances.
                        guess_count -= 1  # Subtracts 1 from guess_count.
                        pygame.display.update() # Updates the screen.
                        anyKey() # Allows the user to press any key to continue.
    
    if user_chances >= 4: # If user_chances is greater than or equal to 4, execute the code below.
        bear_food = bear_values.pop(0) # Pops from position 0 and assigns the value to bear_food.
        bear_food += 2 # Adds 2 to bear_food.
        bear_values.insert(0, bear_food) # Inserts the value back into the list at position 0.
        return bear_values # Return bear_values.
    else: # If the above if does not run, execute the code below.
        bear_energy = bear_values.pop(1) # Pops from position 1 and assigns the value to bear_energy.
        bear_energy -= 1 # Subtracts 1 from bear_energy.
        bear_values.insert(1, bear_energy) # Inserts the value back into the list at position 1.
        return bear_values # Return bear_values.

#Rabbit Puzzle
def rabbitPuzzle(bear_values): # Define a function to the name rabbitPuzzle that takes 1 parameter.
    # Loads images and makes them all into rects.
    race_start = pygame.image.load('puzzle images/rabbit_race.png')
    race_startRect = race_start.get_rect()
    race_win = pygame.image.load('puzzle images/rabbit_race_bwin.png')
    race_winRect = race_win.get_rect()
    race_lose = pygame.image.load('puzzle images/rabbit_race_rwin.png')
    race_loseRect = race_lose.get_rect()
    windowSurface.fill(BACKGROUNDCOLOR) # Fills the window with the background colour.
    # Draws text to the screen calling the drawText function.
    drawText('Hello we will race for your prize.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5))
    drawText('You have an 80% chance of winning if you race once.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 20)
    drawText('You have an 60% chance of winning if you race twice.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 50)
    drawText('Race 1 gives you two food if you win and Race 2 gives you 3.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 80)
    drawText('Press 1 for race one and press 2 for race two.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 110)
    race_startRect.topleft = (0, 385) # Moves the position of the rect.
    windowSurface.blit(race_start, race_startRect) # Blits the rect to the screen.
    pygame.display.update() # Updates the screen.
    flag = True # Assigns the boolean value of Flag to True.
    while flag: # While flag is true, execute the code below.
        for event in pygame.event.get(): # Gets an event from the user.
            if event.type == QUIT: # If the event us QUIT, execute the code below.
                leave() # Call the leave function.
            if event.type == KEYDOWN: # If the event is the user pressing a key, execute the code below.
                if event.key == K_1: # If the user presses key 1, execute the code below.
                    race_chance = [1,1,1,1,1,1,1,1,2,2] # Creates a list with eight 1 values and two 2 values.
                    win_lose = race_chance.pop(random.randint(0,9)) # Pops a random value from the list and assign the value to win_lose.
                    if win_lose == 1: # If win_lose is 1, execute the code below.
                        windowSurface.fill(BACKGROUNDCOLOR)
                        distance_win = random.randint(1,99) # Create a random integer between 1 and 99 and assign the value to distance_win.
                        # Draw text to the screen calling the drawText function.
                        drawText('Darn, you won by ' + str(distance_win) + 'cm. Press any key to return.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 50)
                        race_winRect.topleft = (0, 385) # Moves the position of the rect.
                        windowSurface.blit(race_win, race_winRect) # Blits the image to the screen.
                        bear_food = bear_values.pop(0) # Pop the value of position 0 from the list and assign it to bear_food.
                        bear_food += 2 # Add 2 to bear_food.
                        bear_values.insert(0, bear_food) # Insert the value of bear_food back into position 0 of the list.
                        pygame.display.update() # Updates the screen.
                        anyKey() # Calls the anyKey function
                        flag = False # Assigns flag to False.
                    elif win_lose == 2: # If win_lose is 2, execute the code below.
                        windowSurface.fill(BACKGROUNDCOLOR)
                        distance_win = random.randint(1,99) # Create a random integer between 1 and 99 and assign the value to distance_win.
                        drawText('AHA, I won by ' + str(distance_win) + 'cm. Press any key to return.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 50)
                        race_loseRect.topleft = (0, 385) # Moves the position of the rect.
                        windowSurface.blit(race_lose, race_loseRect) # Blits the image to the screen.
                        bear_energy = bear_values.pop(1) # Pop the value of position 1 from the list ans assign it to bear_energy.
                        bear_energy -= 1 # Subtract 1 from bear_energy.
                        bear_values.insert(1, bear_energy) # Insert the value of bear_energy back into the list at position 0.
                        pygame.display.update() # Updates the screen.
                        anyKey() # 
                        flag = False # Assigns flag to False.
                if event.key == K_2:
                    race_chance = [1,1,1,1,1,1,2,2,2,2] # Creates a list with six 1 values and four 2 values.
                    win_lose = race_chance.pop(random.randint(0,9)) # Pops a random value from the list and assign the value to win_lose.
                    if win_lose == 1: # If win_lose is 1, execute the code below.
                        windowSurface.fill(BACKGROUNDCOLOR)
                        distance_win = random.randint(1,99) # Create a random integer between 1 and 99 and assign the value to distance_win.
                        # Draw text to the screen calling the drawText function.
                        drawText('Darn, you won by ' + str(distance_win) + 'cm. Press any key to return.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 50)
                        race_winRect.topleft = (0, 385) # Moves the position of the rect.
                        windowSurface.blit(race_win, race_winRect) # Blits the image to the screen.
                        bear_food = bear_values.pop(0) # Pop the value of position 0 from the list and assign it to bear_food.
                        bear_food += 3 # Add 3 to bear_food.
                        bear_values.insert(0, bear_food) # Insert the value of bear_food back into position 0 of the list.
                        pygame.display.update() # Updates the screen.
                        anyKey() # Calls the anyKey function.
                        flag = False # Assigns flag to False.
                    elif win_lose == 2: # If win_lose is 2, execute the code below.
                        windowSurface.fill(BACKGROUNDCOLOR)
                        distance_win = random.randint(1,99) # Create a random integer between 1 and 99 and assign the value to distance_win.
                        drawText('AHA, I won by ' + str(distance_win) + 'cm. Press any key to return.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 50)
                        race_loseRect.topleft = (0, 385) # Moves the position of the rect.
                        windowSurface.blit(race_lose, race_loseRect) # Blits the image to the screen.
                        bear_energy = bear_values.pop(1) # Pop the value of position 1 from the list ans assign it to bear_energy.
                        bear_energy -= 1 # Subtract 1 from bear_energy.
                        bear_values.insert(1, bear_energy) # Insert the value of bear_energy back into the list at positon 0.
                        pygame.display.update() # Updates the screen.
                        anyKey() # Calls the anyKey function.
                        flag = False # Assigns flag to False.
    return bear_values # Return the list.

def waitTurtleKey(bear_stat, num_list, t_answer, num1, num2): # Creates a function to the name waitTurtleKey that recieves 1 parameter.
    flag = True # Assigns flag to True.
    # Loads an image and makes it into a rect.
    turtle_img = pygame.image.load('puzzle images/turtle_background.png')
    turtle_img_rect = turtle_img.get_rect()
    while flag: # While True, execute the code below.
        for event in pygame.event.get(): # Get an event from the user.
            if event.type == QUIT:  # If the event is the user pressing the x at the top right, execute the code below.
                leave() # Run the leave() function.
            if event.type == KEYDOWN: # If the event is a user pushing a key down, execute the code below.
                if event.key == K_1 and num_list[0] == t_answer: # If the key pushed down is 1 and the numbers are equal.
                    windowSurface.blit(turtle_img, turtle_img_rect) # Blits the image to the screen.
                    drawText('Correct, here is 2 food! Press any key to return', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                    bear_food = bear_stat.pop(0) # Pop the value of position 0 from a list and assign it to bear_food.
                    bear_food += 2 # Add 2 to bear_food and make that value equal bear_food.
                    bear_stat.insert(0, bear_food)# Insert the value of bear_food back into index 0 of the list.
                    pygame.display.update() # Updates the screen.
                    anyKey() # Calls the anyKey function.
                    flag = False # Assigns flag to False.
                    return bear_stat # Return the list.
                elif event.key == K_1 and num_list[0] != t_answer: # If the key pushed down is 1 and the numbers are not equal.
                    windowSurface.blit(turtle_img, turtle_img_rect) # Blits the image to the screen.
                    drawText('Wrong, You used 1 energy! Press any key to return', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                    bear_energy = bear_stat.pop(1) # Pop the value of position 1 from the list and assign it to bear_energy.
                    bear_energy -= 1 # Subtract 2 from bear_energy and make that value equal bear_energy.
                    bear_stat.insert(1, bear_energy) # Insert the value of bear_energy back into index 1 of the list.
                    pygame.display.update() # Updates the screen.
                    anyKey() # Calls the anyKey function.
                    flag = False # Assigns flag to False.
                    return bear_stat # Return bear_stat.
                if event.key == K_2 and num_list[1] == t_answer: # If the key pushed down is 2 and the numbers are equal.
                    windowSurface.blit(turtle_img, turtle_img_rect) # Blits the image to the screen.
                    drawText('Correct, here is 2 food! Press any key to return', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                    bear_food = bear_stat.pop(0) # Pop the value of position 0 from a list and assign it to bear_food.
                    bear_food += 2 # Add 2 to bear_food and make that value equal bear_food.
                    bear_stat.insert(0, bear_food)# Insert the value of bear_food back into index 0 of the list.
                    pygame.display.update() # Updates the screen.
                    anyKey() # Calls the anyKey function.
                    flag = False # Assigns flag to False.
                    return bear_stat # Return the list.
                elif event.key == K_2 and num_list[1] != t_answer: # If the key pushed down is 2 and the numbers are not equal.
                    windowSurface.blit(turtle_img, turtle_img_rect) # Blits the image to the screen.
                    drawText('Wrong, You used 1 energy! Press any key to return', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                    bear_energy = bear_stat.pop(1) # Pop the value of position 1 from the list and assign it to bear_energy.
                    bear_energy -= 1 # Subtract 2 from bear_energy and make that value equal bear_energy.
                    bear_stat.insert(1, bear_energy) # Insert the value of bear_energy back into index 1 of the list.
                    pygame.display.update() # Updates the screen.
                    anyKey() # Calls the anyKey function.
                    flag = False # Assigns flag to False.
                    return bear_stat # Return bear_stat.
                if event.key == K_3 and num_list[2] == t_answer: # If the key pushed down is 3 and the numbers are equal.
                    windowSurface.blit(turtle_img, turtle_img_rect) # Blits the image to the screen.
                    drawText('Correct, here is 2 food! Press any key to return', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                    bear_food = bear_stat.pop(0) # Pop the value of position 0 from a list and assign it to bear_food.
                    bear_food += 2 # Add 2 to bear_food and make that value equal bear_food.
                    bear_stat.insert(0, bear_food)# Insert the value of bear_food back into index 0 of the list.
                    pygame.display.update() # Updates the screen.
                    anyKey() # Calls the anyKey function.
                    flag = False # Assigns flag to False.
                    return bear_stat # Return the list.
                elif event.key == K_3 and num_list[2] != t_answer: # If the key pushed down is 3 and the numbers are not equal.
                    windowSurface.blit(turtle_img, turtle_img_rect)# Blits the image to the screen.
                    drawText('Wrong, You used 1 energy! Press any key to return', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                    bear_energy = bear_stat.pop(1) # Pop the value of position 1 from the list and assign it to bear_energy.
                    bear_energy -= 1 # Subtract 2 from bear_energy and make that value equal bear_energy.
                    bear_stat.insert(1, bear_energy) # Insert the value of bear_energy back into index 1 of the list.
                    pygame.display.update() # Updates the screen.
                    anyKey() # Calls the anyKey function.
                    flag = False # Assigns flag to False.
                    return bear_stat # Return bear_stat.
                
                return # If none of these keys are pressed return to after the function is called.

def turtlePuzzle(bear_values): # Create a function named turtlePuzzle that recieves 1 parameter.
    turtle_img = pygame.image.load('puzzle images/turtle_background.png')
    turtle_img_rect = turtle_img.get_rect()
    
    windowSurface.blit(turtle_img, turtle_img_rect) # Fill the game window colour to black.
    # Write a sentence to the screen with the following parameters.
    drawText('Hello, add these two numbers to get your prize!', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5))
    t_number1 = random.randint(0,9) # Get a random integer from 0-9 and assign it to t_number1.
    t_number2 = random.randint(0,9) # Get a random integer from 0-9 and assign it to t_number2.
    t_answer = t_number1 + t_number2 # Add the two values and make it equal to t_answer
    # Gets another two random ints.
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num_list = [t_answer, num1, num2] # Create a list with 3 values.
    random.shuffle(num_list) # Shuddles the list.
    new_list = copy.copy(num_list) # Copies the list and assign the new list to new_list.
    list_num = random.randint(0,2) # Get a random number.
    # Write 4 sentences with the following parameters.
    drawText((str(t_number1) + ' + ' + str(t_number2)), font, windowSurface,(WINDOWWIDTH/5), (WINDOWHEIGHT/5) + 20)
    drawText('1: ' + str(num_list.pop(0)), font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5) + 50)
    list_num2 = random.randint(0,1)
    drawText('2: ' + str(num_list.pop(0)),font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5) + 80)
    drawText('3: ' + str(num_list.pop(0)), font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5) + 110) 
    pygame.display.update() # Update the window so the sentences go to the screen.
    bear_new_stats = waitTurtleKey(bear_values, new_list, t_answer, num1, num2) # Call the waitTurtleKey function and send 1 parameter.
    while bear_new_stats == None: # While bear_new_stats is None, execute the code below.
        bear_new_stats = waitTurtleKey(bear_values, new_list, t_answer, num1, num2) # Call the waitTurtleKey function and send 1 parameter.
    return bear_new_stats # Return bear_new_stats.

#Fox puzzle
def foxPuzzle (bear_values): # Creates a function with 1 paramter.
    pygame.mouse.set_visible(True) #Shows the Mouse
    #Loads the fox puzzle sprite
    fox_goalImg = pygame.image.load('puzzle images/fox_goal.png')
    fox_goalRect = fox_goalImg.get_rect()
    
    #Player movement variables
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
    
    #Player speed variable
    PLAYERMOVERATE = 6
    
    windowSurface.fill (BACKGROUNDCOLOR) # Fill the game window colour to black.
    pygame.display.update() # Update the window so the sentences go to the screen.
    
    #Colours
    white = (255,255,255)
    Red = (255, 0, 0)
    Blue = (0, 0, 255)
    
    #BLock movement variables
    LEFT = 4
    RIGHT = 6
        
    #Block speed variable
    moveSpeed = 12
    
    #Block data Structure
    b1 = {'rect':pygame.Rect(200, 200, 60, 60), 'colour':Red, 'dir':RIGHT}
    b2 = {'rect':pygame.Rect(400, 300, 60, 60), 'colour':Blue, 'dir':LEFT}
    b3 = {'rect':pygame.Rect(500, 400, 60, 60), 'colour':white, 'dir':RIGHT}
    blocks = [b1, b2, b3]
    
    #Runs the fox mini game
    fox = True
    while fox:
        playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                leave()
            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where the cursor is.
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)
        
        #States if player collides to the goal rect               
        if playerRect.colliderect(fox_goalRect):
            windowSurface.fill(BACKGROUNDCOLOR)
            drawText('Congratulations! You I will give you 2 food.', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
            bear_food = bear_values.pop(0) # Pop the value of position 0 from a list and assign it to bear_food.
            bear_food += 2 # Add 2 to bear_food and make that value equal bear_food.
            bear_values.insert(0, bear_food) # Insert the value of bear_food back into index 0 of the list.
            pygame.display.update()
            anyKey()
            return bear_values # Return the list. 
            fox = False   
           
        
        # Move the mouse cursor to match the player.
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)
        
        windowSurface.fill(BACKGROUNDCOLOR)
        
        #Block movement code
        for b in blocks:
            if b['dir'] == RIGHT:
                b['rect'].left += moveSpeed
            if b ['dir'] == LEFT:
                b['rect'].right -= moveSpeed
                                          
            if b['rect'].left < 0:
                # block has moved past the left side
                if b['dir'] == LEFT:
                    b['dir'] = RIGHT
            if b['rect'].right > WINDOWWIDTH:
                # block has moved past the right side
                if b['dir'] == RIGHT:
                    b['dir'] = LEFT
            
            #States if player collides with one of the rectangle
            if playerRect.colliderect(b['rect']):
                windowSurface.fill(BACKGROUNDCOLOR)
                drawText('You crashed!!! You used 1 energy. Press any key to return', font, windowSurface, (WINDOWWIDTH/5), (WINDOWHEIGHT/5))
                pygame.display.update()
                bear_energy = bear_values.pop(1) # Pop the value of position 1 from the list and assign it to bear_energy.
                bear_energy -= 1 # Subtract 2 from bear_energy and make that value equal bear_energy.
                bear_values.insert(1, bear_energy) # Insert the value of bear_energy back into index 1 of the list.
                anyKey()
                fox = False
                return bear_values
                 
            # draw the block onto the surface
            pygame.draw.rect(windowSurface, b['colour'], b['rect']) 
        
        fox_goalRect.topleft = (395,17)
        windowSurface.blit(fox_goalImg,fox_goalRect)
        
        #Displays the text onto the window
        drawText('Try to get to the green rectangle!', font, windowSurface, 41, 84)
        drawText('Hint: Move the mouse.', font, windowSurface, 39, 112)
        drawText('Another Hint: Keep on moving.', font, windowSurface, 36, 142)
            
        pygame.display.update()
        mainClock.tick (FPS)
        time.sleep(0.02)
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#Create text animation for Intro 
def displayTextAnimationIntro(string):
    text = ''
    for i in range(len(string)):
        
        #Places the image
        windowSurface.blit(helpImg,helpRect)
        
        #Displays the text onto the window
        drawText('Press any key to continue', font, windowSurface, 94,572)
        
        pygame.display.update()
        
        #Creates the text animation
        text += string[i]
        text_surface = font.render(text, True, TEXTCOLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (359,354)
        windowSurface.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(90)
    return

#Create text animation for Credits
def displayTextAnimationCredit(string):
    text = ''
    for i in range (len(string)):
        windowSurface.blit(creditImg,creditRect)
        #Creates the text animation
        text += string[i]
        text_surface = font.render(text, True, TEXTCOLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = ((WINDOWWIDTH / 2), (WINDOWHEIGHT / 2) )
        windowSurface.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(50)
    return

#Show Help Menu
def showHelp():
    windowSurface.blit(helpImg,helpRect)
    drawText('You are a bear that just arrived to your cave for hibernation.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 8))
    drawText('You realize that your food has been taken away!', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 7) + 10)
    drawText('You must explore the cave, interacting with other animals completing mini-games,', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 6) + 20)
    drawText('to get enough food for hibernation.', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 5) + 15)
    drawText('Time is limited, so make sure you do everything right!', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 4) + 10)
    drawText('Use WASD for movement, or press "p" to pause the game', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 3) + 10)
    drawText('Press any key to start the game', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 2))
    pygame.display.update()
    anyKey()
    intro()
    

#Show the Welcome screen
def showWelcomeScreenandMenu():
    pygame.mouse.set_visible(True) #Shows the mouse
    
    #Loads the menu images
    menuImgTitle = pygame.image.load('main menu images/menu_title.png')
    menuImgRect = menuImg.get_rect()
    
    start_button = pygame.image.load('main menu images/start_button.png')
    start_buttonRect = start_button.get_rect()
    
    help_button = pygame.image.load('main menu images/help_button.png')
    help_buttonRect = help_button.get_rect()
    
    quit_button = pygame.image.load('main menu images/quit_button.png')
    quit_buttonRect = quit_button.get_rect()
    
    #Sets the image locations
    menuImgRect.topleft = (0,0)
    start_buttonRect.topleft = (350, 190)
    help_buttonRect.topleft = (350, 370)
    quit_buttonRect.topleft = (350, 540)
    
    #Displays the image in the window
    windowSurface.blit(menuImg,menuRect)
    windowSurface.blit(menuImgTitle, menuImgRect)
    windowSurface.blit(start_button, start_buttonRect)
    windowSurface.blit(help_button, help_buttonRect)
    windowSurface.blit(quit_button, quit_buttonRect)
    

    pygame.display.update()
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if start_buttonRect.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_visible(False)
                    intro()
                    flag = False
                if help_buttonRect.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_visible(False)
                    showHelp()
                    flag = False
                if quit_buttonRect.collidepoint(mouse_x, mouse_y):
                    leave()
        

#Intro sequence
def intro():
    windowSurface.blit(helpImg,helpRect)
    displayTextAnimationIntro('Oh NO. RAWR! My food has been taken!')               
    anyKey()
    displayTextAnimationIntro('Better go look around the cave before I die!')
    pygame.display.update()

#Credits sequence
def credits():
    displayTextAnimationCredit('Made by BearTactix')
    #Pauses the program at miliseconds (1000 = 1 sec)
    pygame.time.wait(1000)
    displayTextAnimationCredit('Andres: GANTT Chart creator, tile management and creation.')
    pygame.time.wait(2000)
    displayTextAnimationCredit('Peter: Project Scope creator, website management, mini-games coder, collision coder.')
    pygame.time.wait(2000)
    displayTextAnimationCredit('Antonio Karlo: Start menu coder, initial functions coder,  opening sequence coder, credits coder')
    pygame.time.wait(2000)
    displayTextAnimationCredit('Adam: Movement coder, closing sequence coder, mini-game coder.')
    pygame.time.wait(2000)
    displayTextAnimationCredit('Seymour: Site management, Character class creator, UML drawer, Project Management Director.')
    pygame.time.wait(2000)
    displayTextAnimationCredit('Thanks to  H. (2009). A sleuth of bears.....')
    pygame.time.wait(1000) 
    displayTextAnimationCredit('Retrieved October 18, 2016, from http://robertlpeters.com/news/a-sleuth-of-bears')
    pygame.time.wait(1000)
    displayTextAnimationCredit('Thanks to Stewart, P. (2014). Caves Underground Chambers.')
    pygame.time.wait(1000)
    displayTextAnimationCredit('http://science.nationalgeographic.com/science/earth/surface-of-the-earth/caves-article/')
    pygame.time.wait(1000)
    displayTextAnimationCredit('Thanks for playing!')
    pygame.time.wait(1000)
    displayTextAnimationCredit('Bear lives matter.')
    pygame.display.update()
    leave()

#Pause Screen
def pauseScreen():
    #Draws text on the screen
    drawText('PAUSED', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 8))
    drawText('Press "Enter" to unpause, or "q" to quit', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 7) + 10)  
    
    #Runs the pause loop
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                leave()
            if event.type == KEYDOWN:
                #Pressing "escape" or "q" exits the game
                if event.key == K_ESCAPE or event.key == ord('q') :
                    leave()
                #Pressing "Enter" resumes the game
                if event.key == K_RETURN:
                    return
                
        pygame.display.update()
        mainClock.tick(60)

#Function where player wins the game
def playerWin(win):
    windowSurface.fill(BACKGROUNDCOLOR)
    drawText('You have gotten enough food to survive the winter!', font, windowSurface, WINDOWWIDTH / 3, WINDOWHEIGHT / 4)
    drawText('Congratulations you win!', font, windowSurface, WINDOWWIDTH / 3, WINDOWHEIGHT / 3)
    drawText('No need to restart the game for another year.', font, windowSurface, WINDOWWIDTH / 3, 300)
    drawText('Press "q" to quit the game.', font, windowSurface, WINDOWWIDTH/3, 374)
    while win:
        for event in pygame.event.get():
            if event.type == QUIT:
                credits()
            if event.type == KEYDOWN:
                if event.key == ord('q'):
                    credits()                   
        pygame.display.update()

#Function where player loses the game
def playerLose(lose):
    windowSurface.fill(BACKGROUNDCOLOR)
    drawText('You ran out of energy to collect more food!', font, windowSurface, WINDOWWIDTH /4, WINDOWHEIGHT / 4)
    drawText('You Lose...', font,windowSurface, WINDOWWIDTH /3, WINDOWHEIGHT /3)
    drawText('You died from the harsh winter, and cannot restart... Git Gud.', font, windowSurface, 185, 272)
    drawText('Press q to quit.', font, windowSurface, 210, 374)
    while lose:
        for event in pygame.event.get():
            if event.type == QUIT:
                credits()
            if event.type == KEYDOWN:
                if event.key == ord('q'):
                    credits()
        pygame.display.update()

def playerLosePuzzle(lose):
    windowSurface.fill(BACKGROUNDCOLOR)
    drawText('You played all the mini games and did not collect enough food!', font, windowSurface, WINDOWWIDTH /4, WINDOWHEIGHT / 4)
    drawText('You Lose...', font,windowSurface, WINDOWWIDTH /3, WINDOWHEIGHT /3)
    drawText('You died from the harsh winter, and cannot restart... Git Gud.', font, windowSurface, 185, 272)
    drawText('Press q to quit.', font, windowSurface, 210, 374)
    while lose:
        for event in pygame.event.get():
            if event.type == QUIT:
                credits()
            if event.type == KEYDOWN:
                if event.key == ord('q'):
                    credits()
        pygame.display.update()
        
#Set up pygame and the window
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Cave Dweller')
pygame.mouse.set_visible(False) #Hides the mouse

#Set up the font
font = pygame.font.SysFont(None,24)

#Set up the sprites
#Player sprite
playerSprite = pygame.image.load('sprites/spriteBear.png')
playerRect = playerSprite.get_rect()

#Bat sprite
spriteBat = pygame.image.load ('sprites/spriteBat.png')
batRect = spriteBat.get_rect()

#Fox sprite
spriteFox = pygame.image.load ('sprites/spriteFox.png')
foxRect = spriteFox.get_rect()

#Rabbit sprite
spriteRabbit = pygame.image.load ('sprites/spriteRabbit.png')
rabbitRect = spriteRabbit.get_rect()

#Turtle Sprite
spriteTurtle = pygame.image.load ('sprites/spriteTurtle.png')
turtleRect = spriteTurtle.get_rect()

#Loads the Menu Background Image
menuImg = pygame.image.load('background images/menu.png')
menuRect = menuImg.get_rect()

#Loads the Help Background Image
helpImg = pygame.image.load('background images/help.png')
helpRect = helpImg.get_rect()

#Loads an Intro Background Image
introImg = pygame.image.load ('background images/intro.jpg')
introRect = introImg.get_rect()

#Loads Credits Background Image
creditImg = pygame.image.load ('background images/credits.jpg')
creditRect = creditImg.get_rect()

#Loads the tiles images
wallImg = pygame.image.load('tiles/wall.png')
wallRect = wallImg.get_rect()

#Loads the Floor Tiles
floorImg = pygame.image.load('tiles/floor.png')
floorRect = floorImg.get_rect()
floorRect2 = floorImg.get_rect()
floorRect3 = floorImg.get_rect()
floorRect4 = floorImg.get_rect()
floorRect5 = floorImg.get_rect()
floorRect6 = floorImg.get_rect()

#Loads the Long Floor Tiles
longFloorImg = pygame.image.load('tiles/longfloor.png')
longFloorRect = longFloorImg.get_rect()

#Loads the Water Tiles
waterImg = pygame.image.load('tiles/water.png')
waterRect = waterImg.get_rect()
waterRect2 = waterImg.get_rect()
waterRect3 = waterImg.get_rect()


#Runs the Welcome Screen and Menu
showWelcomeScreenandMenu()
pygame.display.update
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#Runs the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            leave() 
        #States if user pushes down a key.     
        if event.type == KEYDOWN:
            #Left button or "A"
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            #Right button or "D"
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            #Up button or "W"
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            #Down button or "S"
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
            #Pause button or "P"
            if event.key == ord('p'):
                paused = True
                pauseScreen()
                
        
        #States if user lets go a key  
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                leave()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
        
    windowSurface.fill(BACKGROUNDCOLOR)
    
    #Sets the tile positions and displays it on the background
    floorRect.topleft = (0,0)
    windowSurface.blit (floorImg, floorRect)
    
    waterRect.topleft = (200, 0)
    windowSurface.blit (waterImg, waterRect)
    
    floorRect2.topleft = (304, 0)
    windowSurface.blit (floorImg, floorRect2)
    
    wallRect.topleft = (504, 0)
    windowSurface.blit (wallImg, wallRect)
    
    floorRect3.topleft = (604, 0)
    windowSurface.blit (floorImg, floorRect3)
    
    longFloorRect.topleft = (0, 200)
    windowSurface.blit (longFloorImg, longFloorRect)
    
    floorRect4.topleft = (0, 400)
    windowSurface.blit (floorImg, floorRect4)
    
    waterRect2.topleft = (200, 400)
    windowSurface.blit (waterImg, waterRect2)
    
    floorRect5.topleft = (304, 400)
    windowSurface.blit (floorImg, floorRect5)
    
    waterRect3.topleft = (504, 400)
    windowSurface.blit (waterImg, waterRect3)    
    
    floorRect6.topleft = (604, 400)
    windowSurface.blit (floorImg, floorRect6)
    
    #Sets the sprite locations and displays the located sprites
    batRect.topleft = (682,550)
    windowSurface.blit (spriteBat,batRect)
    foxRect.topleft = (682,57)
    windowSurface.blit (spriteFox,foxRect)
    rabbitRect.topleft = (384,33)
    windowSurface.blit (spriteRabbit,rabbitRect)
    turtleRect.topleft = (400,550)
    windowSurface.blit (spriteTurtle,turtleRect)    
    
    #Draws the Player
    windowSurface.blit (playerSprite, playerRect)
    
    
    # Checks to see if the player collides with any of the animals.    
    if playerRect.colliderect(batRect) == True and bat_food == 0:
        bear_values = batPuzzle(bear_values)
        playerRect.topleft = (682,450)
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        bat_food = 1
    if playerRect.colliderect(foxRect) == True and fox_food == 0:
        bear_values = foxPuzzle(bear_values)
        playerRect.topleft = (682, 100)
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        fox_food = 1
    if playerRect.colliderect(rabbitRect) == True and rabbit_food == 0:
        bear_values = rabbitPuzzle(bear_values)
        playerRect.topleft = (400,100)
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        rabbit_food = 1
    if playerRect.colliderect(turtleRect) == True and turtle_food == 0:
        bear_values = turtlePuzzle(bear_values)
        playerRect.topleft = (400,480)
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        turtle_food = 1
        
    # Checks to see if the player collides with unwalkable terrain such as the water and walls.
    # If they do move them away from the rect and stop their movement.
    if playerRect.colliderect(waterRect):
        if playerRect.colliderect(waterRect) and playerRect.right > 180 and playerRect.right < 240:
            playerRect.move_ip(-1, 0)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
        if playerRect.colliderect(waterRect) and playerRect.top < 240 and playerRect.top > 150:
            playerRect.move_ip(0, 1)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
        if playerRect.colliderect(waterRect) and playerRect.left < 300 and playerRect.left > 260:
            playerRect.move_ip(1,0)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
    if playerRect.colliderect(waterRect2):
        if playerRect.colliderect(waterRect2) and playerRect.right > 180 and playerRect.right < 240:
            playerRect.move_ip(-1, 0)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
        if playerRect.colliderect(waterRect2) and playerRect.bottom > 360 and playerRect.bottom < 450:
            playerRect.move_ip(0, -1)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
        if playerRect.colliderect(waterRect2) and playerRect.left < 390 and playerRect.right > 340:
            playerRect.move_ip(1, 0)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
    if playerRect.colliderect(waterRect3):
        if playerRect.colliderect(waterRect3) and playerRect.right > 504 and playerRect.right < 550:
            playerRect.move_ip(-1,0)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
        if playerRect.colliderect(waterRect3) and playerRect.bottom > 400 and playerRect.bottom < 450:
            playerRect.move_ip(0, -1)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
        if playerRect.colliderect(waterRect3) and playerRect.left < 650 and playerRect.right > 590:
            playerRect.move_ip(1, 0)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
    if playerRect.colliderect(wallRect):
        if playerRect.colliderect(wallRect) and playerRect.right > 504 and playerRect.right < 550:
            playerRect.move_ip(-1,0)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
        if playerRect.colliderect(wallRect) and playerRect.top < 240 and playerRect.top > 150:
            playerRect.move_ip(0, 1)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
        if playerRect.colliderect(wallRect) and playerRect.left < 700 and playerRect.right > 650:
            playerRect.move_ip(1, 0)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
            
    #Checks if player has the required amount of food
    if bear_values[0] >= 6:
        win = True
        playerWin(win)
    #Check if player has no more energy
    elif bear_values[1] <= 0:
        lose = True
        playerLose(lose)
    elif turtle_food == 1 and rabbit_food == 1 and fox_food == 1 and bat_food == 1 and bear_values[0] < 6:
        lose = True
        playerLosePuzzle(lose)
    
    
    # Moves the player
    if moveDown and playerRect.bottom < WINDOWHEIGHT:
        playerRect.top += PLAYERMOVERATE
    if moveUp and playerRect.top > 0:
        playerRect.top -= PLAYERMOVERATE
    if moveLeft and playerRect.left > 0:
        playerRect.left -= PLAYERMOVERATE
    if moveRight and playerRect.right < WINDOWWIDTH:
        playerRect.right += PLAYERMOVERATE
    
    #Displays the player's stats
    drawText('Your stats', font, windowSurface, 12,405)
    drawText('Energy: ' + str(bear_values[1]), font, windowSurface, 12, 432)
    drawText('Food: ' + str(bear_values[0]), font, windowSurface, 12,464)
    drawText('Required food: 6', font, windowSurface, 12,484)
    
    
    pygame.display.update()
    mainClock.tick (FPS)

    
