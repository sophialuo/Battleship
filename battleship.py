
class Piece(object):  
    '''
    Piece is the parent class of all the unique types of ships in the game and 
    keeps track of its start and end points on a matrix, the cells that it
    occupies on a matrix, the number of cells of its occupied cells that have been 
    hit, and its size.
    '''
    
    def __init__(self, start, end, size):
        '''
        Initializes a Piece object with the following instance variables:
            self.start: tuple with board coordinates 
            self.end: tuple with board coordinates 
            self.occupied_cells: dictionary where the keys are tuples that represent
                                 all board cells the Piece occupies & values are initialized
                                 to 0 and set to 'H' when the cell is hit
            self.hit_cells: number of cells hit by the opponent, initialized to 0
            self.size: the size of the ship
        Args: 
            start: tuple with board coordinates 
            end: tuple with board coordinates
                        
        Exceptions: 
            if the start and end coordinates do not form the correct piece size;
            if the start and end coordinates are not on the same horizontal\vertical line
        '''
        self.start = start 
        self.end = end
        self.occupied_cells = {} 
        self.hit_cells = 0 
        self.size = size
        
        start_x = start[0]
        start_y = start[1]
        end_x = end[0]
        end_y = end[1]
        
        #vertical orientation
        if start_y == end_y:
            #wrong sizing
            if abs(end_x - start_x)+1 != self.size:
                raise Exception('Invalid piece size.')
            #go from topmost cell to bottommost cell
            top = min(start_x, end_x)
            bottom = max(start_x, end_x)+1
            for i in range(top, bottom):
                self.occupied_cells[(i, start_y)] = 0
        #horizonal orientation
        elif start_x == end_x:
            #wrong sizing
            if abs(end_y - start_y)+1 != self.size:
                raise Exception('Invalid piece size.')
            #go from leftmost cell to rightmost cell
            left = min(start_y, end_y)
            right = max(start_y, end_y)+1
            for i in range(left, right):
                self.occupied_cells[(start_x, i)] = 0
        #attempted diagonal orientation
        else: 
            raise Exception('Invalid arrangement of the piece.') 



    def hit(self, cell):
        '''
        This method indicates that the cell has been hit by setting the value at the
        corresponding key of self.occupied_cells to 'H'. This method also increments
        self.hit_cells by 1 to indicate that a cell occupied by the piece has been
        hit
        
        Args:
            cell: tuple of board coordinates
        
        Preconditions: 
            the cell that the opponent has fired at is a hit
        
        '''
        self.occupied_cells[cell] = 'H'
        self.hit_cells += 1
    
    def is_sunk(self):
        '''
        This method returns true if all cells that the piece occupies have been hit; 
        otherwise, return false. 
        
        Returns: boolean
        '''
        if self.hit_cells == len(self.occupied_cells):
            return True
        return False


class Carrier(Piece):
    '''
    subclass of Piece
    
    size specification: 5
    
    additional instance variables:
        ID number: 5
        name: carrier
    '''    


    def __init__(self, start, end, size = 5):
        '''
        Same method as super class __init__(start, end) method
        
        additional functions:
            set the following variables:
                ID = 5
                name = 'carrier'
            throw exception: if the start and end coordinates do not form
                                        a piece of size 5
        
        Args: 
            start: tuple with board coordinates
            end: tuple with board coordinates
        '''
        self.ID = 5
        self.name = 'carrier'

        super(Carrier, self).__init__(start, end, size)
    

class Battleship(Piece):
    '''
    subclass of Piece
    
    size specification: 4
    
    additional instance variables:
        ID number: 4
        name: battleship
    '''   

    def __init__(self, start, end, size = 4):
        '''  
        Same method as super class __init__(start, end) method
        
        additional functions:
            set the following variables:
                ID = 4
                name = 'battleship'
            throw exception: if the start and end coordinates do not form
                             a piece of size 4
        Args: 
            start: tuple with board coordinates
            end: tuple with board coordinates
        '''
        self.ID = 4
        self.name = 'battleship'
     
        super(Battleship, self).__init__(start, end, size)

       
class Submarine(Piece):
    '''
    subclass of Piece
    
    size specification: 3
    
    additional instance variables:
        ID number: 3
        name: submarine
    '''   
    
    def __init__(self, start, end, size = 3):
        '''
        Same method as super class __init__(start, end) method
        
        additional functions:
            set the following variables:
                ID = 3
                name = 'submarine'
            throw exception: if the start and end coordinates do not form
                             a piece of size 3
        
        Args: 
            start: tuple with board coordinates
            end: tuple with board coordinates
        
        '''
        self.ID = 3
        self.name = 'submarine'

        super(Submarine, self).__init__(start, end, size)

   
class Cruiser(Piece):
    '''
    subclass of Piece
    
    size specification: 2
    
    additional instance variables:
        ID number: 2
        name: 'cruiser'
    '''     

    def __init__(self, start, end, size = 2):
        '''    
        Same method as super class __init__(start, end) method
        
        additional functions:
            set the following variables:
                ID = 2
                name = 'cruiser'
            throw exception: if the start and end coordinates do not form
                             a piece of size 2
        
        Args: 
            start: tuple with board coordinates
            end: tuple with board coordinates
        '''
        self.ID = 2
        self.name = 'cruiser'
         
        super(Cruiser, self).__init__(start, end, size)

            
class Destroyer(Piece):
    '''
    subclass of Piece
    
    size specification: 2
    
    additional instance variables:
        ID number: 1
        name: 'destroyer'
    '''    

    def __init__(self, start, end, size = 2):
        '''
        Same method as super class __init__(start, end) method
        
        additional functions:
            set the following variables:
                ID = 1
                name = 'destroyer'
            throw exception: if the start and end coordinates do not form
                             a piece of size 2
        Args: 
            start: tuple with board coordinates
            end: tuple with board coordinates
        
        '''
        self.ID = 1
        self.name = 'destroyer'
                
        super(Destroyer, self).__init__(start, end, size)


class PersonalBoard(object):
    '''
    PersonalBoard represents each player's game board as a 10X10 matrix and keeps
    track of all the pieces in the game, where the pieces are in the board, what
    board cells have been attacked (denoted by 'M' for miss, 'H' for hit, and 
    'S' for sunk), and number of ships that have been sunk. 
    ''' 
    
    def __init__(self):
        '''    
        Initialize a PersonalBoard object with the following instance variables:
            self.board: 10x10 matrix with default values set to 0
            self.pieces: dictionary where keys are piece names and values are the
                         corresponding Piece objects on the board
            self.sunk_ships: number of ships sunk on the board
        '''
        self.board = [[0 for x in range(10)] for y in range(10)]
        self.pieces = {}
        self.sunk_ships = 0
    

    def place_piece(self, start, end, name):
        ''' 
        This function adds a Piece (as specified by the name parameter)
        to self.pieces where the key is the name of the ship and the value is the 
        Piece, and places the Piece on the PersonalBoard by filling the cells the
        Piece occupies of self.board with the ID number of the Piece. 
        
        Args:
            start: tuple with board coordinates
            end: tuple with board coordinates
            name: the name of the Piece
        
        Exceptions:
            if any of the cells that the Piece occupies is out of bounds
            if any of the cells that the Piece occupies overlaps with another Piece
        '''
        ship = None
        if name == 'destroyer':
            ship = Destroyer(start, end, 2)
        elif name == 'cruiser':
            ship = Cruiser(start, end, 2)
        elif name == 'submarine':
            ship = Submarine(start, end, 3)
        elif name == 'battleship': 
            ship = Battleship(start, end, 4)
        elif name == 'carrier':
            ship = Carrier(start, end, 5)

        #store into instance variable
        self.pieces[name] = ship
        #place the ship on the board and throw exceptions for illegal placements
        for cell in ship.occupied_cells:
            x = cell[0]
            y = cell[1]
            if x < 0 or x >= 10 or y < 0 or y >= 10:
                raise Exception('Entered numbers are out of bounds.')
            if self.board[x][y] != 0:
                raise Exception('Illegal overlapping of ships.')
            self.board[x][y] = ship.ID
    

    def opponent_move(self, cell, ships):
        '''
        This method generates a response after the opponent has attacked a 
        specificed cell on the PersonalBoard. If the board cell has value 0 it 
        means that there is no ship on that board cell, so 'miss' is returned and
        the board cell is marked with a 'M'. If the board cell has a 'S', 'M', or
        'H', an exception is raised since that board cell has already been 
        attacked before. Otherwise, the board cell contains a nonzero number that
        is the ID of a Piece on the PersonalBoard, so the ship with that ID has been
        hit. This method then checks to see if that hit has caused the ship to sink,
        in which case all of the occupied cells of the ship are marked with S,
        the number of sunk ships increments by 1, and 'sunk: ' + (name of the ship) 
        is returned. Otherwise, the ship doesn't sink and the board cell is marked
        with a 'H' and 'hit' is returned. 
     
        Args:
            cells: tuple with board coordinates
            ships: list of names of the Pieces on the board
           
        Exceptions:
            if the cell being attacked is out of bounds
            if the cell being attacked has been attacked before
            
        Returns: string
        '''
        x = cell[0]
        y = cell[1]
        #attacked cell is out of bounds
        if x < 0 or x >= 10 or y < 0 or y >= 10:
            raise Exception('Entered numbers are out of bounds.')
        
        ID = self.board[x][y]
        #miss
        if ID == 0:
            self.board[x][y] = 'M'
            return 'miss' 
        #attacked cell already attacked
        elif ID == 'S'or ID == 'M' or ID == 'H':
            raise Exception('Already attacked that square.')
        #hit or sunk
        else:
            name = ships[ID]            
            self.pieces[name].hit(cell)
            ship = self.pieces[name]
            #check if the ship is sunk
            if ship.is_sunk():
                self.sunk_ships += 1                
                for cell in ship.occupied_cells:
                    x = cell[0]
                    y = cell[1]
                    self.board[x][y] = 'S'
                return 'sunk: ' + name
            #otherwise, ship has been hit and not sunk
            self.board[x][y] = 'H'
            return 'hit'
    

    def game_over(self):
        '''
        This method checks if the game is over by comparing the number of
        sunk ships with the number of pieces initially placed on the board.
        
        Returns: boolean
        '''
        if self.sunk_ships == len(self.pieces):
            return True
        return False


class BattleShip(object):
    '''
    Battleship executes the game by prompting players to enter input, processing 
    the input, outputting feedback (e.g. displaying a player's personal board and the 
    opponent's board), and ending the game when all of the ships of 
    a player have sunk. 
    '''
    
    def __init__(self):
        '''
        This initializes two PersonalBoards, one for player 1 and the other for
        player 2
        '''
        self.player1 = PersonalBoard()
        self.player2 = PersonalBoard()
    

    def print_board(self, board):
        ''' 
        This method prints the board of a player to reveal where all the ships
        have been placed and what cells have been missed, hit, or sunk.
        
        Args:
            board: a matrix to print
        '''
        for i in range(10):
            row = ''
            for j in range(10):
                row += str(board[i][j])
                row += '     '
            print(row)
    

    def print_board_opp_pov(self, board):
        '''
        This method prints the board from the point of view of the opponent. Ship
        locations are not revealed since the ID numbers are printed as zeros but
        cells that have been missed, hit, or sunk are displayed. 
    
        Args:
            board: a matrix to print
        '''
        for i in range(10):
            row = ''
            for j in range(10):
                val = board[i][j]
                if val == 0 or val == 'M'  or val == 'H' or val == 'S':
                    row += str(board[i][j])
                else:
                    row += str(0)
                row += '     '
            print(row)
        print('\n')
    

    def collect_input(self, player, ships):
        '''
        This method iterates through all the types of ships, collects user 
        input on the rows and columns of the start and endpoints of each 
        ship, calls the place_piece function to put the ship on the board, and
        calls the print_board function to show the current state of the board
        and where the pieces are located. 
        
        Args:
            player: a PersonalBoard object
            ships: list of names of the Pieces on the board
        '''
        for ID in range(1,len(ships)):
            #collect user input to place the ships on the board
            name = ships[ID]
            print(name.upper() + ' start point:')
            start_x = input('row: ')
            start_y = input('col: ')
            print('\n')
            print(name.upper() + ' end point: ')
            end_x = input('row: ')
            end_y = input('col: ')
            
            #place piece on board
            start = (int(start_x), int(start_y))
            end = (int(end_x), int(end_y))
            player.place_piece(start, end, name)

            #display current state of board and where the pieces are located
            print('\n')
            self.print_board(player.board)        
            print('\n')
    

    def __main__(self):
        '''
        This method executes the game and is user-interactive. It is split into four
        parts
        
        (1) default settings
            An array of ship names is initiazlied and indexed by 1.
        (2) user input for ship placement
            Both players are prompted to place their ships on their boards and the 
            collect_input function is called
        (3) game play
            The game keeps running until one player sinks all the ships of another 
            player. An index that is incremented with each player's turn keeps
            track of whose turn it is (even --> player 1, odd --> player 2). A
            player's turn doesn't end until they miss when they attack. At each 
            turn, a player can choose the following functions
                attack: collects user input on which board cell to attack and calls
                        the opponent_move function
                personal_board: displays the player's own board by calling print_board
                opponent_board: displays opponent's board with hidden ship locations
                                by calling print_board_opp_pov
                quit: quits the game and returns 'Game over' 
                
        (4) game is over
            The player who has won the game is displayed. 
        '''    
        #part (1)
        ships = ['', 'destroyer', 'cruiser', 'submarine', 'battleship', 'carrier']
        
        #part (2)
        print('Player 1 please enter the locations of your ships. The start and \
        end points are inclusive. \n')
        self.collect_input(self.player1, ships)
        print('Player 2 please enter the locations of your ships. The start and \
        end points are inclusive. \n')
        self.collect_input(self.player2, ships)
        
        #part(3)
        index = 0 #keeps track of whose turn: even, player 1; odd, player 2
        while(not self.player1.game_over() and not self.player2.game_over()):
            #indicate whose turn it is            
            if index%2 == 0:
                print('Player 1 move. \n')
            elif index%2 == 1:
                print('Player 2 move. \n')
            #allow the player to attack, display their own board, display their
            #opponent's board, or quit the game
            answer = input('attack    personal_board    opponent_board    quit: ')
            while answer != 'attack': 
                print('\n')
                #quit the game 
                if answer == 'quit':
                    print('Game over')
                    return 
                #display the player's own board
                elif answer == 'personal_board':
                    if index%2 == 0:
                        self.print_board(self.player1.board)
                    elif index%2 == 1:
                        self.print_board(self.player2.board)
                #display the opponent's board
                elif answer == 'opponent_board':
                    if index%2 == 0:
                        self.print_board_opp_pov(self.player2.board)
                    elif index%2 == 1:
                        self.print_board_opp_pov(self.player1.board)
                print('\n')
                answer = input('attack    personal_board    opponent_board    quit: ')
            #attack a board cell on the opponent's board
            result = ''
            if answer == 'attack':
                print('Enter attack location.')
                x = int(input('x_coord: '))
                y = int(input('y_coord: '))           
                print('\n')
                if index%2 == 0:
                    result = self.player2.opponent_move((x,y), ships) + '\n'
                    print(result)
                elif index%2 == 1:
                    result = self.player1.opponent_move((x,y), ships) + '\n'
                    print(result)
            #increment index to keep track of whose turn it is              
            if 'hit' in result or 'sunk' in result:
                index += 2
            else:
                index += 1
        
        #part (4)
        if self.player1.game_over():
            print('Game over: Player 2 wins!')
        elif self.player2.game_over():
            print('Game over: Player 1 wins!')
        