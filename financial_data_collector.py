"""
Multimodal Financial Data Modelling
===================================

A Python package for collecting and analyzing financial data from NSE India.
"""

import requests
import pandas as pd
import time
import os


class IndexConstituentsCollector:
    """Dynamically fetches current constituents of NSE indices"""
    
    def __init__(self, cache_dir="./data/index_data"):
        """Initialize the index constituents collector"""
        self.cache_dir = cache_dir
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        os.makedirs(self.cache_dir, exist_ok=True)
        
    def get_nse_index_constituents(self, index_name):
        """Fetch index constituents from NSE website"""
        # Format index name for URL
        formatted_index = index_name.replace(' ', '%20')
        url = f"https://www.nseindia.com/api/equity-stockIndices?index={formatted_index}"
        
        try:
            session = requests.Session()
            # First get cookies
            session.get("https://www.nseindia.com/", headers=self.headers)
            time.sleep(1)
            
            # Get actual data
            response = session.get(url, headers=self.headers)
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    df = pd.DataFrame(data['data'])
                    df['symbol_yf'] = df['symbol'] + '.NS'  # Add suffix for yfinance
                    print(f"Successfully fetched {len(df)} stocks for {index_name}")
                    return df
                else:
                    print(f"No data found for {index_name}")
            else:
                print(f"Failed to fetch {index_name}: {response.status_code}")
                
        except Exception as e:
            print(f"Error fetching {index_name}: {e}")
        
        return pd.DataFrame()
    
    def get_all_indices(self):
        """Get constituents for all configured indices"""
        indices = [
            'NIFTY 50',         # Large cap
            'NIFTY MIDCAP 150', # Mid cap
            'NIFTY SMALLCAP 250', # Small cap
            'NIFTY 100'         # Large cap expanded
        ]
        
        all_constituents = {}
        
        for index_name in indices:
            print(f"Fetching {index_name}...")
            df = self.get_nse_index_constituents(index_name)
            if not df.empty:
                all_constituents[index_name] = df
            time.sleep(2)  # Respect rate limits
        
        return all_constituents
        
    def get_all_unique_stocks(self):
        """Get a list of all unique stock symbols across all indices"""
        all_constituents = self.get_all_indices()
        all_stocks = set()
        
        for index_id, df in all_constituents.items():
            if 'symbol_yf' in df.columns:
                all_stocks.update(df['symbol_yf'].tolist())
        
        return list(all_stocks)


__version__ = "1.0.0"
__author__ = "DeepRo"
__email__ = "deepro2811@example.com"