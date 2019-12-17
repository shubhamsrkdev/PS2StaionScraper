# PS-2 Station Scraper
A very simple scraper to scrape PS station details and store them in a excel file.
This project uses Python 3.8 along with webbot, beautifulsoup4 and xlwt. Please install the following on top of your Python 3 and pip installation :

```
pip install webbot
pip install beautifulsoup4
pip install xlwt
```

**Make sure you replace Email and Password on lines 13 and 14** like :

```
web.type('f20160184@hyderabad...' , into = 'Username' , id = 'TxtEmail' )
web.type('ABC123..', into = 'Password', id = 'txtPass')
```
