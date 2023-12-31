import os
import re
import datetime
import configparser
import argparse

def autodate():
    # Get current date in format of YYYY-MM-DD
    date = datetime.date.today().strftime('%Y-%m-%d')
    return date

def slugify(title: str):
    # Remove special characters and convert spaces to hyphens
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', title).strip().lower().replace(' ', '-')
    return slug 

def config_parser(config_file:str, data:dict):
    if config_file == "":
        pass
    
    else:
        # Read config ini file and convert into dict 
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(config_file)

        #Loop through each key-value pair in the section and add it to the dictionary
        for section in config.sections():
            for key, value in config[section].items():
                data[key] = value

def arg_parser(data: dict):
    # Initiate parser object
    parser = argparse.ArgumentParser(description="Update default setup value thru commandline")
    
    # Loop thru main dict and create arg
    for key, value in data.items():
        parser.add_argument(f"--{key}", help=f"Overwrite the '{key}' from config setup file", default=value)

    # Create parser object with values
    args = parser.parse_args()
    
    # Object to dict and loop thru to replace value
    for key, value in vars(args).items():
        if data[key] != value:
            data[key] = value
            print(f"Updated {key} to {value}")

def config_path():
    # Check if current config.ini exist in cwd
    pwd_path = ("config.ini")

    if os.path.exists(pwd_path) == True:
        print("Using configuration config.ini from current path")
        return pwd_path
    
    else:
        print("Configuration config.ini not in current dir, skip")
        return ""
    
def save_to_file(filename:str, data: dict):
    # Initialize metadata content with opening hypens
    content = "---\n"

    for key, value in data.items():
        # Append each key value to content
        content = f"{content}{key}: {value}\n"

    content = f"{content}---\n\nStart writing here.."

    # Open and write up the file
    with open(filename, 'w') as file:
        file.write(content)

def main():
    # Create minimum dict with compulsory metadata
    main_dict = {
        "title": "",
        "date": autodate()
    }

    # Update the dict with options metadata
    config_parser(config_path(), main_dict)

    # Argparser for replacing default value
    arg_parser(main_dict)


    # User input if still empty
    for key in main_dict.keys():
        while main_dict[key] == "":
            main_dict[key] = input(f"Enter {key} for this post: ")
            if main_dict[key] == "":
                print(f"Input for {key} can't be empty no default set in config.ini or commandline")

    # Create the output markdown file
    filename = f"{main_dict['date']}-{slugify(main_dict['title'])}.md"

    save_to_file(filename, main_dict)

    print(main_dict)

if __name__ == "__main__":
    main()
