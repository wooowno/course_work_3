import json
from utils import get_post_by_pk


def load_bookmarks() -> list[dict]:
    """ Возвращает закладки """

    with open("data/bookmarks.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def update_bookmarks(bookmarks: list[dict]) -> None:
    """ Обновляет закладки """

    with open("data/bookmarks.json", 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file, ensure_ascii=False, indent=len(bookmarks))


def add_bookmark(post_pk: int) -> None:
    """ Добавляет пост в закладки """

    bookmarks = load_bookmarks()
    post = get_post_by_pk(post_pk)

    if post in bookmarks:
        return

    bookmarks.append(post)

    update_bookmarks(bookmarks)


def remove_bookmark(post_pk: int) -> None:
    """ Удаляет пост из закладок """

    bookmarks = load_bookmarks()
    post = get_post_by_pk(post_pk)

    bookmarks.remove(post)

    update_bookmarks(bookmarks)