import logging

from flask import Flask, render_template, request, jsonify

# Импортируем блюпринт
from bookmarks.views import bookmarks_blueprint

# Импортируем функции
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user
from bookmarks.functions import load_bookmarks

# Создаем экземпляр Flask
app = Flask(__name__)

# Регистрируем блюпринт
app.register_blueprint(bookmarks_blueprint)

# Разрешаем использовать кириллицу в приложении
app.json.ensure_ascii = False

# Создаём логгер
api_logger = logging.getLogger("api")

# Создаём обработчика для записи в файл
file_handler = logging.FileHandler("logs/api.log", encoding="utf-8")

# Устанавливаем формат логов
api_formate = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(api_formate)

# Назначаем уровень логгирования
api_logger.setLevel(level=logging.INFO)

# Добавляем обработчик к журналу
api_logger.addHandler(file_handler)


# Вьюшка главной страницы
@app.route("/")
def index_page():
    return render_template("index.html", posts=get_posts_all(), len_bookmarks=len(load_bookmarks()))


# Вьюшка одного поста
@app.route("/post/<int:post_id>")
def post_page(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments, len_comments=len(comments))


# Вьюшка результата поиска
@app.route("/search")
def search_page():
    query = request.args.get("s")
    posts = search_for_posts(query)
    return render_template("search.html", posts=posts, len_posts=len(posts))


# Вьюшка всех постов пользователя
@app.route("/users/<username>")
def user_feed_page(username):
    return render_template("user-feed.html", posts=get_posts_by_user(username))


# Вьюшка постов по тегу
@app.route("/tag/<tag_name>")
def tag_page(tag_name):
    return render_template("tag.html", tag=tag_name.upper(), posts=search_for_posts('#' + tag_name))


# Обработка ошибки 404
@app.errorhandler(404)
def not_found(e):
    return "статус-код 404"


# Обработка ошибки 500
@app.errorhandler(500)
def server_error(e):
    return "статус-код 500"


# API возвращает полный список постов в виде JSON-списка
@app.route("/api/posts")
def api_posts():
    api_logger.info("Запрос /api/posts")   # Логгирование обращения к API
    return jsonify(get_posts_all())


# API возвращает один пост в виде JSON-словаря
@app.route("/api/posts/<int:post_id>")
def api_post(post_id):
    api_logger.info(f"Запрос /api/posts/{post_id}")   # Логгирование обращения к API
    return jsonify(get_post_by_pk(post_id))


# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()
