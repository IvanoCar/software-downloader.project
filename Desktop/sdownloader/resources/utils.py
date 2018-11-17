import requests
import os
from tkinter import messagebox
from random import choice


class Utility:

    @staticmethod
    def check_internet_conn():
        try:
            r = requests.head('https://www.google.com')
            return True
        except requests.ConnectionError:
            messagebox.showinfo("Connection error",
                                "Please check your internet connection before continuing.")  # DIZAJNIATI
            return False

    @staticmethod
    def check_server_conn(url):
        try:
            r = requests.head(url)
            return True
        except requests.ConnectionError:
            messagebox.showinfo("Sever Error",
                                "We are having some server problems. Please come back later.")  # DIZAJNIATI
            return False

    @staticmethod
    def define_output_path():
        opath = os.path.dirname(os.path.abspath('app.py')) + "\Downloads\\"
        try:
            os.makedirs(os.path.dirname(opath))
        except FileExistsError:
            pass
        return opath
