import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 1. Define the list of URLs you want to scrape
urls = [
    "https://howstat.com/Cricket/Statistics/IPL/BattingMostAgg.asp?q=3",  #Most Runs
    "https://howstat.com/Cricket/Statistics/IPL/BowlingBestAgg.asp?q=2", #Most Wickets
    "https://howstat.com/Cricket/Statistics/IPL/MatchScores.asp?q=1"   #Highest Scores
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def get_table_from_url(url):
    """Helper function to scrape a single table from a URL"""
    print(f"Scraping: {url}...")
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Target the specific statistical table
        table = soup.find('table', class_='TableLined')
        
        if table:
            rows = []
            for tr in table.find_all('tr'):
                cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                # Basic filter: only keep rows with actual data
                if len(cells) > 5:
                    rows.append(cells)
            
            if rows:
                # Use the first row as headers
                return pd.DataFrame(rows[1:], columns=rows[0])
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    return None

def scrape_multiple_to_excel():
    # This will be the name of your final dataset
    filename = "IPL_Combined_Dataset.xlsx"
    
    # We use ExcelWriter to control exactly where tables are placed
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        current_row = 0
        
        for i, url in enumerate(urls):
            df = get_table_from_url(url)
            
            if df is not None:
                # Optional: Add a title row in Excel before the table
                # We create a tiny dataframe just for the title
                title = pd.DataFrame([["" for _ in range(len(df.columns))]])
                title.iloc[0, 0] = f"DATA SOURCE  {i+1}: {url.split('/')[-1]}"
                
                # Write the Title
                title.to_excel(writer, startrow=current_row, index=False, header=False)
                current_row += 1 # Move down 1 row
                
                # Write the Table Data
                df.to_excel(writer, startrow=current_row, index=False)
                
                # Update current_row: (length of data + header + 3 empty rows for spacing)
                current_row += len(df) + 3
                
                print(f"Added table from {url} to Excel.")
                
            # Be kind to the server: wait 1 second between URLs
            time.sleep(1)

    print(f"\nAll done! Check your file: {filename}")

if __name__ == "__main__":
    scrape_multiple_to_excel()