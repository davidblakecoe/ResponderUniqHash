#!/usr/bin/env python3

#Set the script as executable using the 'chmod +x ResponderUniqHash.py' command
#Run the script by running './RepsonderUniqHash.py'

#Import sys library to access command line arguements
import sys

#Check to ensure that the proper command line usage is performed
if (len(sys.argv)) < 2:
    print("Too few commandline arguements")
    print("Usage:  ./UniqHash [HashFileName]")
    print("Pipe the output into a file by using:  ./UniqHash [HashFileName] > [OutputFile]")
    exit()

#Take command line arguement arv[1] and use it as the file to open
FileToOpen = (str(sys.argv[1]))

#Read the hash file
HashFile = open(FileToOpen, "r")

#Declare List
List = []
UniqUserHash = []
#Read each line of file and pull the Username and Domain Name
for Hash in HashFile.readlines():
    #Split the HashFile up using ":" as a delimeter
    Uniq = Hash.split(":")
    #Pull the unique Username and Domain Name
    if (Uniq[0]+"::"+Uniq[2]) not in List:
        #Store the uniq Username and Domain in a List
        List += [Uniq[0]+"::"+Uniq[2]]
        #For each unique Username and Domain Name in List store the entire hash results
        UniqUserHash += [Uniq[0]+"::"+Uniq[2]+":"+Uniq[3]+":"+Uniq[4]+":"+Uniq[5]]
#print the first hash for each unique Username and Domain combination
#* prints a list without a loop & sep="\n" prints one hash per line
print(*UniqUserHash, sep='\n')
#Close hashfile
HashFile.close()
