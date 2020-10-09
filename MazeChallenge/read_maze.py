"""
This challenge is to print to screen the output of challenge_maze.txt to look like:
[' ', ' ', '*', ' ']
[' ', ' ', ' ', ' ']
[' ', '*', ' ', '*']
[' ', ' ', ' ', ' ']

"""

def read_maze(file_name):
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            nums_col_top_row = len(maze[0])
            for row in maze:
                if len(row) != nums_col_top_row:
                    print("The maze is not rectengular.")
                    raise SystemError
            return maze 
    except OSError:
        print("There is a problem with the file you have selected")
        raise SystemExit

if __name__ == "__main__":
    maze = read_maze("mazes/challenge_maze.txt")
    for row in maze:
        print(row)