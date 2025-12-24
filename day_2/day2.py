def read_input(input_file):
    data = []
    with open(input_file, 'r') as file:
        content = file.read()
        
    for item in content.split(','):
        item = item.strip()
        data.append(item)
        
    return data

def parse_data(data):
    parsed_data = {}
    for i, d in enumerate(data):
        split_data = d.split('-')
        lower_range = split_data[0]
        upper_range = split_data[1]
        
        parsed_data[i] = {}
        parsed_data[i]['lower'] = int(lower_range)
        parsed_data[i]['upper'] = int(upper_range)
    
    return parsed_data

def invalid_check(lower, upper):
    
    invalid = 0
    for x in range(lower, upper + 1):
        
        string = str(x)
        
        is_invalid = string in (string + string)[1:-1]
        
        if(is_invalid == True):
            invalid += x
            
    return invalid
   
     
        
def main():
    input_file = "input.txt"
    invalid_id = 0
    
    data = read_input(input_file)
    
    parsed_data = parse_data(data)
        
    for i, bounds in parsed_data.items():
        lower = bounds['lower']
        upper = bounds['upper']

        invalid = invalid_check(lower, upper)
        
        invalid_id += invalid
        
    print(invalid_id)
 
     
        
    
if __name__ == "__main__":
    main()