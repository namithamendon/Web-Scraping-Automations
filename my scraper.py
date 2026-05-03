import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Connect to the practice site
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# 2. Check if the connection is successful
if response.status_code == 200:
    print("Connection Successful! Extracting data...")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    
    # 3. Target the 'quote' containers
    quotes = soup.find_all('div', class_='quote')
    
    for q in quotes:
        text = q.find('span', class_='text').text
        author = q.find('small', class_='author').text
        # Adding some logic to clean the text
        data.append({"Quote": text.strip("“”"), "Author": author})
    
    # 4. Save to Excel/CSV (This is the 'Product' you sell)
    df = pd.DataFrame(data)
    df.to_csv("my_first_scrape.csv", index=False)
    
    print("--- MISSION ACCOMPLISHED ---")
    print(f"Total Quotes Collected: {len(df)}")
    print("Check your folder for 'my_first_scrape.csv'!")
else:
    print(f"Error: Could not connect. Code: {response.status_code}")
