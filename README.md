# free-courses-scraper

# 🎓 Free Courses Scraper

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![Scrapy](https://img.shields.io/badge/scrapy-2.11-green)](https://scrapy.org/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **A powerful Scrapy-based web scraper with intelligent search capabilities to extract and find Udemy free courses from answersQ.com**

Extract hundreds of free Udemy courses daily with coupon codes and search through them efficiently using fuzzy matching, keyword search, and category-based browsing.

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
  - [Running the Scraper](#1-running-the-scraper)
  - [Searching Courses](#2-searching-courses)
  - [Command Line Search](#3-command-line-search)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Search Features](#-search-features)
- [Output Formats](#-output-formats)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Disclaimer](#-disclaimer)

---

## ✨ Features

### 🕷️ Scraping Capabilities

- ✅ Extracts course **titles**, **URLs**, and **publication dates**
- ✅ Exports to **JSON** and **CSV** formats simultaneously
- ✅ Handles 300+ courses per run
- ✅ Respects rate limiting and delays
- ✅ User-agent rotation ready

### 🔍 Search Capabilities

- ✅ **Fuzzy matching** - finds courses even with typos (e.g., "Pyhton" → "Python")
- ✅ **Multi-keyword search** - combine keywords with AND logic
- ✅ **Category-based browsing** - automatically categorizes courses
- ✅ **Relevance scoring** - shows match percentage
- ✅ **Smart sorting** - best matches displayed first
- ✅ **Interactive CLI** - user-friendly menu system

### 📊 Supported Categories

- Python Programming
- JavaScript & Node.js
- Microsoft Excel & VBA
- Graphic Design (Photoshop, Illustrator, Canva)
- Video Editing (Premiere Pro, After Effects)
- AI & Machine Learning
- Business & Management
- Web Development
- Cloud Computing (AWS, Azure, GCP)
- Cybersecurity
- And many more...

---

## 🎬 Demo

```bash
$ python search_courses.py

====================================================================================================
                               UDEMY FREE COURSES SEARCH TOOL
====================================================================================================
✓ Loaded 312 courses

Options:
1. Search by keyword/name
2. Search by multiple keywords (comma-separated)
3. Browse by category
4. Show all courses
5. Exit

Enter your choice (1-5): 1

Enter search term: Python Machine Learning

====================================================================================================
Found 15 courses (showing top 15)
====================================================================================================

1. Machine Learning – Fundamental of Python Machine Learning
   Match: 95.2% | Date: Udemy Free Courses for 11 November 2025
   URL: https://www.udemy.com/course/machine-learning-fundamental...
   --------------------------------------------------------------------------------------------------

2. Master Python for Data Science, Machine Learning, Automation
   Match: 88.7% | Date: Udemy Free Courses for 11 November 2025
   URL: https://www.udemy.com/course/master-python-for-data-science...
   --------------------------------------------------------------------------------------------------
```

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Step 1: Clone the Repository

```bash
git clone https://github.com/AbdulmalikAlayande/free-courses-scraper.git
cd udemy-courses-scraper
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
scrapy>=2.11.0
```

If `requirements.txt` doesn't exist, install Scrapy directly:

```bash
pip install scrapy
```

---

## ⚡ Quick Start

### 1. Run the Scraper

```bash
# Navigate to project directory
cd free_courses_scraper

# Run the spider
scrapy crawl courses
```

**Output:** Creates `courses.json` and `courses.csv` in the current directory.

### 2. Search Courses

```bash
# Interactive search
python search_courses.py
```

### 3. One-Line Search (Advanced)

```bash
# Search from command line
python -c "from search_courses import CourseSearcher; s = CourseSearcher(); s.display_results(s.search('Python'))"
```

---

## 📖 Usage

### 1. Running the Scraper

#### Basic Usage

```bash
scrapy crawl courses
```

#### Custom Output File

```bash
scrapy crawl courses -o my_courses.json
```

#### Specific Format

```bash
# JSON only
scrapy crawl courses -o courses.json -t json

# CSV only
scrapy crawl courses -o courses.csv -t csv

# JSON Lines
scrapy crawl courses -o courses.jsonl -t jsonlines
```

#### With Logging

```bash
# Minimal logging
scrapy crawl courses --loglevel=INFO

# Debug mode
scrapy crawl courses --loglevel=DEBUG

# Save logs to file
scrapy crawl courses --logfile=scraper.log
```

---

### 2. Searching Courses

#### Interactive Mode (Recommended)

```bash
python search_courses.py
```

**Available Options:**

1. **Search by keyword/name** - Single keyword search with fuzzy matching
2. **Search by multiple keywords** - Comma-separated keywords (AND logic)
3. **Browse by category** - View courses grouped by topic
4. **Show all courses** - Display all scraped courses
5. **Exit** - Close the program

#### Example Sessions

**Example 1: Single Keyword Search**

```
Enter your choice (1-5): 1
Enter search term: Excel
```

Finds all Excel-related courses with relevance scoring.

**Example 2: Multiple Keywords**

```
Enter your choice (1-5): 2
Enter keywords (comma-separated): Python, Machine Learning, Beginner
```

Finds courses containing ALL specified keywords.

**Example 3: Browse Categories**

```
Enter your choice (1-5): 3
```

Displays courses organized by categories with counts.

---

### 3. Command Line Search

#### Python API

```python
from search_courses import CourseSearcher

# Initialize searcher
searcher = CourseSearcher('courses.json')

# Simple search
results = searcher.search('Python')
searcher.display_results(results)

# Multi-keyword search
results = searcher.search_by_keywords('Excel, Advanced, VBA')
searcher.display_results(results)

# Get categories
categories = searcher.search_by_category()
searcher.display_categories(categories)

# Access raw data
for result in results:
    course = result['course']
    print(f"{course['title']}: {course['url']}")
```

#### One-Liners

```bash
# Search for Python courses
python -c "from search_courses import CourseSearcher; s=CourseSearcher(); s.display_results(s.search('Python'), limit=10)"

# Search with multiple keywords
python -c "from search_courses import CourseSearcher; s=CourseSearcher(); s.display_results(s.search_by_keywords('AI, ChatGPT'))"

# Show categories
python -c "from search_courses import CourseSearcher; s=CourseSearcher(); s.display_categories(s.search_by_category())"
```

---

## 📁 Project Structure

```
udemy-courses-scraper/
│
├── free_courses_scraper/                 # Main Scrapy project directory
│   ├── __init__.py
│   ├── items.py                   # Data models for scraped items
│   ├── middlewares.py             # Custom middlewares (optional)
│   ├── pipelines.py               # Data processing pipelines
│   ├── settings.py                # Scrapy configuration
│   │
│   └── spiders/                   # Spider directory
│       ├── __init__.py
│       └── courses_spider.py      # Main spider for scraping courses
│
├── scrapy.cfg                     # Scrapy deployment configuration
├── search_courses.py              # Interactive search tool
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── LICENSE                        # License file
├── .gitignore                     # Git ignore rules
│
└── output/                        # Generated output (not in repo)
    ├── courses.json              # JSON output
    ├── courses.csv               # CSV output
    └── scraper.log               # Log file (optional)
```

---

## ⚙️ Configuration

### Scrapy Settings (`free_courses_scraper/settings.py`)

```python
# Bot identification
BOT_NAME = 'free_courses_scraper'

# Obey robots.txt (set to False for this use case)
ROBOTSTXT_OBEY = False

# Download delays (be respectful)
DOWNLOAD_DELAY = 1                 # 1 second between requests
CONCURRENT_REQUESTS = 1            # One request at a time

# User agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

# Output settings
FEEDS = {
    'courses.json': {
        'format': 'json',
        'encoding': 'utf8',
        'overwrite': True,
        'indent': 4
    },
    'courses.csv': {
        'format': 'csv',
        'encoding': 'utf8',
        'overwrite': True
    }
}
```

### Customize Search Thresholds

Edit `search_courses.py`:

```python
# Minimum similarity score (0.0 - 1.0)
results = searcher.search('Python', min_score=0.3)  # Default: 0.3

# Change result limit
searcher.display_results(results, limit=50)  # Default: 20
```

---

## 🔍 Search Features

### 1. Fuzzy Matching

Uses `SequenceMatcher` to find similar course names:

```python
# Will match:
"Python" → "Python Programming", "Learn Python", "Python Complete"
"Exel" → "Excel", "Microsoft Excel"  # Typo tolerance
```

### 2. Multi-Keyword Search

Combines multiple keywords with AND logic:

```python
"Python, Machine Learning"
# Matches only courses containing BOTH keywords
```

### 3. Category Auto-Detection

Automatically categorizes courses based on keywords:

| Category      | Keywords                                     |
| ------------- | -------------------------------------------- |
| Python        | python                                       |
| JavaScript    | javascript, js, node, react, vue             |
| Excel         | excel, spreadsheet                           |
| Design        | photoshop, illustrator, canva, figma, design |
| Video Editing | premiere, after effects, filmora, capcut     |
| AI & ML       | ai, machine learning, chatgpt, deep learning |
| Business      | business, management, leadership, marketing  |
| Cloud         | aws, azure, cloud, gcp                       |

### 4. Relevance Scoring

Each search result includes a match score (0-100%):

- **100%**: Exact match
- **80-99%**: Very similar
- **60-79%**: Somewhat similar
- **30-59%**: Loosely related

---

## 📊 Output Formats

### JSON Format (`courses.json`)

```json
[
	{
		"title": "Python Complete Course For Beginners",
		"url": "https://www.udemy.com/course/python-complete-course-for-beginners-h/?couponCode=...",
		"date": "Udemy Free Courses for 11 November 2025"
	},
	{
		"title": "Machine Learning – Fundamental of Python Machine Learning",
		"url": "https://www.udemy.com/course/machine-learning-fundamental...",
		"date": "Udemy Free Courses for 11 November 2025"
	}
]
```

### CSV Format (`courses.csv`)

```csv
title,url,date
"Python Complete Course For Beginners","https://www.udemy.com/course/...","Udemy Free Courses for 11 November 2025"
"Machine Learning Course","https://www.udemy.com/course/...","Udemy Free Courses for 11 November 2025"
```

---

## 💡 Examples

### Example 1: Find All Python Courses

```python
from search_courses import CourseSearcher

searcher = CourseSearcher()
results = searcher.search('Python')
searcher.display_results(results, limit=10)
```

### Example 2: Advanced Excel Courses

```python
results = searcher.search_by_keywords('Excel, Advanced, VBA')
for result in results[:5]:
    course = result['course']
    print(f"✓ {course['title']}")
    print(f"  {course['url']}\n")
```

### Example 3: AI & Machine Learning Courses

```python
results = searcher.search_by_keywords('AI, Machine Learning')
print(f"Found {len(results)} courses")

# Filter by high relevance
high_quality = [r for r in results if r['score'] > 0.7]
searcher.display_results(high_quality)
```

### Example 4: Export Category Summary

```python
categories = searcher.search_by_category()

# Save to file
with open('categories_summary.txt', 'w', encoding='utf-8') as f:
    for category, courses in sorted(categories.items()):
        f.write(f"\n{category}: {len(courses)} courses\n")
        f.write("=" * 50 + "\n")
        for course in courses[:10]:
            f.write(f"  - {course['title']}\n")
```

### Example 5: Automated Daily Scraping

Create a script `daily_scrape.sh`:

```bash
#!/bin/bash
cd /path/to/free-courses-scraper/free_courses_scraper
scrapy crawl courses --logfile=logs/scrape_$(date +%Y%m%d).log
echo "Scraping completed at $(date)"
```

Schedule with cron (Linux/macOS):

```bash
# Run daily at 9 AM
0 9 * * * /path/to/daily_scrape.sh
```

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'scrapy'`

**Solution:**

```bash
pip install scrapy
# Or with specific version
pip install scrapy==2.11.0
```

---

### Issue: `FileNotFoundError: courses.json not found`

**Solution:**

```bash
# Make sure you run the scraper first
cd free_courses_scraper
scrapy crawl courses

# Then run search from the same directory
python ../search_courses.py
```

---

### Issue: Spider not crawling

**Solution:**

1. Check your internet connection
2. Verify the website is accessible:
   ```bash
   curl -I https://answersq.com/udemy-paid-courses-for-free-with-certificate/
   ```
3. Try with increased verbosity:
   ```bash
   scrapy crawl courses --loglevel=DEBUG
   ```

---

### Issue: Empty results or partial data

**Solution:**

- Website structure may have changed
- Check the spider code in `courses_spider.py`
- Update CSS selectors if necessary
- Use Scrapy shell for debugging:
  ```bash
  scrapy shell "https://answersq.com/udemy-paid-courses-for-free-with-certificate/"
  ```

---

### Issue: Permission denied on Windows

**Solution:**

```bash
# Run as administrator or use:
python -m pip install --user scrapy
```

---

### Issue: SSL Certificate Error

**Solution:**
Add to `settings.py`:

```python
DOWNLOADER_CLIENT_TLS_METHOD = 'TLSv1.2'
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs

1. Check existing issues first
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and use case
3. Provide examples if possible

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/yourusername/udemy-courses-scraper.git
cd udemy-courses-scraper
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If you have dev dependencies
```

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**.

- This scraper is designed to help users discover free educational content
- Always respect the website's terms of service and robots.txt
- Use reasonable delays between requests to avoid overloading servers
- The courses are offered by Udemy, not by this scraper
- Course availability and coupons are subject to expire
- We are not affiliated with Udemy or answersQ.com

**Important Notes:**

- Coupons have limited redemptions (usually 1000 per coupon)
- Course prices and availability may change without notice
- Always verify the course is still free before enrolling
- This tool only extracts publicly available information

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/udemy-courses-scraper/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/udemy-courses-scraper/discussions)
- **Email:** your.email@example.com

---

## 🙏 Acknowledgments

- [Scrapy](https://scrapy.org/) - Web scraping framework
- [answersQ](https://answersq.com/) - Source of free course listings
- [Udemy](https://www.udemy.com/) - Educational platform
- Contributors and users of this project

---

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/udemy-courses-scraper?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/udemy-courses-scraper?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/udemy-courses-scraper)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/udemy-courses-scraper)

---

## 🗺️ Roadmap

- [ ] Add support for more course listing websites
- [ ] Implement email notifications for new courses
- [ ] Add course rating and review scraping
- [ ] Create web interface for searching
- [ ] Add course expiration tracking
- [ ] Implement course recommendations
- [ ] Add Docker support
- [ ] Create mobile app

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by [Your Name](https://github.com/yourusername)

[Report Bug](https://github.com/yourusername/udemy-courses-scraper/issues) · [Request Feature](https://github.com/yourusername/udemy-courses-scraper/issues)

</div>
