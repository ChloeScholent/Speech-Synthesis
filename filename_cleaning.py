#Cleaning the recording data by suppressing the number of takes.

import os

folder = "path_to_file"

for file_name in os.listdir(folder):
    source = folder + file_name
    destination = file_name.replace("_1", "") 
    os.rename(source, destination)
 





