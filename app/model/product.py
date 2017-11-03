from app import db

class Product(db.Model):
    __tablename__ = 'product'
    id_product = db.Column(db.String(255), primary_key=True)
    name_product = db.Column(db.String(255), nullable=False)

# class ProductQty(db.Model):
#     __tablename__ = 'product_qty'
#     id_product = db.Column(db.String(255), primary_key=True)
#     qty_product = db.Column(db.String(255), nullable=False)
#
# class AllProduct(db.Model):
#     __tablename__ = 'all_product'
#     id_product = db.Column(db.String(255), primary_key=True)
#     qty_product = db.Column(db.String(255), nullable=False)
