# 🎓 Student Management API — Development & Testing

A RESTful Student Management API built with **Python (Flask)** and thoroughly tested using **Postman**. This project demonstrates end-to-end QA ownership: API design, CRUD implementation, manual test execution, and structured test documentation.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Author](#author)

---

## Overview

This project simulates a real-world QA workflow. A Student Management API was developed from scratch, then manually tested using Postman to validate:

- Correct HTTP status codes across all endpoints
- Accurate request/response payloads (JSON)
- Input validation and error handling
- Both positive and negative test scenarios

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | API development |
| Flask | Web framework |
| Postman | API testing & documentation |
| JSON | Data format |
| Visual Studio Code | Development environment |

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/isumimapitigama-eng/student-api-testing-project.git
cd student-api-testing-project

# Install dependencies
pip install -r requirement.txt

# Run the API
python studentAPI.py
```

The API will start at `http://localhost:5000`.

To open the UI, visit `http://localhost:5000/ui`.

---

## API Endpoints

### Base URL: `http://localhost:5000`

#### Get All Students
```
GET /students
```
**Response 200:**
```json
[
  { "id": 1, "name": "Alice", "age": 21, "major": "Information Systems" },
  { "id": 2, "name": "Bob", "age": 23, "major": "Management" }
]
```

---

#### Get Student by ID
```
GET /students/{id}
```
**Response 200:**
```json
{ "id": 1, "name": "Alice", "age": 21, "major": "Information Systems" }
```
**Response 404:** `Student not found`

---

#### Create Student
```
POST /students
Content-Type: application/json
```
**Request body:**
```json
{ "name": "Carol", "age": 22, "major": "Computer Science" }
```
**Response 201:**
```json
{ "id": 3, "name": "Carol", "age": 22, "major": "Computer Science" }
```

---

#### Update Student
```
PUT /students/{id}
Content-Type: application/json
```
**Request body:**
```json
{ "age": 24, "major": "Data Science" }
```
**Response 200:** Updated student object  
**Response 404:** `Student not found`

---

#### Delete Student
```
DELETE /students/{id}
```
**Response 204:** No content  

---

## Testing

Testing was performed manually using **Postman**, covering all CRUD endpoints with both positive and negative scenarios.

### Test Coverage Summary

| Endpoint | Method | Positive | Negative |
|----------|--------|----------|----------|
| `/students` | GET | ✅ | ✅ |
| `/students/{id}` | GET | ✅ | ✅ (invalid ID) |
| `/students` | POST | ✅ | ✅ (missing fields) |
| `/students/{id}` | PUT | ✅ | ✅ (non-existent ID) |
| `/students/{id}` | DELETE | ✅ | ✅ (non-existent ID) |

### Key Validations

- **Status codes** — 200, 201, 204, 404 verified for each scenario
- **Response body** — JSON structure and field values validated
- **Error handling** — Verified meaningful error messages for invalid requests
- **Data integrity** — Confirmed data persists correctly after POST and PUT

### Running the Postman Collection

1. Import `Student_Management_API.postman_collection.json` into Postman
2. Ensure the API is running locally on port 5000
3. Run the full collection using **Collection Runner**

Test case details are documented in `API Test Cases.xlsx`.

### Test Evidence

Screenshots of test executions are included in the repository:

| File | Description |
|------|-------------|
| `GET-positive test case.png` | GET request returning valid student |
| `GET-Negative test case.png` | GET request with invalid student ID |
| `POST-positive test case.png` | Successful student creation |
| `PUT-positive test case.png` | Successful student update |
| `PUT negative test case.png` | PUT request with non-existent ID |

---

## Project Structure

```
student-api-testing-project/
├── studentAPI.py                              # Flask REST API
├── requirement.txt                            # Python dependencies
├── index.html                                 # Simple UI
├── API Test Cases.xlsx                        # Full test case documentation
├── Student_Management_API.postman_collection.json  # Postman collection
├── GET-positive test case.png
├── GET-Negative test case.png
├── POST- positive test case.png
├── PUT-positive test case.png
├── PUT negative test case.png
├── .gitignore
└── README.md
```

---

## Author

**Isumi Mapitigama**  
Information Systems Undergraduate — Rajarata University of Sri Lanka  
[LinkedIn](https://linkedin.com/in/isumi-mapitigama) · [GitHub](https://github.com/isumimapitigama-eng)
