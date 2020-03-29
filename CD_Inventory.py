#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# joeprado, 2020-Mar-28, Added code to adress all TODOs
# joeprado, 2020-Mar-20, Changed all object attributes to private
# joeprado, 2020-Mar 29, Continued working on code
# joeprado, 2020-Mar-29, Changed file name to CD_Inventory.py
# joepradi, 2020-Mar-29, Updated/added docstrings. 
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []


class CD(object):
    """Stores data about a CD:

    properties:
        __cd_id: (int) with CD ID  (private attribute)
        __cd_title: (string) with the title of the CD (private attribute)
        __cd_artist: (string) with the artist of the CD (private attribute)
    methods:
        __init__(cdID, title, artist, lst_Inventory): Constructor that conducts error trapping on user CD ID input,
        automatically creates object attributes, and adds CD information to list of CD objects
        cd_id: getter and setter methods to provide read and write to access to private attribute
        cd_title: getter and setter methods to provide read and write to access to private attribute
        cd_artist: getter and setter methods to provide read and write to access to private attribute
    """
    
    def __init__(self, cdID, title, artist, lst_Inventory):
        """Constructor funcriton to create atributes for CD Objects
        
        Conducts error trapping on user CD ID input, creates object attributes, and adds 
        CD information to list of CD objects
        
        Args:
            cdID (int): CD ID either inputted by user or read from file. 
            title (string): CD Title either inputted by user or read from file.
            artist (string): CD Artists  either inputted by user or read from file.
            lst_Inventory (list of objects): 2D data structure that holds the data during runtime
                
        Returns:
            None
        """
        if not str(cdID).isnumeric():
            print ("\nYou must enter the CD ID as an integer. Adding CD failed.")
            input("Press 'Enter' to Continue")
        else:
            self.__cd_id = cdID
            self.__cd_title = title
            self.__cd_artist = artist
            row = self
            lst_Inventory = lst_Inventory.append(row)
        
    @property
    def cd_id(self):
        """Getter Function to access __cd_id attribute"""
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        """Setter Function to assign __cd_id attribute and conduct error trapping"""        
        if not str(value).isnumeric():
            print("ID must be an integer!")
        else:
            self.__cd_id = value
            
    @property
    def cd_title(self):
        """Getter Function to access __cd_title attribute"""
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        """Setter Function to assign __cd_title attribute and conduct error trapping"""  
        if str(value).isnumeric():
            print("Title can't just be numbers!")
        else:
            self.__cd_title = value         
            
    @property
    def cd_artist(self):
        """Getter Function to access __cd_artist attribute"""
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        """Setter Function to assign __cd_artist attribute and conduct error trapping"""  
        if str(value).isnumeric():
            print("Artist can't just be numbers!")
        else:
            self.__cd_artist = value 

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:
        None

    methods:     
        load_inventory(file_name, lst_Inventory): loads text file and creates list of CD Objects
        save_inventory(file_name, lst_Inventory): Saves list of CD Objects into text file. 

    """
    # TODO Add code to process data from a file
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from file to a list of objects.

        Reads the data from file identified by file_name into a 2D table (list of objects) 
        Each line in the file is instantiated into a CD Object, then appended to list of CD objects thru 
        the _init_ constructor.
        
        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of objects): 2D data structure that holds the data during runtime

        Returns:
            None.
        """
        lst_Inventory.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                objCD = CD(data[0], data[1], data[2], lst_Inventory)
            objFile.close()
        except IOError: 
            print("\nNo CD file exists.  Add and save CD info to inventory to create a file.")
            input("Press 'Enter' to continue.")
    
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to save the contents of CD Inventory in volatile memory into a text file.
        
        Takes the list of CD Objects, formats it human readable text, and saves it into text file identified 
        by file_name.
        
        
         Args:
            file_name (string): name of file used to save data to. 
            lst_Inventory (list of objects): 2D data structure that holds the data during runtime
            
        Returns:
            None
        """
        objFile = open(file_name, 'w')
        for row in lst_Inventory:
            cdID = row.cd_id
            cdID = str(cdID)
            title = row.cd_title
            artist = row.cd_artist
            objFile.write("{},{},{}\n".format(cdID, title, artist))
        objFile.close()
    
# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output
    
    properties:
        None

    methods:     
        print_menu(): Displays a menu of choices to the  user.
        menu choice(): Gets user input for menu selection
        show_inventory(lst_Inventory): Displays current inventory table
        intpu_new_cd(): Function that collects user input for a new CD to be added to inventory
        
        """
 
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('\nMenu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
   
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
  
    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory table
        
        Iterates through list of CD Objects, accesses object attributes thru dot notation, assigns attributes 
        to seperate variables, then prints in readable format. 

        Args:
            lst_Inventory (list of objects): 2D data structure that holds the data during runtime.

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            cdID = row.cd_id
            title = row.cd_title
            artist = row.cd_artist
            print('{}\t{} (by: {})'.format(cdID, title, artist))
        print('======================================')
   
    @staticmethod
    def input_new_cd():
        """Function that collects user input for a new CD to be added to inventory.
        
        Args: 
            None.
            
        Returns:
            cdID (string): string representing ID number user entered for CD 
            title (string): string representing CD title entered by user
            artist (string): string representing artist name entered by user
        """
        cdID = input('Enter ID: ').strip()
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return cdID, title, artist

# -- Main Body of Script -- #
FileIO.load_inventory(strFileName, lstOfCDObjects) # When program starts, calls function that reads in the currently saved Inventory
while True:
    IO.print_menu() #Display Menu to user and get choice
    strChoice = IO.menu_choice() # Process menu selection
    if strChoice == 'x': #Process exit first
        break
    if strChoice == 'l': #Process load inventory
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects) #Calls function that loads text file containing CD inventory into runtime. 
            IO.show_inventory(lstOfCDObjects) #Calls function that displays inventory to user
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects) #Calls function that displays inventory to user
        continue  # start loop back at top.
    elif strChoice == 'a': #Process user input
        strID, strTitle, strArtist = IO.input_new_cd() # Calls function that asks user for new ID, CD Title and Artist
        objCD = CD(strID, strTitle, strArtist, lstOfCDObjects) # Instatiates CD Object using Class CD. Constructor also adds object to runtime list
        IO.show_inventory(lstOfCDObjects) #Calls function that displays inventory with added CD
        continue  # start loop back at top.
    elif strChoice == 'i':  # Process display current inventory
        IO.show_inventory(lstOfCDObjects) # Calls function that displays current inventory
        continue  # start loop back at top.
    elif strChoice == 's': #Process save inventory to file
        IO.show_inventory(lstOfCDObjects)    # Calls function that displays current inventory. 
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower() #asks user for confirmation to save
        if strYesNo == 'y': # Process choice
            FileIO.save_inventory(strFileName, lstOfCDObjects) # Calls function that saves data
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:  # catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
        print('General Error')


