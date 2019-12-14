from os import listdir
from os.path import isfile, join

def main():
    directory_address = "dump"
    dump = [f for f in listdir(directory_address) if isfile(join(directory_address, f))]

    for dump_file in dump:
        print(dump_file)


if __name__ == "__main__":
    main()
