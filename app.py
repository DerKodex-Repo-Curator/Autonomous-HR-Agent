from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS candidates
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  resume_text TEXT NOT NULL,
                  skills TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS queries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  employee_name TEXT NOT NULL,
                  query_text TEXT NOT NULL,
                  response TEXT NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

# Simple keyword-based skill extraction
def extract_skills(resume_text):
    skill_keywords = ['python', 'java', 'sql', 'javascript', 'management', 'communication']
    found_skills = [skill for skill in skill_keywords if skill.lower() in resume_text.lower()]
    return ', '.join(found_skills) if found_skills else 'None'

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Recruitment: View and add candidates
@app.route('/candidates', methods=['GET', 'POST'])
def candidates():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resume_text = request.form['resume_text']
        skills = extract_skills(resume_text)
        conn = sqlite3.connect('hr_database.db')
        c = conn.cursor()
        c.execute("INSERT INTO candidates (name, email, resume_text, skills) VALUES (?, ?, ?, ?)",
                  (name, email, resume_text, skills))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Candidate added successfully', 'skills': skills})
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM candidates")
    candidates_list = c.fetchall()
    conn.close()
    return render_template('candidates.html', candidates=candidates_list)

# Employee Support: View and submit queries
@app.route('/employee_support', methods=['GET', 'POST'])
def employee_support():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        query_text = request.form['query']
        # Mock AI response
        response = f"Received query: {query_text}. Suggested action: Check HR portal or contact HR team."
        conn = sqlite3.connect('hr_database.db')
        c = conn.cursor()
        c.execute("INSERT INTO queries (employee_name, query_text, response) VALUES (?, ?, ?)",
                  (employee_name, query_text, response))
        conn.commit()
        conn.close()
        return jsonify({'response': response})
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM queries")
    queries = c.fetchall()
    conn.close()
    return render_template('employee_support.html', queries=queries)

# Analytics: Basic workforce insights
@app.route('/analytics')
def analytics():
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM candidates")
    candidates = c.fetchall()
    c.execute("SELECT * FROM queries")
    queries = c.fetchall()
    conn.close()
    total_candidates = len(candidates)
    total_queries = len(queries)
    chart_config = {
        "type": "bar",
        "data": {
            "labels": ["Candidates", "Queries"],
            "datasets": [{
                "label": "Counts",
                "data": [total_candidates, total_queries],
                "backgroundColor": ["#4CAF50", "#2196F3"],
                "borderColor": ["#388E3C", "#1976D2"],
                "borderWidth": 1
            }]
        },
        "options": {
            "scales": {
                "y": {
                    "beginAtZero": True
                }
            }
        }
    }
    return render_template('analytics.html', total_candidates=total_candidates, total_queries=total_queries, chart_config=chart_config)

if __name__ == '__main__':
    app.run(debug=True)
