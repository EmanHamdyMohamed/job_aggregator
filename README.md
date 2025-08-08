# 💼 Job Aggregator

A modern web application that aggregates job listings from multiple sources, providing a unified interface for job seekers to search and discover remote opportunities.

## 🚀 Features

- **Multi-Source Job Aggregation**: Collects job listings from various platforms
- **Real-time Search**: Search jobs by title, keywords, or skills
- **Modern Web Interface**: Built with Streamlit for a clean, responsive UI
- **Remote Job Focus**: Specialized in remote and work-from-home opportunities
- **Detailed Job Information**: Displays comprehensive job details including salary, location, and requirements

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Web Scraping**: BeautifulSoup4, Requests
- **Data Processing**: Pandas
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
   - Click the "Search" button
   - Browse through the results

## 📁 Project Structure

```
job_aggregator/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── scrapers/             # Web scraping modules
│   ├── __init__.py
│   ├── remoteok_scraper.py  # RemoteOK job scraper
│   └── base_scraper.py      # Base scraper class
├── services/             # Business logic services
│   ├── __init__.py
│   └── job_service.py
├── utils/                # Utility functions
│   ├── __init__.py
│   └── text_cleaner.py
└── data/                 # Data storage directory
```

## 🔧 Configuration

The application is configured to use wide layout mode for better display of job listings. You can modify the following settings in `app.py`:

- **Page title and icon**: Customize the browser tab display
- **Layout width**: Adjust the container width for different screen sizes
- **Search interface**: Modify the column proportions for the search form

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

## 🔮 Future Enhancements

- [ ] Add more job sources (LinkedIn, Indeed, etc.)
- [ ] Implement job filtering by location, salary range, and experience level
- [ ] Add job application tracking
- [ ] Email notifications for new job matches
- [ ] Advanced search with multiple keywords
- [ ] Job recommendations based on user preferences

## 📞 Support

For questions, issues, or contributions, please open an issue on the GitHub repository.
