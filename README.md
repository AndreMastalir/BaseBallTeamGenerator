Description of Class:
In this program, there is a Baseball Team Class that converts a roster of players into a Baseball team with randomized attributes. The objects of the class are the players. The class attribute is the number of players on the team: 9. The two data attributes are position and power of a player. This class uses the random module to generate randomized attributes. This Class also contains two get-set methods for retrieving the position and power of a player. This class also contains a method to get the average hitting power of the team and a display method to display a player’s attributes.
Class Attribute: num_of_players
	The num_of_players attribute pertains to all objects because there are a total of 9 players from a team on the field at any given time.
Data Attributes:
	Position
-	The position attribute is the position of a player, for example, 1B is First Base.
Power
-	The power attribute is an arbitrary number from 1-99 that represents how hard a player can swing and how far they can hit a ball.
Extra Methods:
display_info: 
-	This method cleanly displays the objects name and attributes. It returns a string and takes in the object itself.
get_average_power:
-	This method calculates the average power of the team. It returns a string  and takes in the list of objects.
Description of Demo Program:
	This program allows you to input player names for a baseball team, then will return a team with randomized power attributes and position. The program will then allow you to manipulate the stats of a chosen player.
Instructions:
	This program is a user interaction program. You first run the program, then enter the names of the players you wish to be on your roster, could be anyone! The program will then ask you to enter the number of the player you wish change the attributes of, for example 1 will pick the first player entered. Then you’ll be guided along instructions on what to enter and finally, the program will print out the changed attributes of the chosen player.
