# FoCar - Mirror S Route - Assignment 5.4
# Student: Wasantha Wanniarachchi
import turtle
import time

def read_instructions(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def drive_focar():
    screen = turtle.Screen()
    screen.title("FoCar Mirror S")
    car = turtle.Turtle()
    car.shape("square")
    car.pensize(3)
    instructions = read_instructions("route.txt")
    for cmd in instructions:
        parts = cmd.split()
        if len(parts) < 2:
            continue
        action = parts[0]
        value = int(parts[1])
        if action == "FORWARD":
            car.forward(value)
        elif action == "LEFT":
            car.left(value)
        elif action == "RIGHT":
            car.right(value)
    time.sleep(2)
    screen.bye()
    print("FoCar finished mirror S route!")

if __name__ == "__main__":
    drive_focar()
