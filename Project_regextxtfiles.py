import os
import re
shiplines = []

# regex for text between "arrived" and "cleared", ignoring case
pattern = re.compile('/(?=arrived)(.+?)(?=cleared)/gmis')

# folder path
path = 'C:/Users/Michelle/Desktop/artworksmuseum/chronam/sn83030313/'
  
# Change the directory
os.chdir(path)
  
# read text File
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_lines:

        for line in file_lines:
            if pattern.search(line) != None:
                shiplines.append(line.rstrip('\n'))

    for shipname in shiplines:
        
        print(shipname[1])
  
# iterate through all text files
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
  
        # call read text file function for path
        read_text_file(file_path)

