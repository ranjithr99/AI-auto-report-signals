from flask import Flask, render_template, request, jsonify
import pandas as pd
from datetime import datetime
import io

app = Flask(__name__)

def generate_report(df):
    # Get the most recent date
    latest_date = df['Report_Date'].max()
    
    # Filter for the latest date
    latest_data = df[df['Report_Date'] == latest_date]
    
    # Calculate key metrics
    total_reports = len(latest_data)
    viewed_by_leadership = len(latest_data[latest_data['Leadership_Viewed'] == 'Yes'])
    unviewed = total_reports - viewed_by_leadership
    
    # Get positive feedback (👍)
    positive_feedback = len(latest_data[latest_data['Feedback'] == '👍'])
    
    # Get sections with significant changes (distinct)
    significant_changes = latest_data[latest_data['Changed_Since_Last_Week'] == 'Yes']['Section'].unique().tolist()
    
    # Get sections with blockers or risks (distinct)
    blockers = latest_data[latest_data['Section'].isin(['Blocked dependencies', 'Key risks'])]['Section'].unique().tolist()
    
    # Generate report sections
    report = {
        'date': latest_date,
        'metrics': {
            'total_reports': total_reports,
            'viewed_by_leadership': viewed_by_leadership,
            'unviewed': unviewed,
            'positive_feedback': positive_feedback
        },
        'significant_changes': significant_changes,
        'blockers': blockers,
        'sections': latest_data['Section'].unique().tolist()
    }
    
    return report

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and file.filename.endswith('.csv'):
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Generate the report
        report = generate_report(df)
        
        return jsonify(report)
    
    return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True) 