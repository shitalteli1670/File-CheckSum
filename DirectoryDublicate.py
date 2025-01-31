# Problem Statements : Design automation script which accept diectory name and write names of dublicate files from that directory. write names
# into log file named as Log.txt. Log.txt file should be created into current directory.

# Usage : DirectoryDublicate.py "Test"

from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def FindDublicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for DirName, SubDir, fileList in os.walk(path):
            print('\n--------------------------------------------------------------------')

            for filen in fileList:
                path = os.path.join(DirName,filen)
                FileHash = hashfile(path)
                if FileHash in dups:
                    dups[FileHash].append(path)
                else:
                    dups[FileHash] = [path]
        return dups
    else:
        print("Invalid path...")

def PrintDublicate(dict1):
    results = list(filter(lambda x:len(x)>1, dict1.values()))

    if len(results) > 0:
        print("Dublicate Found : ")
        print("The folowing file are identical.")

        iCnt = 0
        for result in results:
            for subresult in result:
                iCnt = iCnt + 1
                if iCnt >= 2:
                    print('\t\t%s' %subresult)
    else:
        print("No dublicate file found...")

def main():
    print('--------------------------------------------------------------------')
    print("Created by Shital Teli")
    print("Application name:" +argv[0])
    print('--------------------------------------------------------------------')

if (len(argv) != 2):
    print("Error: Invalid number of arguments")
    exit()

if (argv[1] == "-h") or (argv[1] == "-H"):
    print("This Script is used to traverse specific directory and display sizes of files")
    exit()

if (argv[1] == "-u") or (argv[1] == "-U"): 
    print("usage: ApplicationName AbsolutePath_of_Directory ")
    exit()

try:
    arr = {}
    arr = FindDublicate(argv [1])
    PrintDublicate(arr)

except ValueError:
    print("Error: Invalid datatype of input")

except Exception as E:
    print("Error: Invalid input",E)

if __name__ =="__main__":
    main()