import json


def get_posts_all() -> list[dict]:
    """ Возвращает посты """

    with open("data/posts.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def get_post_by_pk(pk: int) -> dict:
    """ Возвращает один пост по его идентификатору """

    for post in get_posts_all():
        if pk == post['pk']:
            return post


def get_posts_by_user(user_name: str) -> list[dict]:
    """
    Возвращает посты определенного пользователя или
    пустой список, если у пользователя нет постов.
    """

    user_posts: list[dict] = []

    for post in get_posts_all():
        if post['poster_name'] == user_name:
            user_posts.append(post)

    return user_posts


def search_for_posts(query: str) -> list[dict]:
    """ Возвращает список постов по ключевому слову """
    posts_by_query: list[dict] = []

    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            posts_by_query.append(post)

    return posts_by_query


def get_all_comments() -> list[dict]:
    """ Возвращает комментарии """

    with open("data/comments.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def does_post_exist(post_pk: int) -> bool:
    """ Возвращает True, если пост с переданным pk существует, False - если нет """

    for post in get_posts_all():
        if post['pk'] == post_pk:
            return True

    return False


def get_comments_by_post_id(post_id: int) -> list[dict]:
    """
    Возвращает комментарии определенного поста.
    Функция вызывает ошибку ValueError если такого поста нет и пустой список,
    если у поста нет комментов.
    """

    comments_by_post_id: list[dict] = []

    if not does_post_exist(post_id):
        raise ValueError

    for comment in get_all_comments():
        if comment['post_id'] == post_id:
            comments_by_post_id.append(comment)

    return comments_by_post_id
