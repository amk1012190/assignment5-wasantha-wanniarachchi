# FoCar - Mirror S Route - Assignment 5.4
# Student: Wasantha Wanniarachchi

def read_instructions(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return []

def drive_focar():
    print("FoCar starting - Mirror S route")
    instructions = read_instructions("route.txt")
    
    for line in instructions:
        line = line.strip()
        if not line:
            continue
        print(f"Executing: {line}")

    print("FoCar finished mirror S route!")

if __name__ == "__main__":
    drive_focar()

