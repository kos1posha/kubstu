from datetime import date

import peewee as pw

from db.base import BaseModel
from db.subscriber import Subscriber
from db.book import Book


class BorrowRecord(BaseModel):
    subscriber = pw.ForeignKeyField(Subscriber, verbose_name='Подписчик')
    book = pw.ForeignKeyField(Book, verbose_name='Книга')
    borrowing_date = pw.DateField(verbose_name='Дата получения', default=date.today)
    borrowing_days = pw.IntegerField(verbose_name='Количество дней')
    returning_date = pw.DateField(verbose_name='Дата возврата', null=True)

    @classmethod
    def create(cls, subscriber: Subscriber, book: Book, borrowing_days: int, **query):
        return super().create(
            subscriber=subscriber,
            book=book,
            borrowing_days=borrowing_days,
            **query
        )

    def save(self, *args, **kwargs):
        if BorrowRecord.select().where(
                (BorrowRecord.book == self.book) &
                (BorrowRecord.returning_date.is_null())
        ).exists():
            raise ValueError(f'Книга "{self.book.name}" уже занята.')
        super().save(*args, **kwargs)

    def marked_returned(self, returning_date: date = None) -> None:
        if returning_date is None:
            returning_date = date.today()
        self.returning_date = returning_date
        self.save()
