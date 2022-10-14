import os
import time

import pyautogui
from dotenv import load_dotenv, dotenv_values, find_dotenv, set_key
from pathlib import Path

dotenv_file = find_dotenv() # finds from a .env file
load_dotenv(dotenv_file) # load from the .env file


env = dotenv_values(".env")

def create_env_file():
    env_file = Path('C:/nucController/.env')
    env_file.touch(exist_ok=True)
    f = open(env_file)
    # create an env file if  does not exist



def get_username():
    username = os.getenv('spotname')
    return username


def set_username(new_value):
    os.environ["spotname"] = new_value
    set_key(dotenv_file, "spotname", os.environ["spotname"])


def set_password(new_value):
    os.environ["password"] = new_value
    set_key(dotenv_file, "password", os.environ["password"])


def get_password():
    password = (os.getenv('password'))
    return password


def get_screen():
    screen = pyautogui.size()
    return screen


def get_pictures_path():
    screen = get_screen()

    size_1920 = "./pictures/png/"
    size_1366 = "./pictures/png.1366/"

    if screen == (1366, 768):
        return size_1366

    if screen == (1920, 1080):
        return size_1920


def get_searchbox():
    searchbox = f'{get_pictures_path()}searchbox.inside.png'
    print(searchbox)
    return searchbox


def get_india() -> str:
    india = f'{get_pictures_path()}india.png'
    print(india)
    return india


def get_uk_london():
    london = f'{get_pictures_path()}uk.london.png'
    print(london)
    return london


def get_uk_glasgow():
    glasgow = f'{get_pictures_path()}uk.glasgow.png'
    print(glasgow)
    return glasgow


def get_usa_orlando():
    orlando = f'{get_pictures_path()}usa.orlando.png'
    print(orlando)
    return orlando


def get_usa_lasvegas():
    vegas = f'{get_pictures_path()}usa.lasvegas.png'
    print(vegas)
    return vegas


def line():
    print("****************************************")


def menu():  ## Your menu design here
    R = " "
    G = " "
    # print("")
    print("")
    print(R + '[0 or R]' + G + ' Restart Computer.')
    print(R + '[1 or C]' + G + ' Cancel Computer Restart.')
    print(R + '[2]' + G + ' Start VPN hotspot.')
    print(R + '[3]' + G + ' Restart VPN hotspot.')
    print(R + '[4]' + G + ' Stop VPN hotspot.')
    print(R + '[5 or I]' + G + ' Change to India')
    print(R + '[6 or U]' + G + ' Change to UK')
    print(R + '[7 or A]' + G + ' Change to USA')
    print(R + '[8 or S]' + G + ' Print Screen Size')
    choice = input("Enter your choice [0-8]: ")
    # print("Enter your choice [0-7]: ", end='')
    # choice = keyboard.read_key()

    if choice == '0' or choice.casefold() == 'r':  # if key 'q' is pressed :
        os.system("shutdown -r -t 30 -f")
        restart = True
        line()
        print("Restart in 30s. Programs will be closed.")
        line()

    if choice == '1' or choice.casefold() == 'c':
        try:
            os.system("shutdown -a")
            line()
            print("Restart cancelled.")
            line()
        except:
            line()
            print("No restart to cancel.")
            line()

    elif choice == '2':
        start_hotspot()

    elif choice == '3':
        stop_hotspot()
        start_hotspot()

    elif choice == '4':
        stop_hotspot()

    elif choice == '5' or choice.casefold() == 'i':
        change_country(get_india(), 'india')
        print("Changed to India.")


    elif choice == '6' or choice.casefold() == 'u':
        change_country(get_uk_london(), 'london')
        print("Changed to UK London.")

    elif choice == '7' or choice.casefold() == 'a':
        change_country(get_usa_lasvegas(), 'Las Vegas')
        print("Changed to Las Vegas, USA.")

    elif choice == '8' or choice.casefold() == 's':
        line()
        print(get_screen())
        line()
    menu()


# Defining Windows
def main():
    # start the hotspot
    start_hotspot()
    # open the menu
    menu()


def start_hotspot():
    username = get_username()
    password = get_password()
    os.system(f'netsh wlan set hostednetwork mode=allow ssid={username} key={password}')
    os.system("NETSH WLAN start hostednetwork")


def stop_hotspot():
    os.system("netsh wlan stop hostednetwork")


# click on the search input box for the countries
def click_searchbox():
    search_box = pyautogui.locateOnScreen(get_searchbox(), confidence="0.9")
    print(search_box)
    pyautogui.moveTo(search_box)  # Moves the mouse to the coordinates of the image
    pyautogui.click()


# empty the searchbox
def clear_searchbox():
    searchboxlocation = pyautogui.locateOnScreen(get_searchbox(), confidence="0.9")
    pyautogui.moveTo(searchboxlocation)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('delete')


# change country country icon is the picture of the country and country is the text to input for search
def change_country(countryIcon: str, country: str):
    clear_searchbox()
    click_searchbox()
    enter_text(country)
    time.sleep(2)
    countrylocation = pyautogui.locateOnScreen(countryIcon, confidence="0.9")
    pyautogui.moveTo(countrylocation)
    line()
    print(countrylocation)
    line()
    pyautogui.click()
    focus_cmd()


# get focus on the nuc controler cmd window
def focus_cmd():
    terminal_window = pyautogui.locateOnScreen(f'{get_pictures_path()}nuccontroller.png', confidence="0.9")
    pyautogui.click(terminal_window)


# enter some text
def enter_text(text: str):
    clear_searchbox()
    pyautogui.write(text, interval=0.25)


if __name__ == "__main__":
    main()
