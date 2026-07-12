from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = {
    1: {"username": "rahma", "role": "User"},
    2: {"username": "admin", "role": "Administrator"}
}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        if username == "rahma":
            return redirect("/profile/1")

        elif username == "admin":
            return redirect("/profile/2")

        else:
            return "User not found"

    return render_template("login.html")


@app.route("/profile/<int:user_id>")
def profile(user_id):

    user = users.get(user_id)

    if user:
        return render_template("profile.html", user=user)

    return "User not found"


if __name__ == "__main__":
    app.run(debug=True)