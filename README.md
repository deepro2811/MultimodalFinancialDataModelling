# Multimodal Financial Data Modelling

A comprehensive project for collecting, analyzing, and modeling financial data from the National Stock Exchange (NSE) of India using multimodal approaches.

## Overview

This project focuses on multimodal financial data analysis, combining traditional numerical financial data with alternative data sources to build predictive models for stock market analysis.

## Features

- **NSE Index Data Collection**: Automated collection of current constituents from major NSE indices (NIFTY 50, NIFTY MIDCAP 150, NIFTY SMALLCAP 250, NIFTY 100)
- **Financial Data Analysis**: Comprehensive analysis of stock returns, volatility, and momentum indicators
- **Multimodal Modeling**: Integration of multiple data sources for enhanced prediction capabilities

## Project Structure

```
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore patterns
├── index.ipynb              # NSE index data collection utilities
└── dissertation.ipynb       # Main analysis and modeling notebook
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/deepro2811/MultimodalFinancialDataModelling.git
cd MultimodalFinancialDataModelling
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Data Collection

The `index.ipynb` notebook contains the `IndexConstituentsCollector` class for fetching current NSE index constituents:

```python
from index import IndexConstituentsCollector

# Initialize collector
collector = IndexConstituentsCollector()

# Get all unique stocks across indices
stocks = collector.get_all_unique_stocks()

# Get constituents for specific indices
constituents = collector.get_all_indices()
```

### Analysis

Open and run the `dissertation.ipynb` notebook for comprehensive financial data analysis and modeling.

## Data Sources

- **NSE India**: Live index constituents and stock data
- **Financial APIs**: Additional market data and indicators

## Requirements

- Python 3.9+
- See `requirements.txt` for detailed package dependencies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational and research purposes.

## Disclaimer

This project is for educational purposes only. Do not use this for actual trading decisions. Past performance does not guarantee future results.