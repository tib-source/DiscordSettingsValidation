#!/usr/bin/env python3

import plyvel
import argparse

def main():
    # Creating argument parser
    parser = argparse.ArgumentParser(description="A simple Python script that takes a file path as input.")
    
    # Adding arguments
    parser.add_argument("--file-path", help="Path to the leveldb file", required=True)
    parser.add_argument("--name", help="Name of output", required=True)
    
    # Parsing arguments
    args = parser.parse_args()
    
    # Accessing the file path argument
    file_path = args.file_path
    name = args.name
    
    # Print the file path
    print("File path provided:", file_path)
    
    getMediaJson(file_path, name)

def getMediaJson(db_path, name): 
    # Open the LevelDB database folder
    with open(f'./files/db_output/{name}.json', 'w', newline='', encoding='utf-8') as jsonFile:
        # Open the LevelDB database
        db = plyvel.DB(db_path, create_if_missing=False)
        
        for key, value in db:

            try:
                key_str =  key
                value_str =  value
            except UnicodeDecodeError:
                continue  # Skip this entry
            if b'MediaEngineStore' in key_str: 
                json_string = value_str.decode('utf-8', 'ignore')
                cleaned_json_string = json_string.lstrip(b"b'\x01".decode())
                jsonFile.write(f"{cleaned_json_string}")
                db.close()
                break
        db.close()
    jsonFile.close()

if __name__ == "__main__":
    main()