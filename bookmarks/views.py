from flask import Blueprint, render_template, redirect

# Импортируем функции
from .functions import load_bookmarks, add_bookmark, remove_bookmark


# Создаём блюпринт
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


# Вьюшка для закладок
@bookmarks_blueprint.route("/bookmarks")
def bookmarks_page():
    return render_template("bookmarks.html", posts=load_bookmarks())


# Вьюшка для добавления закладки
@bookmarks_blueprint.route("/bookmarks/add/<int:post_id>")
def bookmarks_add_page(post_id):
    add_bookmark(post_id)
    return redirect("/", code=302)


# Вьюшка для удаления закладки
@bookmarks_blueprint.route("/bookmarks/remove/<int:post_id>")
def bookmarks_remove_page(post_id):
    remove_bookmark(post_id)
    return redirect("/bookmarks", code=302)
