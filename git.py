import os
os.system("git add .")
print("""


 ██▓███   █    ██  ██████  ██░ ██    ▄▄▄█████▓ ▒█████       ▄████  ██▓▄▄▄█████▓ ██░ ██  █    ██  ▄▄▄▄   
▓██░  ██▒ ██  ▓██▒██    ▒ ▓██░ ██▒   ▓  ██▒ ▓▒▒██▒  ██▒    ██▒ ▀█▒▓██▒▓  ██▒ ▓▒▓██░ ██▒ ██  ▓██▒▓█████▄ 
▓██░ ██▓▒▓██  ▒██░ ▓██▄   ▒██▀▀██░   ▒ ▓██░ ▒░▒██░  ██▒   ▒██░▄▄▄░▒██▒▒ ▓██░ ▒░▒██▀▀██░▓██  ▒██░▒██▒ ▄██
▒██▄█▓▒ ▒▓▓█  ░██░ ▒   ██▒░▓█ ░██    ░ ▓██▓ ░ ▒██   ██░   ░▓█  ██▓░██░░ ▓██▓ ░ ░▓█ ░██ ▓▓█  ░██░▒██░█▀  
▒██▒ ░  ░▒▒█████▓▒██████▒▒░▓█▒░██▓     ▒██▒ ░ ░ ████▓▒░   ░▒▓███▀▒░██░  ▒██▒ ░ ░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
▒▓▒░ ░  ░░▒▓▒ ▒ ▒▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒     ▒ ░░   ░ ▒░▒░▒░     ░▒   ▒ ░▓    ▒ ░░    ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
░▒ ░     ░░▒░ ░ ░░ ░▒  ░ ░ ▒ ░▒░ ░       ░      ░ ▒ ▒░      ░   ░  ▒ ░    ░     ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
░░        ░░░ ░ ░░  ░  ░   ░  ░░ ░     ░      ░ ░ ░ ▒     ░ ░   ░  ▒ ░  ░       ░  ░░ ░ ░░░ ░ ░  ░    ░ 
            ░          ░   ░  ░  ░                ░ ░           ░  ░            ░  ░  ░   ░      ░      
                                                                                                      ░ 

""")
cname = input("Commit Name: ")
cname = "git commit -m "+cname
os.system(cname)
os.system("git push -u origin 'main'")