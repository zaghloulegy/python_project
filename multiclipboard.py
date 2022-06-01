import sys
import clipboard
import json


file = "clipboard.json"

def save_data(filepath,data):
    with open(filepath,'w') as f:
        json.dump(data,f)


def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(file)



    if command == 'save':
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(file,data)
        print("Saved to clipboard")


    elif command == 'load':
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Loaded from clipboard")
        else:
            print("Key not found")
            
    elif command == 'list':
        print(data)
    else:
        print("Invalid command")
        sys.exit(1)

else:
    print("please add only one command")
