def get_model(title):
    import db
    match title:
        case 'Subscriber':
            return db.Subscriber
        case 'Book':
            return db.Book
        case 'Genre':
            return db.Genre
        case 'BookGenre':
            return db.BookGenre
        case 'BorrowRecord':
            return db.BorrowRecord
        case _:
            raise LookupError('Такой модели не существует')
