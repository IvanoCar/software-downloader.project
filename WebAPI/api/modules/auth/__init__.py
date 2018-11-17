class Auth:

    def __init__(self):
        self.keys = {
            'update': 'UPDATE KEY GOES HERE',
            'get': 'GET KEY GOES JERE'
        }

        self.agents = {
            'update': 'software-downloader.cron',
            'get': 'software-downloader.desktop'
        }

    def get(self, request):
        try:
            if request.headers['api-key'] == self.keys['get']:
                if request.headers['user-agent'] == self.agents['get']:
                    return True
            return False
        except KeyError:
            return False

    def post(self, request):
        try:
            if request.headers['api-key'] == self.keys['update']:
                if request.headers['user-agent'] == self.agents['update']:
                    return True
            return False
        except KeyError:
            return False
