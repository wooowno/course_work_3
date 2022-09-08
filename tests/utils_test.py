import pytest

from utils import *

# Какие ключи ожидаем получать у поста
post_keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

# Какие ключи ожидаем получать у комментария
comment_keys_should_be = {'post_id', 'commenter_name', 'comment', 'pk'}


def test_get_posts_all():
    """ Проверяем, верный ли список постов возвращается """
    posts = get_posts_all()
    assert type(posts) == list, "возвращается не список"
    assert len(posts) > 0, "возвращается пустой список"
    assert set(posts[0].keys()) == post_keys_should_be, "неверный список ключей"


def test_get_post_by_pk():
    """ Проверяем, верный ли пост возвращается """
    post_by_pk = get_post_by_pk(1)
    assert post_by_pk['pk'] == 1, "возвращается неправильный пост"
    assert set(post_by_pk.keys()) == post_keys_should_be, "неверный список ключей"


def test_get_posts_by_user_johnny():
    """ Проверяем, верный ли список постов пользователя возвращается """
    posts_by_user = get_posts_by_user("johnny")
    assert posts_by_user[0]['poster_name'] == "johnny", "возвращаются неправильные посты"
    assert set(posts_by_user[0].keys()) == post_keys_should_be, "неверный список ключей"


def test_get_posts_by_user_none():
    """ Проверяем, возвращается ли пустой список, если постов у пользователя нет """
    posts_by_user = get_posts_by_user("")
    assert posts_by_user == [], "возвращается не пустой список"


def test_search_for_posts():
    """ Проверяем, содержат ли посты искомое """
    posts_by_query = search_for_posts("еда")
    assert "еда" in posts_by_query[0]['content'], "возвращаются неправильные посты"
    assert set(posts_by_query[0].keys()) == post_keys_should_be, "неверный список ключей"


def test_get_all_comments():
    """ Проверяем, верный ли список комментов возвращается """
    comments = get_all_comments()
    assert type(comments) == list, "возвращается не список"
    assert len(comments) > 0, "возвращается пустой список"
    assert set(comments[0].keys()) == comment_keys_should_be, "неверный список ключей"


def test_does_post_exist_true():
    """ Проверяем, правильно ли определяет функция, что пост существует """
    true = does_post_exist(1)
    assert true, "возвращается неверное значение"


def test_does_post_exist_false():
    """ Проверяем, правильно ли определяет функция, что пост не существует """
    false = does_post_exist(-1)
    assert not false, "возвращается неверное значение"


def test_get_comments_by_post_id():
    """ Проверяем, верные ли комменты к посту возвращаются """
    comments_by_post_id = get_comments_by_post_id(1)
    assert comments_by_post_id[0]['post_id'] == 1, "возвращаются неправильные комменты"
    assert set(comments_by_post_id[0].keys()) == comment_keys_should_be, "неверный список ключей"


def test_get_comments_by_post_id_error():
    """ Проверяем, что при несуществуемом id поста поднимается ошибка ValueError """
    with pytest.raises(ValueError):
        get_comments_by_post_id(-1)


def test_get_comments_by_post_id_none():
    """ Проверяем, возвращается ли пустой список, если комментов у поста нет """
    comments_by_post_id = get_comments_by_post_id(8)
    assert comments_by_post_id == [], "возвращается не пустой список"
