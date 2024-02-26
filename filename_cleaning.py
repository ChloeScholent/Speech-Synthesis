#Cleaning the recording data by suppressing the number of takes.

import os

folder = r'C:\Users\Chloé\Desktop\chloe arctica\\'

for file_name in os.listdir(folder):
    source = folder + file_name
    destination = file_name.replace("_1", "") 
    os.rename(source, destination)
 





