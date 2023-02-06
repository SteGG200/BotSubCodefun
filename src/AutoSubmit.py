import Tools
from os import getenv
import time
import random

tasks = ["001"]
language = getenv("LANGUAGE", "Python3")
driver = Tools.setup()

for i in tasks:
    try:
        Tools.submit(driver, i, language)
        timeSubmit = random.randint(90, 300)
        print(f"{i} submitted, waiting for {timeSubmit} seconds")
        time.sleep(timeSubmit)
    except KeyboardInterrupt:
        print("Sleep period interrupted, force submitting next file")
    except:
        print(f"Error while submitting {i}")
driver.quit()
