
def read_input(input_file):
    with open(input_file, 'r') as file:
        return [line.strip() for line in file.readlines()]

def new_position(position, direction, rotation):
    zero = 0
    
    if direction == "L":
        position = position - rotation

        while position <= -1:
            position = position + 100
    
    else:
        position = position + rotation
        
        while position >= 100:
            position = position - 100

    print(position)
    
    if position == 0:
        zero += 1
    
    return position, zero

def main():
    total_zero = 0
    input_file = "input.txt"
    lines = read_input(input_file)
    
    position = 50
    
    for i, line in enumerate(lines):
        direction = line[0]
        rotation = line[1:]
        
        position, zeros = new_position(position, direction, int(rotation))
        
        if zeros:
            total_zero += zeros
    

    
    print(f"TOTAL ZEROS: {total_zero}")
        
        
if __name__ == "__main__":
    main()