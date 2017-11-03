from flask import Blueprint, jsonify, redirect
from flask.templating import render_template
from app.mod.mod_product.form import ProductForm
from app.model.product import Product
from app import db

# mod_product = Blueprint('product',__name__, url_prefix="/product")
mod_product = Blueprint('product',__name__)

@mod_product.route("/",methods=["GET"])
def index_product():
    list_product = Product.query.all()
    return render_template("product/index.html", message="Select one table",list_product=list_product)

@mod_product.route("/create",methods=["GET"])
def create_product():
    return render_template("product/create.html")

@mod_product.route("/create", methods=["POST"])
def save_product():
    form = ProductForm()
    if not form.validate():
        return jsonify({"error": form.errors})

    product = Product()
    product.id_product = form.id_product.data
    product.name_product = form.name_product.data

    db.session.add(product)
    db.session.commit()
    return redirect("/")

