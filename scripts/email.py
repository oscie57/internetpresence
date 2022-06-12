import os, subprocess

emails = []

def main():
    quest = True
    while quest == True:
        ans = input("Email: ")

        if ans == "n" or ans == "N" or ans == "No" or ans == "no":
            quest = False
        else:
            emails.append(ans)

    def create_banner(item : str):
        itemLen = len(item)

        banner = "*" * (itemLen + 6)
        bannerLen = len(banner)

        itemCen = item.center(bannerLen)

        final = f"\n{banner}\n{itemCen}\n{banner}"

        print(final)

    if "email.txt" in os.listdir():
        fileemail = open('./email.txt', "w", encoding="utf-8")
    else:
        fileemail = open('./email.txt', "x", encoding="utf-8")

    emailfinal = ""

    for item in emails:
        create_banner(item)
        emailout = subprocess.check_output(f"holehe --only-used {item}", text=True)
        emailfinal += emailout

    replacelist = [
        "Twitter : @palenath\nGithub : https://github.com/megadose/holehe\nFor BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ",

        "[32m",
        "[0m",
        "[35m",
        "[31m",
        "[H[J"
    ]

    for item in replacelist:
        emailfinal = emailfinal.replace(item, "")

    fileemail.write(emailfinal)

    fileemail.close()

if __name__ == '__main__':
    main()