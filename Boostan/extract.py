from os import listdir
from os.path import isfile, join

directory_address = "dump"
dump = [f for f in listdir(directory_address) if isfile(join(directory_address, f))]

print(dump)
