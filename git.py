import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# function to allow student to initialize an empty repo
def init_repo():
    print("Initializing git repository")

    # checking if directory is a git repo
    if os.system("git rev-parse") != 0:
        os.system("git init .")

        lines = ["git.py", ".idea/"]        # we can add more to this list to ignore more files and directories
        content = "\n".join(lines)
        with open(".gitignore", "w") as gitignore:
            gitignore.write(content)

    else:
        print("Directory is already a git repository")


# function to allow student to make a new commit
def commit():
    print("Committing files")

    if os.system("git rev-parse") == 0:
        os.system("git add .")

        message = input("Please give a commit message: ")
        os.system('git commit -m "{}"'.format(message))

    else:
        init_repo()

        os.system("git add .")

        message = input("Please give a commit message: ")
        os.system('git commit -m "{}"'.format(message))


# function to allow student to checkout a previous commit
def checkout():
    if os.system("git rev-parse") == 0:
        commit_hash = input("Checkout commit:  ")

        # implement hashing checking condition to see if student entered the right hash
        os.system("git checkout {}".format(commit_hash))

    else:
        print("This directory is currently not a git repository.")


# function to allow students to return head to latest commit
def return_to_latest():
    if os.system("git rev-parse") == 0:
        os.system("git checkout master")

    else:
        print("This directory is currently not a git repository.")


# function to display git log; later on if we want, we can display git graph
def display_log():
    if os.system("git rev-parse") == 0:
        os.system("git log")

        print(bcolors.OKBLUE + "\nIf you don't see the commit you're looking for,\n" +
                               "run git.py again and return to the latest commit (option 1)." + bcolors.ENDC)

    else:
        print("This directory is currently not a git repository.")


print("Hello! Welcome to the CS112 git interface!\n")

print("Please select one of the following options: ")
print("1: Initialize git repo")
print("2: Make new commit")
print("3: Checkout previous commit")
print("4: Return to latest commit")
print("5: Display log")

option = input("Select Option: ")

try:
    option_int = int(option)

except ValueError:
    print("Not a valid option")

else:
    if option_int == 1:
        init_repo()

    elif option_int == 2:
        commit()

    elif option_int == 3:
        checkout()

    elif option_int == 4:
        return_to_latest()

    elif option_int == 5:
        display_log()

    else:
        print("Not a valid option")
