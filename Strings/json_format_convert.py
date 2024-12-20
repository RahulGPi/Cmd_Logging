from log_file.Read_Cmds.readline_1 import read_line as rd
from datetime import date
from api.api import api
# D:\GlobalStoragePro\Python WorkSpace\Cmd_logging\log_file\Read_Cmds\readline_1.py
class convert:
    
    def conversion_to_json():
        log_file_path = "path file -> cmd_commands.log"
        
        date_now = date.today()
        target_string = date_now.strftime("%d-%m-%Y")
        
        lines = rd.read_lines_until_string(log_file_path, target_string)
        # String to send
        lines = '\n'.join(lines)

        response = api.combine(lines)
        # Collects response from api, returns list on '\n' , removes '\n' values in the returned list 
        returned_api_list = response.text.split('\n')
        print(lines[:22])
        cleaned_list = []
        for line in returned_api_list:
            cleaned_list.append(line)

        cleaned_list = rd.remove_empty_strings(cleaned_list)
        
        return lines, cleaned_list