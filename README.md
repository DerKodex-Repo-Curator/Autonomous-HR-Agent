### How to Run the Project
1. **Set up the environment**:
   - Install Python (3.8 or higher).
   - Create a project directory and save all files in the structure shown above.
   - Install dependencies: Run `pip install -r requirements.txt` in the project directory.

2. **Run the application**:
   - Navigate to the project directory in a terminal.
   - Run `python app.py`.
   - Open a browser and go to `http://localhost:5000`.

3. **Using the application**:
   - **Home**: Overview of the HR Agent.
   - **Recruitment**: Add candidates with name, email, and skills; view the candidate list.
   - **Employee Support**: Submit employee queries and view responses (simulated AI responses for simplicity).
   - **Analytics**: View total candidates, queries, and skills distribution.

### Features Implemented
- **Recruitment**: Add and view candidates with a simple form and table.
- **Employee Support**: Submit queries with a simulated AI response stored in the database.
- **Analytics**: Basic insights like candidate count, query count, and skills distribution.
- **Workflow Automation**: Simplified to database storage for candidates and queries (onboarding and payroll can be extended similarly).
- **Benefits**: The app reduces manual work by storing and displaying data, minimizes bias by standardizing inputs, and can scale with more features.

### Notes for Beginners
- **Flask**: A lightweight Python web framework for building the backend.
- **SQLite**: A simple database for storing candidates and queries.
- **HTML/CSS/JavaScript**: Basic frontend for user interaction.
- **Extensibility**: You can add features like resume parsing (using libraries like `PyPDF2`) or advanced AI responses (using APIs like xAI’s Grok API, see https://x.ai/api).

This project provides a foundation you can build upon. Let me know if you want to add specific features or need help running it!