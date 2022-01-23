from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify, flash

main_view = Blueprint("main_view", __name__)

@main_view.route('/')
def root():
	return jsonify("home"), 200