import Tools
import time
from dotenv import load_dotenv
from os import getenv
from requests.exceptions import ConnectionError
import random

load_dotenv()
FILE_PATH = getenv("PATH_TO_FOLDER")
sublist = []

print(f"Preparing for submission of all files in folder {FILE_PATH}")
try:
    sublist = Tools.getlooplist()
except ConnectionError:
    print("Connection error")
    exit(1)

if (len(sublist) == 0):
    print("Nothing to submit")
    exit(0)

print(f"Submitting {sublist}")
confirm = input("Proceed? (y/n) ").lower()

if confirm == "y" or confirm == "yes":
    print("Submitting...")
    driver = Tools.setup()
    for file in sublist:
        try:
            Tools.submitfile(driver, f"{FILE_PATH}\{file}")

            timeSubmit = random.randint(90, 120)
            print(f"{file} submitted, waiting for {timeSubmit} seconds")
            time.sleep(timeSubmit)
        except KeyboardInterrupt:
            halt = input(
                "Sleep period interrupted, halt program? (y/n) ").lower()
            if halt == "y" or halt == "yes":
                print("Aborted")
                exit(0)
            else:
                print("Force submitting next file")
        except:
            print(f"Error while submitting {file}")
    driver.quit()
else:
    print("Aborted")
