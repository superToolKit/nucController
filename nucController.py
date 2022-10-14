import os
import pyautogui
import time

def get_username():
    return "TEST"


def get_password():
    return "TEST"


def get_searchbox():
    return "./pictures/png/searchbox.inside.png"

def get_india() -> str:
    return "./pictures/png/india.png"


def get_uk_london():
    return "./pictures/png/uk.london.png"


def get_uk_glasgow():
    return "./pictures/png/uk.glasgow.png"


def get_usa_orlando():
    return "./pictures/png/usa.orlando.png"


def get_usa_lasvegas():
    return "./pictures/png/usa.lasvegas.png"


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
    choice = input("Enter your choice [0-7]: ")
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
    search_box = pyautogui.locateOnScreen(get_searchbox(), confidence="0.7")
    print(search_box)
    pyautogui.moveTo(search_box)  # Moves the mouse to the coordinates of the image
    pyautogui.click()

# empty the searchbox
def clear_searchbox():
        searchboxlocation = pyautogui.locateOnScreen(get_searchbox(), confidence="0.7")
        pyautogui.moveTo(searchboxlocation)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('delete')

# change country country icon is the picture of the country and country is the text to input for search
def change_country(countryIcon: str, country: str):
    clear_searchbox()
    click_searchbox()
    enter_text(country)
    time.sleep(2)
    countrylocation = pyautogui.locateOnScreen(countryIcon, confidence="0.7")
    pyautogui.moveTo(countrylocation)
    line()
    print(countrylocation)
    line()
    pyautogui.click()
    focus_cmd()

# get focus on the nuc controler cmd window
def focus_cmd():
    terminal_window = pyautogui.locateOnScreen("./pictures/png/nuccontroller.png", confidence="0.7")
    pyautogui.click(terminal_window)

# enter some text
def enter_text(text: str):
    clear_searchbox()
    pyautogui.write(text, interval=0.25)

if __name__ == "__main__":
    main()
