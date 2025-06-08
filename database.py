import sqlite3

def init_db():
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    # Create candidates table
    c.execute('''CREATE TABLE IF NOT EXISTS candidates
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  skills TEXT NOT NULL)''')
    # Create queries table
    c.execute('''CREATE TABLE IF NOT EXISTS queries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  employee_name TEXT NOT NULL,
                  query_text TEXT NOT NULL,
                  response TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_candidate(name, email, skills):
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO candidates (name, email, skills) VALUES (?, ?, ?)",
              (name, email, skills))
    conn.commit()
    conn.close()

def get_candidates():
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM candidates")
    candidates = c.fetchall()
    conn.close()
    return candidates

def add_query(employee_name, query_text, response):
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO queries (employee_name, query_text, response) VALUES (?, ?, ?)",
              (employee_name, query_text, response))
    conn.commit()
    conn.close()

def get_queries():
    conn = sqlite3.connect('hr_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM queries")
    queries = c.fetchall()
    conn.close()
    return queries