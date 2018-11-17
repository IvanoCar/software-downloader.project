import requests
from bs4 import BeautifulSoup
from scheduler.modules.utils import Utils


# TODO:
# - split this class into several: optimize scraping
# - threading notifications?
#  FILL IN EMAIL, PASSWORD
class Scraper:
    def __init__(self):
        self.headers = {
            'user-agent': Utils.set_random_usr_agent()
        }

        self.ddlinks = {}
        self.errors = []
        self.error = False
        self.init_download_links()

    # def notify(self):
    #     err = ''
    #     for i in self.errors:
    #         err += '%s: %s\n' % (i['name'], i['error'])
    #         err += "\n"
    #
    #     message = MIMEText('Errors in Software Web Scraper\n\n{}'.format(err), 'plain')
    #     msg = MIMEMultipart()
    #     msg['Subject'] = '[NEW ERRORS] Software'
    #     msg.attach(message)
    #     smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #     smtpObj.login("MAIL", "PASS")
    #
    #     try:
    #         smtpObj.sendmail("MAIL, ['RECIEPENT MAIL'], msg.as_string())
    #     except smtplib.SMTPException:
    #         pass

    def init_download_links(self):
        self.cc_cleaner()
        self.chrome()
        self.opera()
        self.firefox()
        self.sevenzip()
        self.cdburnerxp()
        self.teamviewer()
        self.freeavast()
        self.vlc()
        self.foxit()
        self.aimp()
        self.libreoffice()
        self.speccy()
        self.utorrent()

    def utorrent(self):
        self.ddlinks['uTorrent'] = 'http://download-hr.utorrent.com/track/stable/endpoint/utorrent/os/windows'

    def speccy(self):
        try:
            soup = BeautifulSoup(requests.get('https://www.piriform.com/speccy/download/standard',
                                              headers=self.headers).text, 'html.parser')
            link = soup.find("div", {'class': 'text-center'}).find('a')['href']
            self.ddlinks['Speccy'] = link
        except Exception as e:
            self.errors.append({'name': 'Speccy', 'error': str(e)})
            self.error = True
            self.ddlinks['Speccy'] = "-"

    def libreoffice(self):
        try:
            soup = BeautifulSoup(requests.get("https://www.libreoffice.org/download/download/?type=win-x86_64",
                                              headers=self.headers).text, 'html.parser')
            link = soup.find("span", {'class': 'dl_yellow_download_button'}).find('a')['href']

            soup = BeautifulSoup(requests.get(link, headers=self.headers).text, 'html.parser')
            link = soup.find('p', {'class': 'bs-callout'}).find('a')['href']

            self.ddlinks['Libre Office'] = 'https:' + link
        except Exception as e:
            self.errors.append({'name': 'Libre Office', 'error': str(e)})
            self.error = True
            self.ddlinks['Libre Office'] = "-"

    def aimp(self):
        try:
            soup = BeautifulSoup(requests.get("http://www.aimp.ru/?do=download&os=windows", headers=self.headers).text,
                                 'html.parser')
            link = soup.find("div", {'class': 'card_content'}).find('a')['href']
            self.ddlinks['AIMP'] = link
        except Exception as e:
            self.errors.append({'name': 'AIMP', 'error': str(e)})
            self.error = True
            self.ddlinks['AIMP'] = "-"

    def foxit(self):
        try:
            soup = BeautifulSoup(requests.get("https://www.foxitsoftware.com/downloads/thanks.php?product=Foxit-Reader"
                                              "&platform=Windows", headers=self.headers).text, 'html.parser')
            link = soup.find('span', {'class': 'no_manually_down'}).find('a')['href']
            self.ddlinks['Foxit Reader'] = link
        except Exception as e:
            self.errors.append({'name': 'Foxit Reader', 'error': str(e)})
            self.error = True
            self.ddlinks['Foxit Reader'] = "-"

    def vlc(self):
        try:
            soup = BeautifulSoup(requests.get("https://www.videolan.org/vlc/index.hr.html", headers=self.headers).text,
                                 'html.parser')
            link = "https://" + soup.find('a', {'id': 'downloadButton2'})['href'].replace("//", "")

            self.ddlinks['VLC Media Player'] = link
        except Exception as e:
            self.errors.append({'name': 'VLC Media Player', 'error': str(e)})
            self.error = True
            self.ddlinks['VLC Media Player'] = "-"

    def freeavast(self):
        try:
            soup = BeautifulSoup(requests.get("https://www.avast.com/en-us/download-thank-you.php?product=FAV-ONLINE&"
                                              "locale=en-us", headers=self.headers).text, 'html.parser')
            link = soup.find('a', {'id': 'pdl-manual'})['href']

            self.ddlinks['Avast Free'] = link
        except Exception as e:
            self.errors.append({'name': 'Avast Free', 'error': str(e)})
            self.error = True
            self.ddlinks['Avast Free'] = "-"

    def teamviewer(self):
        self.ddlinks['TeamViewer'] = "https://download.teamviewer.com/download/TeamViewer_Setup.exe"

    def cdburnerxp(self):
        self.ddlinks['CD Burner XP'] = "https://cdburnerxp.se/downloadsetup.exe"

    def sevenzip(self):
        try:
            soup = BeautifulSoup(requests.get("http://www.7-zip.org/download.html",
                                              headers=self.headers).text, 'html.parser')
            a_elements = []
            table_data = soup.find_all('td', {'class': 'Item'})
            for td in table_data:
                if td.find('a') is not None:
                    a_elements.append(td.find('a'))
                if len(a_elements) is 2:
                    break
            version64 = 'http://www.7-zip.org/' + a_elements[1]['href']
            version32 = 'http://www.7-zip.org/' + a_elements[0]['href']

            self.ddlinks['7zip (32bit)'] = version32
            self.ddlinks['7zip (64bit)'] = version64
        except Exception as e:
            self.errors.append({'name': '7zip', 'error': str(e)})
            self.error = True
            self.ddlinks['7zip (32bit)'] = "-"
            self.ddlinks['7zip (64bit)'] = "-"

    def cc_cleaner(self):
        try:
            soup = BeautifulSoup(requests.get("http://www.piriform.com/ccleaner/download/standard",
                                              headers=self.headers).text, 'html.parser')
            link = (soup.find('div', {'class': 'text-center'})).find('a')['href']
            self.ddlinks['CC Cleaner'] = link
        except Exception as e:
            self.errors.append({'name': 'CC Cleaner', 'error': str(e)})
            self.error = True
            self.ddlinks['CC Cleaner'] = "-"

    def chrome(self):
        self.ddlinks['Google Chrome'] = "https://dl.google.com/tag/s/appguid={8A69D345-D564-463C-AFF1-A69D9E530F96}&" \
                                        "iid={4D9D2560-AF43-CE6C-A151-7AFB0D3F2A4E}/update2/installers/ChromeSetup.exe"

    def opera(self):
        try:
            soup = BeautifulSoup(requests.get("http://www.opera.com/computer/thanks?ni=stable&os=windows",
                                              headers=self.headers).text, 'html.parser')
            link = (soup.find('p', {'class': 'info-message'})).find('a')['href']
            self.ddlinks['Opera'] = link
        except Exception as e:
            self.errors.append({'name': 'Opera', 'error': str(e)})
            self.error = True
            self.ddlinks['Opera'] = "-"

    def firefox(self):
        self.ddlinks['Mozilla Firefox'] = 'https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US'

