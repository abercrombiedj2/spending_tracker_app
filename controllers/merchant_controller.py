import re
from flask import Flask, Blueprint, render_template, request, redirect
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def view_merchants():
    merchants = merchant_repository.select_all()
    return render_template("/merchants/view_merchants.html", all_merchants=merchants)

@merchants_blueprint.route("/merchants/new_merchant", methods=['GET'])
def new_merchant():
    return render_template("/merchants/new_merchant.html")

@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    merchant_name = request.form['merchant_name']
    merchant = Merchant(merchant_name)
    merchant_repository.save(merchant)
    return redirect("/merchants")