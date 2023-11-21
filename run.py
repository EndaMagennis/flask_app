import os
import json
# Check if env.py file exists and import it
if os.path.exists("env.py"):
    import env

from flask import Flask, render_template, request, flash

# Initialize Flask app
app = Flask(__name__)
# Get secret key from environment variables
app.secret_key = os.environ.get("SECRET_KEY")


# Define route for home page
@app.route("/")
def index():
    return render_template("index.html")


# Define route for about page
@app.route("/about")
def about():
    data = []
    # Open and read the company.json file
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # Render the about page and pass the company data to it
    return render_template("about.html", page_title="About", company=data)


# Define route for contact page, allowing both GET and POST requests
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # If the request method is POST, flash a thank you message
    if request.method == "POST":
        # Flash a thank you message, getting the name from the form data
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    # Render the contact.html template, passing in the page title
    return render_template("contact.html", page_title="Contact")

# Define a route for the careers page


@app.route("/careers")
def careers():
    # Render the careers.html template, passing in the page title
    return render_template("careers.html", page_title="Careers")

# Define a route for the about page for a specific member


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    # Open the company.json file in read mode
    with open("data/company.json", "r") as json_data:
        # Load the JSON data from the file
        data = json.load(json_data)
        # Loop through each object in the data
        for obj in data:
            # If the url field of the object matches the member name
            if obj["url"] == member_name:
                # Set the member variable to the current object
                member = obj
    # Render the member.html template, passing in the member data
    return render_template("member.html", member=member)


# If this script is run directly (not imported)
if __name__ == "__main__":
    # Run the Flask app
    app.run(
        # Get the IP address from the environment variables, default 0.0.0.0
        host=os.environ.get("IP", "0.0.0.0"),
        # Get the port number from the environment variables, default 5000
        port=int(os.environ.get("PORT", "5000")),
        # Enable debug mode
        debug=True)
