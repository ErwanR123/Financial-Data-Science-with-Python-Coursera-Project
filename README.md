# **Financial Data Science with Python**

This project is part of the Coursera Data Science specialization. It involves collecting, cleaning, and analyzing financial data using Python. The analysis includes stock price trends and quarterly revenue for companies such as Tesla, GameStop, Apple, AMD, and Netflix.

---

## **Project Overview**

The project demonstrates the following concepts:
- **Data Collection**:
  - Retrieve historical stock price data using the `yfinance` library.
  - Scrape quarterly revenue data from webpages using `BeautifulSoup` and `requests`.
- **Data Cleaning and Preprocessing**:
  - Format and clean scraped revenue data for consistency and usability.
  - Handle missing or malformed data and convert data types as required.
- **Data Visualization**:
  - Plot stock prices alongside revenue data for insights.
  - Use dual-axis plots for clear comparison between stock trends and revenue trends.

---

## **Key Features**
1. **Analyze Multiple Companies**:
   - Tesla (`TSLA`)
   - GameStop (`GME`)
   - Apple (`AAPL`)
   - AMD (`AMD`)
   - Netflix (`NFLX`)

2. **End-to-End Data Science Workflow**:
   - Collect financial data from APIs and web scraping.
   - Clean and prepare data for analysis.
   - Generate visualizations to uncover insights.

3. **Dynamic and Scalable Design**:
   - Modularized functions for data collection, cleaning, and visualization.
   - Easily extendable for analyzing additional companies or metrics.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - `yfinance`: For fetching historical stock data.
  - `pandas`: For data manipulation and analysis.
  - `matplotlib`: For data visualization.
  - `requests` and `BeautifulSoup`: For web scraping.
 
---

## **File Structure**
- `Financial_Data_Science_with_Python-Coursera_Project.py`: Main Python script containing all the code for this project.
- `apple_info.json`, `amd_info.json`: Sample JSON files with additional company information (like sector or country).
- **Data Sources**:
  - Tesla Revenue: [Coursera Project Data](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm)
  - GameStop Revenue: [Coursera Project Data](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html)
  - Netflix Historical Data: [Netflix Data Page](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html)

---

## **Results**
1. Historical stock price and revenue trends for Tesla and GameStop.
2. Dual-axis visualizations showing stock performance relative to revenue.
3. Cleaned DataFrames ready for further analysis or machine learning models.

---

## **Acknowledgments**
This project was developed as part of the Coursera course **"Python Project for Data Science "**, offered by IBM.

