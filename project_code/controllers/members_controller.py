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
    return render_template("members/single_member.jinja", member = member)