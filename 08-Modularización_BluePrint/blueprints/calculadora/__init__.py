from flask import Blueprint, render_template, redirect

calculadora_bp = Blueprint("calculadora",__name__,template_folder="templates")

@calculadora_bp.route("/")
def index():
    return render_template("index.html")

@calculadora_bp.route("/suma/<int:num1>/<int:num2>")
def suma(num1,num2):
    return f"El resultado de : {num1} + {num2} = {str(num1+num2)}"

@calculadora_bp.route("/resta/<int:num1>/<int:num2>")
def resta(num1,num2):
    return f"El resultado de : {num1} - {num2} = {str(num1-num2)}"