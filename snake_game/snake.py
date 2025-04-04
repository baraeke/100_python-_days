from turtle import Turtle 

# Constants for movement
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Represents the snake in the game."""

    def __init__(self):
        """Initialize the snake with three segments and set the head."""
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """Creates the initial snake with three segments."""
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_part(position)

    def add_part(self, position):
        """Adds a new segment to the snake at the given position."""
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake.append(new_snake)

    def reset(self):
        """Resets the snake to its initial position and removes old segments."""
        for segment in self.snake:
            segment.goto(1000, 1000)  # Move old segments out of the screen
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        """Adds a new segment to the snake."""
        self.add_part(self.snake[-1].position())

    def move(self):
        """Moves the snake forward."""
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            self.snake[snake_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    # Movement controls
    def up(self):
        """Move the snake up (if not already moving down)."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move the snake down (if not already moving up)."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the snake left (if not already moving right)."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the snake right (if not already moving left)."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
