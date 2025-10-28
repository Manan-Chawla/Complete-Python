from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create SQLAlchemy instance
db = SQLAlchemy(app)


# api key
app.secret_key="manan@321"


# Define Model
class StudentProfile(db.Model):
    __tablename__ = 'student_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String(20), nullable=False)
    student_code = db.Column(db.String(20), unique=True, nullable=False)
    agree_terms = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Student {self.username} ({self.course})>"



# blog's model
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Blog {self.title}>"




# ---------------------- ROUTES ----------------------

@app.route("/")
def main():
    return render_template("base.html")


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        course = request.form.get("course")
        student_code = request.form.get("student_code")
        agree_terms = 'gridCheck' in request.form

        # Simple validation
        if not all([first_name, last_name, username, email, password, course, student_code]):
            flash("All fields are required!", "danger")
            return redirect(url_for("register"))

        # Check if username already exists
        existing_user = StudentProfile.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken! Try another.", "warning")
            return redirect(url_for("register"))

        new_student = StudentProfile(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            course=course,
            student_code=student_code,
            agree_terms=agree_terms
        )

        db.session.add(new_student)
        db.session.commit()

        flash("Registration successful!", "success")
        return redirect(url_for("index"))

    return render_template("register.html")



# routes for blog model

# create 
@app.route("/add_blog", methods=["GET", "POST"])
def add_blog():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        author = request.form["author"]

        new_blog = Blog(title=title, content=content, author=author)
        db.session.add(new_blog)
        db.session.commit()

        flash("Blog added successfully!", "success")
        return redirect(url_for("blogs"))

    return render_template("add_blog.html")



# read
@app.route("/blogs")
def blogs():
    all_blogs = Blog.query.all()
    return render_template("blogs.html", blogs=all_blogs)


# udpate
@app.route("/edit_blog/<int:id>", methods=["GET", "POST"])
def edit_blog(id):
    blog = Blog.query.get_or_404(id)
    if request.method == "POST":
        blog.title = request.form["title"]
        blog.content = request.form["content"]
        blog.author = request.form["author"]

        db.session.commit()
        flash("Blog updated successfully!", "info")
        return redirect(url_for("blogs"))

    return render_template("edit_blog.html", blog=blog)


# delete
@app.route("/delete_blog/<int:id>")
def delete_blog(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    flash("Blog deleted successfully!", "danger")
    return redirect(url_for("blogs"))




@app.route("/contact")
def contact():
    return render_template("contact.html")


# Run the app and create database
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
