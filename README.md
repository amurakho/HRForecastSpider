# HRForecastSpider

The catalog is a complete project. Those. virtual environment with all the necessary libraries already "in the box"

Download Project(git clone https://github.com/amurakho/HRForecastSpider.git)

Go to the directory with the project  (cd HRForecastspider)

Activate the virtual environment (source venv/bin/activate)

Enter the desired directory to run the project (cd HRForecastSpider/HRForecastSpider)

Launch the spider, which save the base in 'base.csv' (scrapy crawl HRForecast -o base.csv)

Run a convector from .csv to .xlsx (python read_csv.py)

The data.xlsx file stores the base.

!!! Variables with the names of the database files are embedded in the code !!! "
