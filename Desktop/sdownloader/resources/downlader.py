import requests
import time
from sdownloader.resources.utils import Utility
from tkinter import *
from tkinter import ttk


class SoftwareDownloader:

    def __init__(self, gui_widgets, main_window):
        super().__init__()
        self.widgets = gui_widgets
        self.out_path = Utility.define_output_path()

        self.progress = ttk.Progressbar(main_window, orient=HORIZONTAL, value=0)
        self.info_console = Text(main_window)
        self.info_console.bind("<Key>", lambda e: "break")
        self.current_task_lbl = Label(main_window, text='Ready for download.')

        self.current_task_lbl.place(x=14, y=165)
        self.progress.place(x=15, y=190, width=338)
        self.info_console.place(x=15, y=220, height=90, width=338)

    def download_setup(self, name, url):
        self.current_task_lbl['text'] = 'Downloading ' + name + '....'

        local_filename = self.out_path + url.split('/')[-1]
        if ".exe" not in local_filename:
            local_filename = self.out_path + name + ".exe"
        else:
            if len(local_filename) > 20:
                local_filename = self.out_path + name + ".exe"

        if '.msi' in url:
            local_filename = local_filename.replace('.exe', '.msi')

        r = requests.get(url, stream=True)
        try:
            total_size = int(r.headers['Content-Length'])
        except KeyError:
            total_size = len(r.content)

        self.current_task_lbl['text'] += ' [ {} MB ]'.format(round(((total_size/1024)/1000), 2))

        self.progress.configure(mode='determinate', maximum=total_size)
        self.progress['value'] = 0

        with open(local_filename, 'wb') as f:
            i = 0
            for chunk in r.iter_content(chunk_size=4096):
                i += len(chunk)
                f.write(chunk)
                self.progress['value'] = i
        self.current_task_lbl['text'] = "Done."
        self.info_console.insert(END, name + " downloaded.\n")
        self.info_console.see(END)


