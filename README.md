# Experiment No. 12: Simple Web Application Using Python Flask

## 📌 Aim
To build simple web applications using Django (full-stack framework) or Flask (lightweight micro-framework), such as building personal portfolio websites, developing content management systems (CMS), and rapid prototyping of web ideas.

---

## 🛠️ Technology Stack
- **Backend:** Python 3 &amp; Flask (Lightweight WSGI Micro-framework)
- **Frontend:** HTML5 &amp; CSS3 (Vanilla, Responsive, Minimalist Dark Slate Theme)
- **Templating Engine:** Jinja2 (Template inheritance, loops, conditionals)
- **Data Storage:** In-memory / stateless (No database required for this practical)
- **Editor / IDE:** Visual Studio Code

---

## 📁 Project Structure

```text
EXP12/
│
├── app.py                 # Flask server with routes, validation, and template rendering
├── requirements.txt       # Project dependencies (Flask)
├── run.bat                # Windows one-click launcher
├── README.md              # Complete experiment documentation & viva guide
│
├── templates/             # Jinja2 HTML templates
│   ├── base.html          # Master layout (navbar, flash alerts, footer, boilerplate)
│   ├── index.html         # Home page with hero section & highlights
│   ├── about.html         # About me (education, skills, interests)
│   ├── projects.html      # Projects showcase (dynamic rendering via Jinja2 loop)
│   └── contact.html       # Contact details & validated message form
│
└── static/
    └── style.css          # Modern, responsive vanilla CSS stylesheet
```

---

## 🚀 Execution & Setup Instructions

### 1. Open Terminal in `EXP12` Folder
In Visual Studio Code, open the integrated terminal (`Ctrl + ~`) and navigate to the project directory:
```bash
cd d:\Shaurya\College\DjSanghvi\sem3\PythonLab\EXP12
```

### 2. Create and Activate Virtual Environment
A virtual environment ensures project dependencies are isolated:
```bash
# Create virtual environment named 'venv'
python -m venv venv

# Activate on Windows (Command Prompt or PowerShell)
venv\Scripts\activate
```
*(On Windows PowerShell, if execution policy errors occur, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first)*

### 3. Install Dependencies
Install Flask using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server:
```bash
python app.py
```

### 5. Access the Website
Open any web browser and visit:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)** *(or `http://localhost:5000`)*

*(Alternatively, on Windows you can simply double-click **`run.bat`** to automate all the steps above!)*

---

## 🔍 How Flask Routes & Jinja2 Templates Work

### 1. Routes (`app.py`)
- **`@app.route("/")`**: The root route handles requests to the homepage and calls `render_template("index.html")`.
- **`@app.route("/about")`**: Delivers the educational and technical profile.
- **`@app.route("/projects")`**: Passes a Python list of dictionaries (`projects=projects_list`) into the template context.
- **`@app.route("/contact", methods=["GET", "POST"])`**:
  - `GET`: Displays the blank contact form.
  - `POST`: Extracts data from `request.form`, performs server-side validation to check that fields aren't empty, and uses `flash()` to display a feedback message.

### 2. Jinja2 Templating
- **Template Inheritance (`{% extends "base.html" %}`)**: Avoids duplicating common HTML (such as `<!DOCTYPE>`, `<head>`, `<nav>`, and `<footer>`) across multiple files.
- **Blocks (`{% block content %}`)**: Defines placeholders in `base.html` that child templates override with page-specific content.
- **Loops (`{% for project in projects %}`)**: Iterates through Python lists dynamically to generate project cards in `projects.html`.
- **Conditionals (`{% if request.endpoint == 'home' %}active{% endif %}`)**: Automatically highlights the current page link in the navigation bar.

---

## ✅ Testing Checklist
1. **Home Page (`/`)**: Verify that the hero greeting, student intro, and CTA buttons display properly.
2. **Navigation Bar**: Click on *Home*, *About*, *Projects*, and *Contact* links to ensure smooth transitions between pages and correct active link styling.
3. **About Page (`/about`)**: Verify personal overview, education timeline, technical skills badges, and interests.
4. **Projects Page (`/projects`)**: Verify that all 4 projects render dynamically with titles, descriptions, and technology tags.
5. **Contact Page (`/contact`)**:
   - **Empty Submission Test**: Try submitting the form without filling out fields &rarr; Browser and server validate and block empty submission.
   - **Valid Submission Test**: Fill in Name, Email, and Message and click *Send Message* &rarr; Page reloads with a green success alert banner: *"Thank you, [Name]! Your message has been received successfully."*
6. **Mobile Responsiveness**: Resize the browser window or test on a mobile viewport to confirm that the navbar, cards, and grid collapse into a single clean column.

---

## 🎓 Viva Questions & Answers (For College Lab Exam)

**Q1: What is Flask and why is it called a micro-framework?**  
*Answer:* Flask is a lightweight Python web framework based on Werkzeug (WSGI) and Jinja2. It is called a "micro-framework" because it does not enforce specific database tools, form libraries, or predefined directory structures, giving developers the flexibility to choose only the components they need.

**Q2: What is the difference between Django and Flask?**  
*Answer:* Django is an all-inclusive, "batteries-included" full-stack framework with built-in ORM, admin panel, authentication, and form handling. Flask is minimalist, lightweight, and ideal for microservices, small to medium web apps, and rapid prototyping.

**Q3: What is Jinja2 and how does template inheritance work?**  
*Answer:* Jinja2 is Python's templating engine. Template inheritance allows you to create a parent "skeleton" template (`base.html`) containing common layout elements, while child templates (`index.html`, etc.) extend it using `{% extends %}` and inject content into `{% block %}` sections.

**Q4: How does Flask handle GET vs POST requests?**  
*Answer:* By default, Flask routes handle `GET` requests. By specifying `methods=["GET", "POST"]` in `@app.route()`, the route can inspect `request.method` to distinguish between fetching a page (`GET`) and processing submitted form payloads (`POST`) via `request.form`.

**Q5: What is the role of `app.secret_key` in Flask?**  
*Answer:* `secret_key` is used to cryptographically sign session cookies and flash message payloads to prevent tampering by clients.
