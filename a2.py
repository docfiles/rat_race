# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.



WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'




class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.

    def __init__(self, symbol, row, col) -> None:
        """ (Rat,str,int,int) -> NoneType
        Creates a rat with an instance variables 
        >>> rat = Rat('P', 2, 2)
        >>> rat.symbol
        'P'
        >>> rat.row
        2
        >>> rat.col
        2
        >>> rat.num_sprouts_eaten
        0
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def __str__(self) -> str:
        """ (Rat) -> str
        Returns a string representation of the rat
        >>> rat = Rat('P', 2, 2)
        >>> print(rat)
        P at (2, 2) ate 0 sprouts.
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
    


    def set_location(self, row, col) -> None:
        """ (Rat,int,int) -> NoneType
        Set the rat's row and col instance 
        variables to the given row and column
        >>> rat = Rat('P', 2, 2)
        >>> rat.set_location(4, 4)
        >>> rat.row
        4
        >>> rat.col
        4
        """
        self.row = row
        self.col = col

    def eat_sprout(self) -> None:
        """ (Rat) -> NoneType
        Add one to the rat's instance variable
        >>> rat = Rat('P', 2, 2)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1
    


class Maze:
    """ A 2D maze. """
    

    def __init__(self, contents, rat_1, rat_2) -> None:
        """ (Maze, list of list of str, Rat, Rat) -> NoneType
        Creates a maze with an instance variables
        >>> maze = Maze(contents_main, Rat('J', 1, 1), Rat('P', 1, 4))
        >>> print(maze.rat_1)
        J at (1, 1) ate 0 sprouts.
        >>> print(maze.rat_2)
        P at (1, 4) ate 0 sprouts.
        """
        self.maze = contents
        self.maze[rat_1.row][rat_1.col] = rat_1.symbol
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol
        
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = self.sprout_count(contents)
        

    def __str__(self) -> str:
        """ (Maze) -> str
        Returns a string representation of the maze
        """
    
        superstr = substr ='' 

        for lst in self.maze:
            for i in lst:
                substr = substr + i
            superstr = superstr + substr + '\n'
            substr = ''

        return superstr + str(self.rat_1) + '\n' + str(self.rat_2)


    def sprout_count(self, contents) -> int:
        """ (Maze, list of list of str) -> int
        Counts a number of sprouts (@) left in contents
        >>> maze = Maze(contents_main, Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze.num_sprouts_left
        3
        """
        counter = 0

        for lst in contents:
            for i in lst:
                if i == SPROUT:
                    counter += 1
        return counter


    def is_wall(self, row, col) -> bool:
        """ (Maze, int, int) -> bool
        Return True if and only if there is a wall at the given 
        row and column of the maze.
        >>> maze = Maze(contents_main, Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze.is_wall(1, 1)
        False
        >>> maze.is_wall(0, 0)
        True
        >>> maze.is_wall(0, 1)
        True
        """
        if self.maze[row][col] == WALL:
            return True
        else:
            return False



    def get_character(self, row, col):
        """ (Maze, int, int)
        Return the character in the maze at the given row and column. 
        If there is a rat at that location, then its character should be returned
        rather than HALL.
        >>> maze = Maze(contents_main, Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze.get_character(1, 1)
        'J'
        >>> maze.get_character(1, 0)
        '#'
        >>> maze.get_character(2, 1)
        '.'
        >>> maze.get_character(4, 1)
        '@'
        """
        if row == self.rat_1.row and col == self.rat_1.col:
            return self.rat_1.symbol
        if row == self.rat_2.row and col == self.rat_2.col:
            return self.rat_2.symbol

        character = self.maze[row][col]
        return character

    def wall_stop(self, some_rat, vertic, horizon) -> bool:
        """ (Maze, Rat, int, int) - > bool
        Check the future position of the rat, return True 
        if it's going to hit the wall 
        """
        col = some_rat.col + horizon
        row = some_rat.row + vertic

        if self.is_wall(row, col) is True:
            return True
        else:
            return False
        
    
    def move_analyze(self, vertic, horizon) -> int:
        """(Maze, int, int) -> int
        Checks weather both coordinates are not equal to 
        zero, returns more than 1 if it is
        """
        factor = 0
        if vertic == NO_CHANGE:
            factor += 1
        if horizon == NO_CHANGE:
            factor += 1
        
        return factor

    def haller(self, some_rat) -> None:
        """(Maze, Rat) -> NoneType
        Check weather other player on this spot or not,
        if it is do not leave a HALL after moving
        """
        r1_position = [self.rat_1.col, self.rat_1.row]
        r2_position = [self.rat_2.col, self.rat_2.row]

        if r1_position != r2_position:
            self.maze[some_rat.row][some_rat.col] = HALL
        
        else:
            if some_rat.symbol == RAT_1_CHAR:
                self.maze[some_rat.row][some_rat.col] = RAT_2_CHAR
            if some_rat.symbol == RAT_2_CHAR:
                self.maze[some_rat.row][some_rat.col] = RAT_1_CHAR



    def move(self, some_rat, vertic, horizon) -> bool:
        """ (Maze, Rat, int, int) -> bool
        Move the rat in the given direction, unless there is a wall 
        in the way. Also, check for a Brussels sprout at that 
        location and eat it, etc..
        """

        if self.wall_stop(some_rat, vertic, horizon) is False:
            
            if self.move_analyze(vertic, horizon) < 2:
                self.haller(some_rat)
                row = some_rat.row + vertic
                col = some_rat.col + horizon
                if self.get_character(row, col) == SPROUT:
                    some_rat.eat_sprout()
                    self.num_sprouts_left -= 1
                some_rat.row += vertic
                some_rat.col += horizon

                

                self.maze[some_rat.row][some_rat.col] = some_rat.symbol




            return True
        
        else:
            return False

# maze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
#              ['#', '.', '.', '.', '.', '.', '#'], 
#              ['#', '.', '#', '#', '#', '.', '#'], 
#              ['#', '.', '.', '@', '#', '.', '#'], 
#              ['#', '@', '#', '.', '@', '.', '#'], 
#              ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1), Rat('P', 1, 4))

        

         
