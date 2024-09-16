from typing import List

import peewee as pw

from db.base import BaseModel


class Book(BaseModel):
    name = pw.CharField(verbose_name='Название', max_length=128)
    author = pw.CharField(verbose_name='Автор', max_length=256)
    edition = pw.CharField(verbose_name='Издание', max_length=64, null=True)
    position = pw.CharField(verbose_name='Позиция', max_length=64, null=True, unique=True)
    is_lost = pw.BooleanField(verbose_name='Потеряно', default=False)

    @classmethod
    def create(cls, name: str, author: str, edition: str, genres: List['Genre'], position: str = None, **query):
        inst = super().create(
            name=name,
            author=author,
            edition=edition,
            position=position,
            **query
        )
        for genre in genres:
            BookGenre.create(inst, genre)
        return inst

    @property
    def genres(self) -> List['Genre']:
        return [bg.genre for bg in BookGenre.select().where(BookGenre.book == self)]


class Genre(BaseModel):
    name = pw.CharField(verbose_name='Название', max_length=64, unique=True)

    @classmethod
    def create(cls, name: str, **query):
        return super().create(
            name=name,
            **query
        )

    @property
    def books(self) -> List[Book]:
        return [bg.book for bg in BookGenre.select().where(BookGenre.genre == self)]


class BookGenre(BaseModel):
    class Meta:
        constraints = [pw.SQL('UNIQUE ("book_id", "genre_id")')]

    book = pw.ForeignKeyField(Book, verbose_name='Книга')
    genre = pw.ForeignKeyField(Genre, verbose_name='Жанр')

    @classmethod
    def create(cls, book: Book, genre: Genre, **query):
        return super().create(
            book=book,
            genre=genre,
            **query
        )
