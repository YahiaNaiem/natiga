from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Function to get student results by seating_no
def get_student_results(seating_no):
    conn = sqlite3.connect('F:/Results/students.db')  # Path to your SQLite database
    cursor = conn.cursor()
    cursor.execute("SELECT arabic_name, total_degree, student_case, student_case_desc, c_flage FROM students WHERE seating_no=?", (seating_no,))
    results = cursor.fetchone()
    conn.close()
    return results

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for fetching results
@app.route('/results', methods=['POST'])
def results():
    seating_no = request.form['seating_no']
    student_results = get_student_results(seating_no)
    return render_template('results.html', results=student_results)

if __name__ == '__main__':
    app.run(debug=True)
