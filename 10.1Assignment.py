"""
Andre Mastalir
Professor Hari
Intro to Python Assignment 10.1 Custom Class
"""
#import time and random modules
import random 
import time

#set global variables for help
position_change = None
dict_of_positions = {}

#Create class for a base ball team where each player is an object
class BaseBall_Team:
    #try and except for input handling
    try:
        #class attribute because a BaseBall Team will always have 9 players on the field
        num_of_players = 9 
        #init function with optional power and position arguments
        def __init__(self, name, power=0, position="bench"):
            #set name as object attrubite
            self.__name = name
            #set napowerme as object attrubite
            self.__power = power 
            #set position as object attrubite
            self.__position = position

        #get power function to get access to hidden variables
        def get_power(self):
            #return object's power
            return self.__power
        #get position function to get access to hidden variables
        def get_position(self):
            #return object's position on field
            return self.__position
        #get name function to get access to hidden variables
        def get_name(self):
            #return object's name
            return self.__name
        
        #Function to change the position of a player
        def set_position(self):
            #catalogue old position
            old_pos = self.__position
            #catalogue new poition as global variable
            position_change = input(f"Please enter the position you wish to switch {self.__name} to, the choices are: 1B, 2B, 3B, LF, RF, CF, C, P, SS\n>>>")
            #set selfs position as new position
            self.__position = position_change
            #return string saying the switch has been made
            return f"Position of {self.__name} changed to {self.__position}"
        #function to set new power attribute
        def set_power(self):
            #Print randomizing attribute
            print("Randomizing Power Attribute...")
            #stall for 1.5 seconds
            time.sleep(1.5)
            #get new power randomly through random 
            new_power = random.randint(1, 99)
            #set self's new power attriute
            self.__power = new_power    
            #return string explaing what happened                             
            return f"Power of {self.__name} randomly changed to {self.__power}"
        
        #Function to get the information of a player
        def display_info(self):
            #return player name, power, and position
                return f"Player Name: {self.get_name()}, Power: {self.get_power()}, Position: {self.get_position()}"
        #Function to get the average hitting power from the team
        def get_average_power(roster):
            #set sum as 0
            sum = 0
            #for every obj in roster
            for obj in roster:
                #add power attribute to  sum
                sum += int(obj.get_power())
            #calculate average power
            average_power = sum / 9
            #return calculation in a string
            return f"The average power of your team is {average_power}"
    except:
        print("Invalid Input")
        
#function to build team using user input
def get_roster():
    #try and except for input handling
    try:
        #empty roster
        roster_of_players = []
        #for i in the range from 1 to 10
        for i in range(1, 10): 
            #if i = 1
            if i == 1:
                #Get First player of the team
                roster_of_players.append(input(f"Enter the name of the {i}st player of your team in the form: First Last\n>>>"))
            #if i is 2
            if i == 2:
                #Get second player of the team
                roster_of_players.append(input(f"Enter the name of the {i}nd player of your team in the form: First Last\n>>>"))
            #if i is 3
            if i == 3:
                ##Get third player of the team
                roster_of_players.append(input(f"Enter the name of the {i}rd player of your team in the form: First Last\n>>>"))
            #if i is 4-10
            if i > 3 and i <= 10:
                #Get 4th - 10th player of the team
                roster_of_players.append(input(f"Enter the name of the {i}th player of your team in the form: First Last\n>>>"))
        #interface message
        print("Team Built")
        #return filled roster
        return roster_of_players
    #if janky input, print error message
    except:
        print("Invalid Input")

#funtion to assign random position to the players
def get_random_positions(roster):
    #list of all positions
    list_of_positions = ["1B", "2B", "3B", "LF", "CF", "RF", "C", "SS", "P"]
    #counter starting at 8 counting down for indexing
    counter = 8
    #counter starting at 0 counting up for indexing
    counter2 = 0
    #for player in roster
    for x in roster:
         #if statement to continue for 9 iterations
        if counter >= 0:
            #calculate random int for position
            x = random.randint(0,counter)
            #dictionary for player:positions tracking
            dict_of_positions[roster[counter2]] = list_of_positions[x]
            #del position that was just assigned
            del list_of_positions[x]
            #sub counter by 1
            counter -= 1
            #add counter by 1
            counter2 += 1
    #return final dictionary
    return dict_of_positions

#function to update each player to Basbeball Team class
def update_roster(roster):
    #empty roster
    updated_roster = []
    #create a dictionary for player:position items
    position_dict = get_random_positions(roster)
    #print interface message
    print("Updating Roster...")
    #sleep for 2 secs
    time.sleep(2)
    #print interface message
    print("Randomizing player attributes...")
    #sleep for 2 secs 
    time.sleep(2)
    #for i in range from 0 to the length of the roster
    for i in range(0, len(roster)):
        #add created objects to updated roster list
        updated_roster.append( BaseBall_Team(f"{roster[i]}", random.randint(1, 99), position_dict[roster[i]]))
    #print interface message
    print("Roster Updated!")
    #return list of objects
    return updated_roster

#main function
def main():
    #try and except for input handling
    try:
        #get object roster from helper functions
        roster = update_roster(get_roster())
        #print interface message
        print("Here is your baseball team with Randomized Positions and Power")
        #counter for indexing
        counter = 1
        #for every object in object list
        for obj in roster:
            #print player name and attributes
            print(f"Player {counter} Name: {obj.get_name()} Power: {obj.get_power()} Position: {obj.get_position()}")
            #add to counter
            counter += 1
        #print class attribute
        print(f"Total number of players: {BaseBall_Team.num_of_players}")
        #print average hitting power
        print(f"{BaseBall_Team.get_average_power(roster)}")
        #get player number for alterations
        number = (int(input("Please enter the number of the player whose attributes you wish to change.\n>>> ")) - 1)
        
        #print chosen players attributes
        print(f"The name of player number {number + 1} is: {roster[number].get_name()}")
        print(f"The position of player number {number + 1} is: {roster[number].get_position()}")
        print(f"The power of player number {number + 1} is: {roster[number].get_power()}")
        #print the change in position
        print(roster[number].set_position())
        #print change in power attribute
        print(roster[number].set_power())

        #print new average power
        print(f"{BaseBall_Team.get_average_power(roster)}")
        #use display method to cleanly print players changed status
        print(roster[number].display_info())
    #except phrase for input handling
    except:
        print("Invalid Input")

#call main function
if __name__ == "__main__":
    main()