import os, subprocess

phones = []

def main():
    quest = True

    print("Please input phone numbers here.")
    print("Make sure to put the country code before the number.")
    print("Example: '44 1234222222'\n")
    while quest == True:
        ans = input("Phone Number: ")

        if ans == "n" or ans == "N" or ans == "No" or ans == "no":
            quest = False
        else:
            phones.append(ans)

    def create_banner(item : str):
        itemLen = len(item)

        banner = "*" * (itemLen + 6)
        bannerLen = len(banner)

        itemCen = item.center(bannerLen)

        final = f"\n{banner}\n{itemCen}\n{banner}"

        print(final)

    if "phone.txt" in os.listdir():
        file = open('../phone.txt', "w", encoding="utf-8")
    else:
        file = open('../phone.txt', "x", encoding="utf-8")

    final = ""

    for item in phones:
        create_banner(item)
        out = subprocess.check_output(f"ignorant --only-used {item}", text=True)
        final += out

    replacelist = [
        "Twitter : @palenath\nGithub : https://github.com/megadose/ignorant\nFor BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ",

        "[32m",
        "[0m",
        "[35m",
        "[31m",
        "[H[J"
    ]

    for item in replacelist:
        final = final.replace(item, "")

    file.write(final)

    file.close()

if __name__ == '__main__':
    main()