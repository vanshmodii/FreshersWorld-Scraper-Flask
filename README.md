# FreshersWorld Job Scraper (Flask Web App)

This project is a **web scraping application** built with Flask and BeautifulSoup/Selenium. It allows users to **search for jobs** on FreshersWorld based on **job title** and **location**, and then download the results in an **Excel file**.

## 🚀 Features
- 🏢 **Scrapes job listings** from FreshersWorld.
- 🔍 **User input** for job title and location.
- 📊 **Exports job data** (Company Name, Job Title, Salary, Experience, etc.) to an Excel file.
- 🌐 **Flask-based Web App** with a simple UI.
- 📅 **Daily updates** with new job postings.

## 🛠️ Tech Stack
- **Backend**: Flask (Python)
- **Web Scraping**: BeautifulSoup / Selenium
- **Frontend**: HTML, CSS
- **Data Storage**: Excel (Pandas)

## 📥 Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/vanshmodii/FreshersWorld-Scraper-Flask.git
cd FreshersWorld-Scraper-Flask
2️⃣ Set Up a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Flask App
sh
Copy
Edit
python app.py
Then, open http://127.0.0.1:5000/ in your browser.

📸 Screenshots
![Screenshot 2025-03-23 155900](https://github.com/user-attachments/assets/686beb41-de0b-43f1-afd2-efd56b67c41e)
![Screenshot 2025-03-23 155958](https://github.com/user-attachments/assets/df0a7bda-f201-42b6-9e08-84b276222d86)


📝 Usage
Enter the job title and location.

Click "Scrape Jobs".

The job results will appear on the webpage.

Click "Download Excel" to get the job listings.

🚀 Deployment
(Add deployment details if hosted on Render, Railway, etc.)

🤝 Contributing
Feel free to fork the repository, make improvements, and submit pull requests!
