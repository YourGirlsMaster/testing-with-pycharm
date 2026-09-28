from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/greet", methods = ["GET", "POST"])
def greet():
    message = ""

    if request.method == "POST":
        name = request.form.get("name")
        message =f"hello, {name} !"

    return render_template("greet.html", messages =message)


if __name__ =="__main__":
    app.run(debug=True)