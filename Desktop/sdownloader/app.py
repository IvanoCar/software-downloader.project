from tkinter import *
from sdownloader.resources.gui import GUIwidgets
from sdownloader.resources.utils import Utility

window = Tk()
window.geometry("370x360")
window.resizable(False, False)
window.title("Software Downloader")

widgets = GUIwidgets(window)

if Utility.check_internet_conn():
    if Utility.check_server_conn(widgets.API_URL):
        widgets.init_download_links()

window.mainloop()
