import sys
import datetime
import socket

def show_help():
    print("Program: Fixing Inseucre Windows Service Permission")
    print("Version: 1.0")
    print("Written: Vorawut Sanitnok")
    print("")
    print(f"Usage: {sys.argv[0]} [-enforce|-e|-restore|-r|-h|-help] filename")
    print("  -enforce or -e: enforce changes to the file")
    print("  -restore or -r: restore the original file from the backup")
    print("  -h or -help: display this help message")
    print("  filename: the name of the text file to process")

# Check the number of arguments
if len(sys.argv) != 3:
    show_help()
    sys.exit(1)

action = sys.argv[1]       # Initialize the action variable
filename = sys.argv[2]     # Get the filename from the first argument

if action not in ['-enforce', '-e', '-restore', '-r', '-h', '-help']:
    show_help()
    sys.exit(1)

if action in ['-h', '-help']:
    show_help()
    sys.exit(0)

now = datetime.datetime.now()
hostname = socket.gethostname()
backup_filename = now.strftime("%Y%m%d-%H%M%S") + "_" + hostname + ".txt"

print("Program: Fixing Inseucre Windows Service Permission")
print("Version: 1.0")
print("Written: Vorawut Sanitnok")
print("")

if action in ['-enforce', '-e']:
    count = 0
    with open(backup_filename, "w") as backup_file:
        with open(filename, 'r') as file:
            for line in file:
                original_line = line
                index = line.find("(AU")
                if index != -1:
                    end = line.find(")", index)
                    if "WO" in line[index:end]:
                        line = line[:index] + line[index:end].replace("WO", ";") + line[end:]
                        count += 1
                backup_file.write(original_line)
                print("Original Line: ", original_line)
                print("Modified Line: ", line)

    print("Number of changes: ", count)
    print("Backup file created: ", backup_filename)

if action in ['-restore', '-r']:
    with open(filename, "w") as file:
        with open(backup_filename, 'r') as backup_file:
            for line in backup_file:
                file.write(line)
    print("File restored from: ", backup_filename)
