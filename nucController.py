import os
import time
import sched
# Import the necessary packages

# Create some items
def p():
    print("test print")

s = sched.scheduler(time.time, time.sleep)

import pyautogui
from dotenv import load_dotenv, dotenv_values, find_dotenv, set_key
from pathlib import Path
from typing import Union

hotspot_status = False


def get_hotspot_status():
    return hotspot_status


def create_env_file():
    env_file = Path('C:/nucController/.env')
    env_file.touch(exist_ok=True)
    f = open(env_file)
    # create an env file if  does not exist


# get environment variable from .env file
def get_env(env_name: str):
    """

    :type env_name: String
    """
    dotenv_file = find_dotenv()  # finds from a .env file
    load_dotenv(dotenv_file)  # load from the .env file
    return os.getenv(env_name)


# given an env_name e.g. password writes the new value to the env file
# e.g. setenv('password', 'hello') sets the .env file to password='hello'
def setenv(env_name: str, new_value: str):
    os.environ[env_name] = new_value
    dotenv_file = find_dotenv()  # finds from a .env file
    load_dotenv(dotenv_file)  # load from the .env file
    set_key(dotenv_file, env_name, os.environ[env_name])


def get_username():
    username = get_env('spotname')
    return username


def set_username(new_value: str):
    setenv("spotname", new_value)


def set_password(new_value: str):
    setenv("password", new_value)


def get_password():
    password = get_env('password')
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
    if get_env('debug') == 'True':
        print(searchbox)
    return searchbox


def get_india() -> str:
    india = f'{get_pictures_path()}india.png'
    if get_env('debug') == 'True':
        print(india)
    return india


def get_uk_london():
    london = f'{get_pictures_path()}uk.london.png'
    if get_env('debug') == 'True':
        print(london)
    return london


def get_uk_glasgow():
    glasgow = f'{get_pictures_path()}uk.glasgow.png'
    if get_env('debug') == 'True':
        print(glasgow)
    return glasgow


def get_usa_orlando():
    orlando = f'{get_pictures_path()}usa.orlando.png'
    if get_env('debug') == 'True':
        print(orlando)
    return orlando


def get_usa_lasvegas():
    vegas = f'{get_pictures_path()}usa.lasvegas.png'
    if get_env('debug') == 'True':
        print(vegas)
    return vegas


def get_network_icon():
    wired_network = f'{get_pictures_path()}network.png'
    if get_env('debug') == 'True':
        print(wired_network)
    return wired_network


def get_mobilehotspot_icon():
    hotspot = f'{get_pictures_path()}hotspot.png'
    if get_env('debug') == 'True':
        print(hotspot)
    return hotspot


def line():
    print("****************************************")


# click on the search input box for the countries
def click_searchbox():
    search_box = pyautogui.locateOnScreen(get_searchbox(), confidence="0.9")
    if get_env('debug') == 'True':
        print(search_box)
    pyautogui.moveTo(search_box)  # Moves the mouse to the coordinates of the image
    pyautogui.click()


def tile_windows():
    pyautogui.getWindowsWithTitle("cmd")[0].minimize()
    time.sleep(1)
    pyautogui.getWindowsWithTitle("surfshark")[0].maximize()
    time.sleep(1)
    click_searchbox()
    time.sleep(1)
    pyautogui.hotkey('win', 'left')
    time.sleep(4)
    pyautogui.hotkey('enter')
    time.sleep(4)
    os.system("cls")


# this menu must be printed everywhere due to focus cmd command
def master_menu():
    R = " "
    G = " "
    # print("")
    print("")
    print(R + '[0 or R]' + G + ' Restart Computer.')


def more_menu():
    R = " "
    G = " "
    # print("")
    master_menu()
    print(R + '[1 or C]' + G + ' Change to Australia.')
    print(R + '[2]' + G + ' Country ......')
    print(R + '[3]' + G + ' Country .......')
    print(R + '[4]' + G + ' Country ......')
    print(R + '[5]' + G + ' Country .......')
    print(R + '[6' + G + ' Country ......')
    print(R + '[7]' + G + ' Country .......')
    print(R + '[8]' + G + ' ')
    print(R + '[9]' + G + ' More options....')

    if get_hotspot_status() == False:
        global hotspot_status
        hotspot_status = True
        start_hotspot_gui()

    choice = input("Enter your choice [0-10]: ")

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
        start_hotspot_gui()

    elif choice == '3':
        start_hotspot_gui()
        stop_hotspot_gui()

    elif choice == '4':
        stop_hotspot_gui()

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

    elif choice == '9':
        set_username(input("New SSID name: "))

    elif choice == '10':
        set_password(input("New password: "))
    menu()

def menu():  ## Your menu design here
    R = " "
    G = " "
    # print("")
    print("")
    master_menu()
    print(R + '[1 or C]' + G + ' Cancel Computer Restart.')
    print(R + '[2]' + G + ' Start VPN hotspot.')
    print(R + '[3]' + G + ' Restart VPN hotspot.')
    print(R + '[4]' + G + ' Stop VPN hotspot.')
    print(R + '[5 or I]' + G + ' Change to India')
    print(R + '[6 or U]' + G + ' Change to UK')
    print(R + '[7 or A]' + G + ' Change to USA')
    print(R + '[8 or S]' + G + ' Print Screen Size')
    print(R + '[9]' + G + ' Set new SSID NAME')
    print(R + '[10]' + G + ' Set new password')

    if get_hotspot_status() == False:
        global hotspot_status
        hotspot_status = True
        start_hotspot_gui()

    choice = input("Enter your choice [0-10]: ")

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
        start_hotspot_gui()

    elif choice == '3':
        start_hotspot_gui()
        stop_hotspot_gui()

    elif choice == '4':
        stop_hotspot_gui()

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

    elif choice == '9':
        set_username(input("New SSID name: "))

    elif choice == '10':
        set_password(input("New password: "))
    menu()


# run this when the program starts
def initialise():
    # create an env file if it doesnt exist
    create_env_file()

    username = get_username()
    password = get_password()
    debug = get_env('debug')

    if username is None:
        set_username(input('Please set a new hotspot name: '))

    if password is None:
        set_password(input('Please set a new password for the hotspot: '))

    if debug is None:
        setenv('debug', 'False')

    # pyautogui.hotkey('win', 'left')

    tile_windows()
    # open the menu
    menu()
    focus_cmd()


# Defining Windows
def main():
    # start the hotspot
    initialise()


def start_hotspot():
    username = get_username()
    password = get_password()
    os.system(f'netsh wlan set hostednetwork mode=allow ssid={username} key={password}')
    os.system("NETSH WLAN start hostednetwork")


def start_hotspot_gui():
    wired_network = pyautogui.locateOnScreen(get_network_icon(), confidence="0.90")
    if get_env('debug') == 'True':
        print(wired_network)
    pyautogui.moveTo(wired_network)
    pyautogui.click()
    time.sleep(2)
    # comment
    mobile_hotspot = pyautogui.locateOnScreen(get_mobilehotspot_icon(), confidence="0.9")
    pyautogui.moveTo(mobile_hotspot)
    pyautogui.click()
    # comment
    time.sleep(2)
    # closes the wifi window
    wired_network = pyautogui.locateOnScreen(get_network_icon(), confidence="0.90")
    if get_env('debug') == 'True':
        print(wired_network)
    pyautogui.moveTo(wired_network)
    pyautogui.click()
    time.sleep(2)
    # comment
    focus_cmd()


def stop_hotspot_gui():
    start_hotspot_gui()


def stop_hotspot():
    os.system("netsh wlan stop hostednetwork")


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
