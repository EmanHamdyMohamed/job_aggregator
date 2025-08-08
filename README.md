# 💼 Job Aggregator

A modern web application that aggregates job listings from multiple sources, providing a unified interface for job seekers to search and discover opportunities with intelligent filtering capabilities.

## 🚀 Features

- **Multi-Source Job Aggregation**: Collects job listings from various platforms
- **Smart Search & Filtering**: Advanced filtering by work type, country, and salary range
- **Real-time Search**: Search jobs by title, keywords, or skills
- **Modern Web Interface**: Built with Streamlit for a clean, responsive UI
- **Work Type Filtering**: Filter by Remote Only, On-site Only, Hybrid, or All jobs
- **Global Country Selection**: Choose from 40+ countries or search worldwide
- **Salary Range Filtering**: Filter jobs by annual salary range with automatic parsing
- **Detailed Job Information**: Displays comprehensive job details including salary, location, and requirements

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Web Scraping**: BeautifulSoup4, Requests
- **Data Processing**: Pandas
- **Text Processing**: Regular Expressions (re)
- **Python**: 3.8+

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd job_aggregator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8501`

3. **Search for jobs**
   - Enter a job title or keyword in the search box
   - Use the sidebar filters to refine your search:
     - **Work Type**: Choose Remote Only, On-site Only, Hybrid, or All
     - **Country**: Select from 40+ countries or choose "All Countries"
     - **Salary Range**: Set your desired annual salary range
   - Click the "Search" button
   - Browse through the filtered results
   - View applied filters summary in the expandable section

## 📁 Project Structure

```
job_aggregator/
├── app.py                 # Main Streamlit application with smart filtering
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── scrapers/             # Web scraping modules
│   ├── __init__.py
│   ├── remoteok_scraper.py  # RemoteOK job scraper with enhanced parsing
│   └── base_scraper.py      # Base scraper class
├── services/             # Business logic services
│   ├── __init__.py
│   └── job_service.py
├── utils/                # Utility functions
│   ├── __init__.py
│   └── text_cleaner.py
└── data/                 # Data storage directory
```

## 🎯 Key Features Explained

### **Smart Filtering System**
- **Work Type Detection**: Automatically identifies remote jobs using keywords like "Remote", "Anywhere", "Worldwide"
- **Country Matching**: Case-insensitive country name matching across 40+ countries
- **Salary Parsing**: Extracts numeric values from salary strings for range filtering
- **Combined Filters**: All filters work together for precise job matching

### **Enhanced User Experience**
- **Sidebar Filters**: Clean, organized filtering interface
- **Filter Summary**: Shows applied filters in an expandable section
- **Results Counter**: Displays number of jobs found
- **Improved Data Display**: Better formatted dataframe with proper column widths
- **Direct Application Links**: Clickable links to job applications

## 🔧 Configuration

The application is configured to use wide layout mode for better display of job listings. You can modify the following settings in `app.py`:

- **Page title and icon**: Customize the browser tab display
- **Layout width**: Adjust the container width for different screen sizes
- **Search interface**: Modify the column proportions for the search form
- **Filter options**: Add or modify countries, work types, and salary ranges
- **Salary parsing**: Adjust the regex patterns for salary extraction

## 📊 Data Sources

Currently supported job sources:
- **RemoteOK**: Remote job listings with salary information
- More sources coming soon...

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Known Issues

- Some job listings may not display salary information if the source doesn't provide it
- Web scraping may be affected by website structure changes
- Salary parsing may not work for all salary formats (currently optimized for USD)
- Country filtering relies on location text matching and may miss some variations

## 🔮 Future Enhancements

- [x] ✅ Smart filtering by work type (Remote/On-site/Hybrid)
- [x] ✅ Country-based filtering with 40+ countries
- [x] ✅ Salary range filtering with automatic parsing
- [x] ✅ Enhanced UI with sidebar filters and results summary
- [ ] Add more job sources (LinkedIn, Indeed, etc.)
- [ ] Implement experience level filtering
- [ ] Add job application tracking
- [ ] Email notifications for new job matches
- [ ] Advanced search with multiple keywords
- [ ] Job recommendations based on user preferences
- [ ] Save and load filter preferences
- [ ] Export filtered results to CSV/PDF
- [ ] Job alerts for specific criteria

## 📞 Support

For questions, issues, or contributions, please open an issue on the GitHub repository.
