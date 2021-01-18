from flask import Flask, render_template, url_for, request, redirect
import cleaner as cl

app = Flask(__name__)
url = ""

@app.route("/", methods=["POST", "GET"])
def home():
    global url
    if request.method == "POST":
        url = request.form["text_url"]
        return redirect(url_for("cleaner"))
    else:
        return render_template("home.html")


@app.route("/cleaned/")
def cleaner():
    toprint = cl.clean(url)
    return render_template("cleaned.html",out = toprint)

if __name__ == "__main__":
    app.run(debug=True)
    
