from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  title = "Siri Herbal Beauty Parlour"
  return render_template('home.html', title=title)

@app.route("/services")
def services():
  title = "SERVICES — Siri"
  return render_template('services.html', title=title)

@app.route("/about")
def about():
  title = "ABOUT — Siri"
  return render_template('about.html', title=title)

@app.route("/gallery")
def gallery():
  title = "GALLERY — Siri"
  return render_template('gallery.html', title=title)

@app.route("/contact")
def contact():
  title = "CONTACT — Siri"
  return render_template('contact.html', title=title)
    
if __name__ == "__main__":
  app.run(debug=True)