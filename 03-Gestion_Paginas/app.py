from flask import Flask,jsonify,request,render_template,url_for,redirect


app = Flask(__name__)

@app.route("/inicio/<email>")
def inicio(email):
    return render_template("base.html",usuario=email)

#Login 
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == "admin@gmail.com" and password == "admin123":
            return redirect(url_for("inicio",email=email))
        else: 
            return render_template("404.html")
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)