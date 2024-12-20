class read_line:
    #Reads the latest 
    def read_lines_until_string(file_path, target_string):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        result = []
        for line in reversed(lines):
            result.append(line.strip())
            if target_string in line:
                break

        return list(reversed(result))
    
    def remove_empty_strings(input_list):
        filtered_list = [] 
        for string in input_list: 
            if string: # This condition checks if the string is not empty
                filtered_list.append(string)
        
        return filtered_list