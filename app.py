from flask import Flask, render_template, request, jsonify
import sqlite3
from database import init_db, add_candidate, get_candidates, add_query, get_queries

app = Flask(__name__)

# Initialize the database
init_db()

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
        skills = request.form['skills']
        add_candidate(name, email, skills)
        return jsonify({'message': 'Candidate added successfully'})
    candidates_list = get_candidates()
    return render_template('candidates.html', candidates=candidates_list)

# Employee Support: View and submit queries
@app.route('/employee_support', methods=['GET', 'POST'])
def employee_support():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        query_text = request.form['query']
        # Simple AI response simulation
        response = f"Received query: {query_text}. Our team will follow up soon."
        add_query(employee_name, query_text, response)
        return jsonify({'response': response})
    queries = get_queries()
    return render_template('employee_support.html', queries=queries)

# Analytics: Basic workforce insights
@app.route('/analytics')
def analytics():
    candidates = get_candidates()
    queries = get_queries()
    total_candidates = len(candidates)
    total_queries = len(queries)
    skills_count = {}
    for candidate in candidates:
        for skill in candidate[3].split(','):
            skill = skill.strip()
            skills_count[skill] = skills_count.get(skill, 0) + 1
    return render_template('analytics.html', total_candidates=total_candidates, total_queries=total_queries, skills_count=skills_count)

if __name__ == '__main__':
    app.run(debug=True)