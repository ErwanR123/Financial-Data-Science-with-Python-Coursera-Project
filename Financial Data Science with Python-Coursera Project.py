import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
from bs4 import BeautifulSoup

# Load Apple data
apple = yf.Ticker("AAPL")
with open('apple_info.json') as json_file:
    apple_info = json.load(json_file)

print("Apple Country:", apple_info.get("country", "Unknown"))
print("Apple Info:", apple_info)

# Fetch historical stock data for Apple
apple_share_price_data = apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)
print(apple_share_price_data.head())

# Load AMD data
amd = yf.Ticker("AMD")
with open('amd_info.json') as json_file:
    amd_info = json.load(json_file)

print("AMD Country:", amd_info.get("country", "Unknown"))
print("AMD Sector:", amd_info.get("sector", "Unknown"))

# Fetch historical stock data for AMD
amd_share_price_data = amd.history(period="max")
amd_share_price_data.reset_index(inplace=True)
print(amd_share_price_data.head())

first_day_volume = amd_share_price_data.iloc[0]["Volume"]
print("AMD First Day Volume:", first_day_volume)

# Scrape Netflix data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
response = requests.get(url)

if response.status_code == 200:
    print("Netflix webpage downloaded successfully.")
    soup = BeautifulSoup(response.text, 'html.parser')
    netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

    for row in soup.find("tbody").find_all('tr'):
        cols = row.find_all("td")
        netflix_data = netflix_data.append({
            "Date": cols[0].text.strip(),
            "Open": cols[1].text.strip(),
            "High": cols[2].text.strip(),
            "Low": cols[3].text.strip(),
            "Close": cols[4].text.strip(),
            "Adj Close": cols[5].text.strip(),
            "Volume": cols[6].text.strip()
        }, ignore_index=True)
    print(netflix_data.head())
else:
    print(f"Error downloading Netflix data: {response.status_code}")

# Tesla stock and revenue data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data["Date"] = pd.to_datetime(tesla_data["Date"])
print(tesla_data.head())

# Scrape Tesla revenue data
url_tesla_revenue = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url_tesla_revenue)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')

    for table in tables:
        if "Tesla Quarterly Revenue" in str(table):
            relevant_table = table
            break

    tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
    for row in relevant_table.tbody.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) == 2:
            tesla_revenue = tesla_revenue.append({
                "Date": cols[0].text.strip(),
                "Revenue": cols[1].text.strip().replace(',', '').replace('$', '')
            }, ignore_index=True)

    tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])
    tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue["Revenue"], errors='coerce')
    tesla_revenue.dropna(inplace=True)
    print(tesla_revenue.tail())
else:
    print(f"Error downloading Tesla revenue data: {response.status_code}")

# GameStop stock and revenue data
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data["Date"] = pd.to_datetime(gme_data["Date"])
print(gme_data.head())

# Scrape GameStop revenue data
url_gme_revenue = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
response = requests.get(url_gme_revenue)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')

    for table in tables:
        if "GameStop Quarterly Revenue" in str(table):
            relevant_table = table
            break

    gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
    for row in relevant_table.find_all("tr")[1:]:
        cols = row.find_all("td")
        gme_revenue = gme_revenue.append({
            "Date": cols[0].text.strip(),
            "Revenue": cols[1].text.strip().replace(',', '').replace('$', '')
        }, ignore_index=True)

    gme_revenue["Date"] = pd.to_datetime(gme_revenue["Date"])
    gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"], errors='coerce')
    gme_revenue.dropna(inplace=True)
    print(gme_revenue.tail())
else:
    print(f"Error downloading GameStop revenue data: {response.status_code}")

# Plotting function
def make_graph(stock_data, revenue_data, stock_name):
    fig, ax1 = plt.subplots(figsize=(14, 7))

    ax1.plot(stock_data['Date'], stock_data['Close'], color='blue', label="Stock Price")
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Stock Price (USD)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(revenue_data['Date'], revenue_data['Revenue'], color='red', label="Revenue")
    ax2.set_ylabel('Revenue (USD)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    plt.title(f'{stock_name} Stock Price and Revenue')
    plt.show()

# Plot data
make_graph(tesla_data, tesla_revenue, "Tesla")
make_graph(gme_data, gme_revenue, "GameStop")