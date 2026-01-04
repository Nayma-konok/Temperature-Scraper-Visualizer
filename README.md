# Temperature Scraper & Visualizer  

A Python project that scrapes temperature data from online sources, stores it with timestamps, and visualizes historical trends through an interactive dashboard using Streamlit and Plotly. 
This project demonstrates data collection, cleaning, and visualization skills in a practical, real-world workflow.  

## Features  
• Scrapes temperature data with timestamps from a web source.  
• Prevents duplicate entries to maintain data accuracy.  
• Stores data in a .txt file for analysis and tracking.  
• Interactive line chart visualization to explore historical temperature trends.  
• Built using Python libraries: requests, pandas, streamlit, and plotly.  

## Technologies Used
• Python – Core programming
• Pandas – Data handling and transformation
• Requests – Web scraping
• Plotly & Streamlit – Interactive data visualization and dashboard
• .txt – Data storage

## Usage
• The app scrapes the latest temperature data when run the dashboard.  
• Data is automatically stored in `temp_data.txt`.  
• Interactive charts allow you to explore trends over time.  

## How It Works
Collect temperature from a website.  
Clean and organize the data (remove duplicates, add timestamps).  
Save the data in a .txt file.  
Show the data in a chart that you can interact with.  

## How to Run
1. Clone the project:
```bash 
git clone https://github.com/Nayma-konok/Temperature-Scraper-Visualizer.git
```
2. Go to the folder:
```bash
cd Temperature-Scraper-Visualizer
```
3. Install packages:
```bash
pip install -r requirements.txt
```
4. Run the dashboard:
```bash
streamlit run app.py
```

## Project Structure
```graphql
Temperature-Scraper-Visualizer/
│
├── webapp.py           # Main Streamlit dashboard
├── temp.py             # Code for scraping or processing temperature data
├── temp_data.txt       # File that stores collected temperature data
├── extract1.yaml       # Scraper configuration
└── README.md           # Project description   
```

## What I Learned
• How to collect data from websites (web scraping)  
• How to clean and save data (data handling)  
• How to make charts and dashboards (data visualization)  
• How a simple data pipeline works: collect → clean → save → show  






