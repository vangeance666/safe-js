from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify, flash

api_view = Blueprint("api_view", __name__)

@api_view.route('/')
def root():
	return jsonify("home"), 200

@api_view.route('/analyze/', methods=['GET', 'POST'])
def analyze():
	return jsonify("test_analyze"), 200
