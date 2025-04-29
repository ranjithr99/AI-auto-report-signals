# AI Report Generator

A modern web application that transforms CSV data into concise, leader-friendly reports. The application processes report data and presents key metrics, changes, and blockers in a clean, single-page format with interactive visualizations.

![Report Generator Screenshot](screenshot.png)

## Features

- 📊 **Interactive Dashboard**: Clean, modern interface with real-time data visualization
- 📈 **Visual Analytics**: Bar charts and metrics cards for quick insights
- 📁 **Easy File Upload**: Drag-and-drop CSV file upload with visual feedback
- 🔄 **Real-time Processing**: Instant report generation with loading indicators
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices

## Key Metrics Tracked

- Total Reports
- Reports Viewed by Leadership
- Unviewed Reports
- Positive Feedback Count
- Significant Changes
- Current Blockers and Risks

## Technical Stack

- **Backend**: Python/Flask
- **Frontend**: HTML5, JavaScript
- **Styling**: Tailwind CSS
- **Charts**: Chart.js
- **Data Processing**: Pandas

## Setup Instructions

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## CSV File Format

The application expects a CSV file with the following columns:
- `Report_Date`: Date of the report
- `Section`: Report section name
- `Submitted_By`: Who submitted the report
- `Leadership_Viewed`: Whether leadership viewed it (Yes/No)
- `Feedback`: Any feedback provided
- `Changed_Since_Last_Week`: Whether the section changed (Yes/No/Barely)

## Deployment Options

### Option 1: Deploy to Heroku

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Add gunicorn to requirements.txt:
```
gunicorn==20.1.0
```

3. Deploy to Heroku:
```bash
heroku create
git push heroku main
```

### Option 2: Deploy to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Flask and Python
- Styled with Tailwind CSS
- Charts powered by Chart.js
- Icons from Heroicons 