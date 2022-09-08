from app import app


# Какие ключи ожидаем получать у поста
keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


def test_api_posts():
    """ Проверяем, верный ли список постов возвращается """

    request = app.test_client().get("/api/posts", follow_redirects=True)
    assert type(request.json) == list, "возвращается не список"
    assert set(request.json[0].keys()) == keys_should_be, "неверный список ключей"


def test_api_post():
    """ Проверяем, верный ли пост возвращается """

    request = app.test_client().get("/api/posts/1", follow_redirects=True)
    assert type(request.json) == dict, "возвращается не словарь"
    assert set(request.json.keys()) == keys_should_be, "неверный список ключей"
