from flask import Blueprint, jsonify, request, render_template
from app.models.product import Product
from app import db

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
    if request.headers.get('Accept') == 'application/json':
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products])
    return render_template('products.html')

@bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())
