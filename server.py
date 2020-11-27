from flask import Flask, render_template, request, redirect
from markupsafe import escape
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# storing to a database1
def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

# storing to a database2


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not stored into the database,something wrong happened"
    else:
        return "something wrong happened"


"""
@app.route('/works.html')
def works():
    return render_template("works.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/components.html")
def components():
    return render_template("components.html")


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/users/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

"""
