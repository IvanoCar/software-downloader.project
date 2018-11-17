from tkinter import *
from sdownloader.resources.scraper import GetResources
from sdownloader.resources.downlader import SoftwareDownloader
from sdownloader.resources.utils import Utility
from threading import Thread


class GUIwidgets(SoftwareDownloader, GetResources):
    def __init__(self, main_window):
        super().__init__(self, main_window)
        self.checkboxes = {}
        self.download_btn = Button(main_window, text="Download", command=self.download_btn)

        var_chrome = IntVar()
        var_opera = IntVar()
        var_firefox = IntVar()
        var_cccleaner = IntVar()
        var_7zip32 = IntVar()
        var_7zip64 = IntVar()
        var_burnerxp = IntVar()
        var_teamv = IntVar()
        var_avastfree = IntVar()
        var_vlc = IntVar()
        var_foxit = IntVar()
        var_aimp = IntVar()
        var_libre = IntVar()
        var_speccy = IntVar()
        var_utorrent = IntVar()

        self.checkbox_chrome = Checkbutton(main_window, text="Google Chrome", variable=var_chrome)
        self.checkbox_firefox = Checkbutton(main_window, text="Mozilla Firefox", variable=var_firefox)
        self.checkbox_opera = Checkbutton(main_window, text="Opera", variable=var_opera)
        self.checkbox_cccleaner = Checkbutton(main_window, text="CC Cleaner", variable=var_cccleaner)
        self.checkbox_7zip32 = Checkbutton(main_window, text="7zip (32bit)", variable=var_7zip32)
        self.checkbox_7zip64 = Checkbutton(main_window, text="7zip (64bit)", variable=var_7zip64)
        self.checkbox_burnerxp = Checkbutton(main_window, text="CD Burner XP", variable=var_burnerxp)
        self.checkbox_tviewer = Checkbutton(main_window, text="TeamViewer", variable=var_teamv)
        self.checkbox_avastf = Checkbutton(main_window, text="Avast Free Version", variable=var_avastfree)
        self.checkbox_vlc = Checkbutton(main_window, text="VLC Media Player", variable=var_vlc)
        self.checkbox_foxit = Checkbutton(main_window, text="Foxit Reader", variable=var_foxit)
        self.checkbox_aimp = Checkbutton(main_window, text="AIMP", variable=var_aimp)
        self.checkbox_libre = Checkbutton(main_window, text="Libre Office", variable=var_libre)
        self.checkbox_speccy = Checkbutton(main_window, text="Speccy", variable=var_speccy)
        self.checkbox_utorrent = Checkbutton(main_window, text="uTorrent", variable=var_utorrent)

        self.checkboxes['Google Chrome'] = var_chrome
        self.checkboxes['Mozilla Firefox'] = var_firefox
        self.checkboxes['Opera'] = var_opera
        self.checkboxes['CC Cleaner'] = var_cccleaner
        self.checkboxes['7zip (32bit)'] = var_7zip32
        self.checkboxes['7zip (64bit)'] = var_7zip64
        self.checkboxes['CD Burner XP'] = var_burnerxp
        self.checkboxes['TeamViewer'] = var_teamv
        self.checkboxes['Avast Free'] = var_avastfree
        self.checkboxes['VLC Media Player'] = var_vlc
        self.checkboxes['Foxit Reader'] = var_foxit
        self.checkboxes['AIMP'] = var_aimp
        self.checkboxes['Libre Office'] = var_libre
        self.checkboxes['Speccy'] = var_speccy
        self.checkboxes['uTorrent'] = var_utorrent

        self.set_widget_positions()

    def download_btn(self):
        self.download_btn['state'] = 'disabled'
        if Utility.check_internet_conn():
            if Utility.check_server_conn(self.API_URL):
                if not self.are_pulled:
                    self.info_console.insert(END, "Checking for latest versions...\n")
                    self.info_console.update()
                    self.init_download_links()
                    self.info_console.insert(END, "Latest versions updated.\n")
                Thread(target=self.download_but_fn).start()
        else:
            self.download_btn['state'] = 'normal'

    def download_but_fn(self):
        self.download_btn['state'] = 'disabled'
        c = 0
        for i, k in self.checkboxes.items():
            if k.get() == 1:
                c += 1
                if self.ddlinks[i] is '-':
                    self.info_console.insert(END, "%s can't be downloaded.\n" % i)
                else:
                    self.download_setup(i, self.ddlinks[i])
        if c is 0:
            self.info_console.insert(END, "No programs were selected.\n")
            self.info_console.see(END)
        self.download_btn['state'] = 'normal'
        self.reset_cboxes()

    def reset_cboxes(self):
        for i, k in self.checkboxes.items():
            k.set(0)

    def set_widget_positions(self):
        self.checkbox_chrome.place(x=10, y=10)
        self.checkbox_firefox.place(x=130, y=10)
        self.checkbox_opera.place(x=240, y=10)

        self.checkbox_cccleaner.place(x=10, y=40)
        self.checkbox_7zip32.place(x=130, y=40)
        self.checkbox_7zip64.place(x=240, y=40)

        self.checkbox_burnerxp.place(x=10, y=70)
        self.checkbox_tviewer.place(x=130, y=70)
        self.checkbox_avastf.place(x=240, y=70)

        self.checkbox_vlc.place(x=10, y=100)
        self.checkbox_foxit.place(x=240, y=100)
        self.checkbox_aimp.place(x=130, y=100)

        self.checkbox_libre.place(x=10, y=130)
        self.checkbox_speccy.place(x=130, y=130)
        self.checkbox_utorrent.place(x=240, y=130)

        self.download_btn.place(x=285, y=320)
