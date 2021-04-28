import os

import argparse
import json

def main():
    if not os.path.exists("storage.data"):
        data = {}
        with open("storage.data", "w") as write_file: #create file storage.data
            json.dump(data, write_file)

    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")
    args = parser.parse_args()

    if args.val == None:
        read_key(args.key)
    else:
        write_key(args.key, args.val)



def write_key(key, value):
    with open("storage.data", "r") as read_file:
        data = json.load(read_file)

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open("storage.data", "w") as write_file:
        json.dump(data, write_file)

def read_key(key):
    with open("storage.data", "r") as read_file:
        data = json.load(read_file)
    if key in data:
        return print(*data[key], sep=', ')
    else:
        return print(None)


if __name__ == '__main__':
    main()


