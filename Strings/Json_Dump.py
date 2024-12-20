import os
import json

class jason:
    file_path = "path file -> return_prompts.json"

    # Initialize JSON file if it doesn't exist or is empty
    @classmethod
    def FilePut(cls, lines:list, cleaned_list:list):
        if not os.path.exists(cls.file_path) or os.path.getsize(cls.file_path) == 0:
            with open(cls.file_path, 'w') as json_file:
                json.dump({}, json_file)

        # Reading data from the JSON file 
        with open(cls.file_path, 'r') as json_file:
            prompts = json.load(json_file)

        date = lines[:22]
        # date = datetime.datetime.strptime(date, "%d-%m-%Y %H:%M:%S.%f")
        
        prompts[date] = {
            cleaned_list[0] : cleaned_list[1]
        }
        # Writing updated data to the JSON file 
        with open(cls.file_path, 'w') as json_file: 
            json.dump(prompts, json_file, indent=4)