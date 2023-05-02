from flask import render_template, redirect, request

from flask import Blueprint
from models.member import *

import repositories.member_repo as member_repo
import repositories.booking_repo as booking_repo 
import repositories.session_repo as session_repo 

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def show_all_members():
    members = member_repo.select_all()
    return render_template('/members/members.jinja', title = "All members page", members = members)


@members_blueprint.route("/members/<id>")
def show_member_index(id):
    member = member_repo.select(id)
    return render_template("/members/single_member.jinja", member = member)

@members_blueprint.route('/members/new')
def add_member():

    return render_template('members/new.jinja')

@members_blueprint.route('/members/new', methods = ["POST"])
def submit_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    postcode = request.form['postcode']
    premium_member = True if 'premium_member' in request.form else False # will cause errors if not ticked hence else False is needed.
    
    new_member = Member(first_name, last_name, postcode, premium_member)
    member_repo.save(new_member)
    return redirect("/members")

# EDIT
# GET '/members/<id>/edit'
@members_blueprint.route('/members/<id>/edit')
def edit_member(id):
    edit_member = member_repo.select(id)
    return render_template('members/edit.jinja', member = edit_member)

# UPDATE
# PUT '/members/<id>/edit'
@members_blueprint.route("/members/<id>/edit", methods=['POST'])
def update_member(id):
    member_repo.select(id)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    postcode = request.form['postcode']
    premium_member = request.form["premium_member"]
    edit_member = Member(first_name, last_name, postcode, premium_member, id)
    member_repo.update(edit_member)
    return redirect('/members')

