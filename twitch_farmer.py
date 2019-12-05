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

