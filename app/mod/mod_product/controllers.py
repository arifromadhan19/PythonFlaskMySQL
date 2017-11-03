from flask import Blueprint
from flask.templating import render_template

from app.model.product import Product

# mod_product = Blueprint('product',__name__, url_prefix="/product")
mod_product = Blueprint('product',__name__)

@mod_product.route("/",methods=["GET"])
def index_product():
    list_product = Product.query.all()
    for p in list_product:
        print(p.id_product)
        print(p.name_product)
    return render_template("product/index.html", message="Select one table",list_product=list_product)