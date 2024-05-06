class MazeRunner:
    def __init__(self):
        self.cords = ()
        self.facing = ''

    def set_cords(self, maze):
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == 'H':
                    self.cords = (i, j)

    def set_facing(self, maze):
        if maze[self.cords[0] + 1][self.cords[1]] == '-':
            self.facing = 'south'
            return

        if maze[self.cords[0] - 1][self.cords[1]] == '-':
            self.facing = 'north'
            return

        if maze[self.cords[0]][self.cords[1] + 1] == '-':
            self.facing = 'east'
            return

        if maze[self.cords[0]][self.cords[1] - 1] == '-':
            self.facing = 'west'
            return



class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.maze_runner = MazeRunner()

    def solveMaze(self):
        self.maze_runner.set_cords(self.maze)
        self.maze_runner.set_facing(self.maze)

        