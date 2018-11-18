# Software Downloader project

Old project for downloading software installations from official websites expanded with web API and server-side download link scraping once a day. 

All components are written in Python:

- Desktop can be built with Pyinstaller
- WebAPI is made with Flask microframework - tested with Heroku. MongoDB (mLab) is used for database.
- Scheduler is scheduler app used for scraping links and saving to DB. Errors are sent via email (TODO).



