from flask import Blueprint, jsonify, request, render_template
from app.models.transaction import Transaction
from app import db

bp = Blueprint('transactions', __name__, url_prefix='/transactions')

@bp.route('/', methods=['GET'])
def get_transactions():
    if request.headers.get('Accept') == 'application/json':
        transactions = Transaction.query.all()
        return jsonify([transaction.to_dict() for transaction in transactions])
    return render_template('transactions.html')

@bp.route('/', methods=['POST'])
def create_transaction():
    data = request.get_json()
    transaction = Transaction(
        type=data['type'],
        amount=data['amount'],
        description=data['description'],
        product_id=data.get('product_id'),
        quantity=data.get('quantity')
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify(transaction.to_dict()), 201
