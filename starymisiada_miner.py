from time import sleep
from colorama import Fore, Style
import string, random
import time
from progress.bar import Bar

# logo
chuj = ["""             .                                                     o8o            o8o                  .o8            """,
        """           .o8                                                     `"'            `"'                 "888            """,
        """ .oooo.o .o888oo  .oooo.   oooo d8b oooo    ooo ooo. .oo.  .oo.   oooo   .oooo.o oooo   .oooo.    .oooo888   .oooo.   """,
        """d88(  "8   888   `P  )88b  `888""8P  `88.  .8'  `888P"Y88bP"Y88b  `888  d88(  "8 `888  `P  )88b  d88' `888  `P  )88b  """,
        """`"Y88b.    888    .oP"888   888       `88..8'    888   888   888   888  `"Y88b.   888   .oP"888  888   888   .oP"888   ©""",
        """o.  )88b   888 . d8(  888   888        `888'     888   888   888   888  o.  )88b  888  d8(  888  888   888  d8(  888  """,
        """8""888P'   "888" `Y888""8o d888b        .8'     o888o o888o o888o o888o 8""888P' o888o `Y888""8o `Y8bod88P" `Y888""8o """,
        """                                    .o..P'                                                                            """,
        """                                    `Y8P'                                                                             \n"""
        ]

# logo animation
for chunk in chuj:
    print(Fore.YELLOW + chunk + Style.RESET_ALL)
    sleep(0.15)
input("Please, enter your bitcoin wallet adress: ")
print ("Connecting to database")
sleep (1.5)

# progressbar
bar=Bar(max=20, suffix="%(percent)d%%")
for i in range (20):
    bar.next()
    time.sleep(0.5)
bar.finish()

print (Fore.GREEN +"Successful connection, please wait")
sleep (1.5)
print("Account connected\nMining starting now:\n"+ Style.RESET_ALL )
sleep (2)

# wallet generator
for i in range(random.randint(0,100)):
    print(''.join(random.choice(string.ascii_letters + string.digits) for i in range(52)) + Fore.RED + " --> 0.000000 BTC" + Style.RESET_ALL)
    sleep (0.5)
print(''.join(random.choice(string.ascii_letters + string.digits) for i in range(52)) + Fore.GREEN + f" --> {round(random.uniform(0,1),6)} BTC" + Style.RESET_ALL)