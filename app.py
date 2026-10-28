"""
Personal Portfolio Web Application - Python Flask
Experiment No. 12: Simple Web Application Using Flask

Aim:
To build a simple, responsive, and functional personal portfolio website
using the Flask micro-framework and Jinja2 templating.
"""

from flask import Flask, render_template, request, flash, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Secret key required for managing session data and flash messages
app.secret_key = "portfolio_secret_key_exp12"


# -----------------------------------------------------------------------------
# Home Route (GET)
# -----------------------------------------------------------------------------
@app.route("/")
def home():
    """
    Renders the Home page.
    Introduces the student with a hero section and call-to-action buttons.
    """
    return render_template("index.html")


# -----------------------------------------------------------------------------
# About Route (GET)
# -----------------------------------------------------------------------------
@app.route("/about")
def about():
    """
    Renders the About Me page.
    Displays education background, technical skills, and interests.
    """
    return render_template("about.html")


# -----------------------------------------------------------------------------
# Projects Route (GET)
# -----------------------------------------------------------------------------
@app.route("/projects")
def projects():
    """
    Renders the Projects page.
    Passes a list of project dictionaries to demonstrate Jinja2 templating loops.
    """
    # Sample projects data (can be easily edited or extended)
    projects_list = [
        {
            "title": "College Management & Student Portal",
            "description": "A comprehensive web portal for managing students, course enrollments, attendance, and administrative records with role-based access.",
            "tech_stack": ["Python", "Flask", "SQLite", "HTML/CSS"],
            "category": "Full-Stack Web App"
        },
        {
            "title": "Machine Learning Operations & Classifier",
            "description": "Supervised machine learning pipeline utilizing Scikit-Learn to preprocess datasets, train multi-class classifiers, and evaluate model accuracy.",
            "tech_stack": ["Python", "Scikit-Learn", "Pandas", "Matplotlib"],
            "category": "Machine Learning"
        },
        {
            "title": "Interactive GUI Task & To-Do Manager",
            "description": "Desktop productivity application featuring dynamic task creation, status toggles, deletion, and persistent state management.",
            "tech_stack": ["Python", "Tkinter", "File I/O"],
            "category": "Desktop GUI"
        },
        {
            "title": "Personal Portfolio Website",
            "description": "A clean, responsive multi-page personal portfolio developed using Flask, Jinja2 template inheritance, and vanilla CSS3.",
            "tech_stack": ["Python", "Flask", "Jinja2", "CSS3"],
            "category": "Web Development"
        }
    ]

    return render_template("projects.html", projects=projects_list)


# -----------------------------------------------------------------------------
# Contact Route (GET & POST)
# -----------------------------------------------------------------------------
@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Handles both displaying the contact form (GET)
    and processing submitted form data (POST) with validation.
    """
    if request.method == "POST":
        # Extract form inputs
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Basic server-side validation: ensure fields are not empty
        if not name or not email or not message:
            flash("Please fill in all fields before submitting.", "error")
            return render_template("contact.html", name=name, email=email, message=message)

        # Successful submission feedback (no real email sending required)
        flash(f"Thank you, {name}! Your message has been received successfully.", "success")
        return redirect(url_for("contact"))

    # Render clean contact form for GET request
    return render_template("contact.html")


# -----------------------------------------------------------------------------
# Application Entry Point
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # debug=True allows automatic reloading on code changes and provides a debugger
    app.run(debug=True, host="127.0.0.1", port=5000)
