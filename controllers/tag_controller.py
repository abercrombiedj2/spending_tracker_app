from flask import Flask, Blueprint, render_template, request, redirect
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags/view_tags")
def view_tags():
    tags = tag_repository.select_all()
    return render_template("tags/view_tags.html", all_tags=tags)

@tags_blueprint.route("/tags/new_tag", methods=['GET'])
def new_tag():
    return render_template("tags/new_tag.html")

@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    tag_name = request.form['tag_name']
    tag = Tag(tag_name)
    tag_repository.save(tag)
    return redirect("/")

@tags_blueprint.route("/tags/<id>/edit_tag")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template("tags/edit_tag.html", tag=tag)

@tags_blueprint.route("/tags/<id>", methods=['POST'])
def update_tag(id):
    tag_name = request.form['tag_name']
    tag = Tag(tag_name, id)
    tag_repository.update(tag)
    return redirect("/")