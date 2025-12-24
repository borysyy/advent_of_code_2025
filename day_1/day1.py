from utils import read_input

def new_position(position, direction, rotation):
    zero = 0
    
    if direction == "L":
        if position == 0:
            position = 100

        position = position - rotation
        while position <= -1:
            position = position + 100
            zero += 1
   
    else:
        position = position + rotation
        while position > 100:
            position = position - 100
            zero += 1
            
    if position == 100:
        position = 0
    
    if position == 0:
        zero += 1
        
    return position, zero

def main():
    total_zero = 0
    input_file = "input.txt"
    lines = read_input(input_file)
    
    position = 50
    
    for line in lines:
        direction = line[0]
        rotation = line[1:]
        
        position, zeros = new_position(position, direction, int(rotation))
        
        if zeros:
            total_zero += zeros
    

    
    print(f"TOTAL ZEROS: {total_zero}")
        
        
if __name__ == "__main__":
    main()