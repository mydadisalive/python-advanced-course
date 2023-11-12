import sys
import os

# this script gets an argument directory, runs over the directory and moves files to either Text or Images folder based on the extension

args = sys.argv
# check arg numbers
if len(args) != 2:
    print("bad number of arguments")
    sys.exit(1)
    
# check argument dir
if not os.path.exists(args[1]):
    print("bad directory")
    sys.exit(1)


# MAIN
# run over the files in dir and move them to the relevant folders