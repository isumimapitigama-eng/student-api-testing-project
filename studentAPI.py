from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice", "age": 21, "major": "Information Systems"},
    {"id": 2, "name": "Bob", "age": 23, "major": "Management"}
]

@app.route('/')
def home():
    return "Welcome to the Student API!"

@app.route('/ui')
def ui():
    return render_template("index.html")

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    return jsonify(student) if student else ("Student not found", 404)

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.json
    new_student['id'] = students[-1]['id'] + 1 if students else 1
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        data = request.json
        student.update(data)
        return jsonify(student)
    return ("Student not found", 404)

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return ("", 204)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')