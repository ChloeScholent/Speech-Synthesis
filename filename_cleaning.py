#Cleaning the recording data by suppressing number of takes.

import os

#Open folder
folder = r'C:\Users\Chloé\Desktop\chloe arctica\\'

#Determine the string to be renamed
for file_name in os.listdir(folder):
    source = folder + file_name
    destination = file_name.replace("_1", "") 

    os.rename(source, destination)
 





