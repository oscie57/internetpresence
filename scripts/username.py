import os
import subprocess
import sys

usernames = ""

def create_banner(item: str):
    itemLen = len(item)

    banner = "*" * (itemLen + 6)
    bannerLen = len(banner)

    itemCen = item.center(bannerLen)

    final = f"\n{banner}\n{itemCen}\n{banner}"

    print(final)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.isdir("sherlock"):
    create_banner("Installing Sherlock")
    os.system("git clone https://github.com/sherlock-project/sherlock")
    os.chdir("sherlock/")
    os.system("py -m pip install -r requirements.txt")
    create_banner("Installation finished")

quest = True
while quest == True:
    ans = input("Username: ")

    if ans == "n" or ans == "N" or ans == "No" or ans == "no":
        quest = False
    else:
        usernames = usernames + " " + ans

os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.check_call(
    f"py sherlock/sherlock --verbose --print-all --folderoutput \"../username/\" --timeout 10 {usernames}", stdout=sys.stdout, stderr=subprocess.STDOUT, text=True)