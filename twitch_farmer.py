import sys
import os
from pathlib import Path
from time import sleep

from selenium import webdriver
import pandas
import json

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = None
current_proxy = None
proxy_timeout = False
delay = 10
page_elements = None


def follow_channel(username, follow_channel_name):



def sign_in(username, password):


def main():


def run_driver(run_with_proxy):
    global driver
    global current_proxy

    # stop driver before changing it
    stop_driver()

    chrome_options = Options()
    chrome_options.add_argument("--lang=en-US,en")
    chrome_options.add_argument("--disable-notifications")

    if run_with_proxy:
        current_proxy = find_available_proxy()

        if current_proxy:
            chrome_options.add_argument(
                "--proxy-server={}".format(current_proxy))
            print("Using proxy: [{}]".format(current_proxy))

    current_os = sys.platform

    chrome_driver_file_name = ""
    if current_os in "darwin":
        chrome_driver_file_name = "chromedriver_mac64"
    elif current_os in "linux":
        chrome_driver_file_name = "chromedriver_linux64"
    elif current_os in "win32":
        chrome_driver_file_name = "chromedriver_win32.exe"

    chrome_driver_path = get_full_path(
        "/drivers/{}".format(chrome_driver_file_name))

    driver = webdriver.Chrome(options=chrome_options,
                              executable_path=chrome_driver_path)
    driver.set_window_size(880, 720)
    driver.set_window_position(0, 0)
    driver.set_page_load_timeout(20)


def stop_driver():
    global driver

    if driver is None:
        pass
    else:
        driver.quit()
        driver = None


def exit():
    stop_driver()
    input("Pres 'Enter' to Exit")
    sys.exit()


if __name__ == '__main__':
    main()
    exit()
