#Author Brandon Noecker
#Date: 4/15/2021
#Purpose: This program is to replace all newline characters in a txt file with spaces and save it in the original file.

import os

def main():
    #Prompt the user for the file name
    filename = "Job-Desc-Hiding/description.txt"

    #Open the file
    infile = open(filename, 'r')
    data = infile.read()
    infile.close()

    #Replace all newline characters with spaces
    data = data.replace('\n', ' ')
    
    #Open the file again and write the data to it
    outfile = open(filename, 'w')
    outfile.write(data)
    outfile.close()

    print("The new data has been written to the file.")

main()
