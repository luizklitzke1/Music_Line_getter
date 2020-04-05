def read_lines(name):

    print(f"musics/{name}.txt", "r")
    with open(f"musics/{name}.txt", "r") as file:  
        lines_array = file.readlines()
    return lines_array

def print_lines(array):
    for line in array:
        print(line)
        
if __name__ == "__main__": 
    
    array = read_lines("murder_one")
    print_lines(array)
    
    