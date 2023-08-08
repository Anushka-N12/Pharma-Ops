from flask import Blueprint, jsonify
from pharmacy_management.service import add_product,get_all_product,get_product_by_id,add_batch_to_product,get_batch_by_product,get_batch_by_batchid,get_all_batch,update_batch,delete_batch,update_product,delete_product,get_all_stock,get_stock_by_productid,allsales,process_order,get_salesitem_by_salesid
pharmacy_management_bp = Blueprint('pharmacy_management', __name__)



@pharmacy_management_bp.route('/product/add', methods=['POST'])
def add_product_process():
    product = add_product()
    return jsonify(product)

@pharmacy_management_bp.route('/product', methods=['GET'])
def get_all_product_def():
    product = get_all_product()
    return jsonify(product)


@pharmacy_management_bp.route('/product/:product_id', methods=['GET'])
def get_product_by_id_def(product_id):
    product = get_product_by_id(product_id)
    return jsonify(product)

@pharmacy_management_bp.route('/product/batch/add/:product_id', methods=['POST'])
def add_batch_product_def(product_id):
    product = add_batch_to_product(product_id)
    return jsonify(product)


@pharmacy_management_bp.route('/product/batch/:product_id', methods=['GET'])
def get_batch_by_product_def(product_id):
    product = get_batch_by_product(product_id)
    return jsonify(product)

@pharmacy_management_bp.route('/batch/:batch_id', methods=['GET'])
def get_batch_by_batchid_def(batch_id):
    product = get_batch_by_batchid(batch_id)
    return jsonify(product)

@pharmacy_management_bp.route('/product/batch', methods=['GET'])
def get_all_batch_def():
    product = get_all_batch()
    return jsonify(product)


@pharmacy_management_bp.route('/product/batch/update/:batch_id', methods=['POST'])
def update_batch_def(batch_id):
    product = update_batch(batch_id)
    return jsonify(product)

@pharmacy_management_bp.route('/product/batch/delete/:batch_id', methods=['POST'])
def delete_batch_def(batch_id):
    product = delete_batch(batch_id)
    return jsonify(product)

@pharmacy_management_bp.route('/product/update/:product_id', methods=['POST'])
def update_product_def(product_id):
    product = update_product(product_id)
    return jsonify(product)

@pharmacy_management_bp.route('/product/delete/:product_id', methods=['POST'])
def delete_product_def(product_id):
    product = delete_product(product_id)
    return jsonify(product)

@pharmacy_management_bp.route('/product/stock', methods=['GET'])
def get_all_stock_def():
    product = get_all_stock()
    return jsonify(product)

@pharmacy_management_bp.route('/product/stock/:product_id', methods=['GET'])
def get_stock_by_productid_def(product_id):
    product = get_stock_by_productid(product_id)
    return jsonify(product)

@pharmacy_management_bp.route('/processOrder', methods=['POST'])
def process_order_def():
    product = process_order()
    return jsonify(product)

@pharmacy_management_bp.route('/Sales', methods=['GET'])
def get_all_sales_def():
    product = allsales()
    return jsonify(product)

@pharmacy_management_bp.route('/Sales/:saleid/items', methods=['GET'])
def get_salesitem_by_salesid_def(saleid):
    product = get_salesitem_by_salesid(saleid)
    return jsonify(product)


