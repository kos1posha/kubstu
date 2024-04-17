from fldb.connection import FLDBConnection
from logs import loger


# init class for filmlibrary database
class FLDBInitializer:
    __debug = False
    __connection: FLDBConnection
    __tables = [
        {
            'name': '"Genres"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Боевик", "Жанр кинематографа, в котором основное внимание уделяется перестрелкам, дракам, погоням и т.д.")',
                '(2, "Комедия", "Жанр кинематографа, в основе которых эстетические категории сатиры, юмора и буффонады.")',
                '(3, "Хоррор", "Жанр кинематографа, призванный вызвать у зрителей чувство страха, тревоги и неопределённости, создать напряжённую атмосферу ужаса или мучительного ожидания чего-либо ужасного.")',
                '(4, "Драма", NULL)',
                '(5, "Комедийная драма", NULL)',
                '(6, "Триллер", NULL)',
                '(7, "Зомби-боевик", NULL)',
                '(8, "Военный", NULL)',
                '(9, "Постапокалиписис", NULL)',
            ],
        },  # Genres
        {
            'name': '"AgeRatings"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "G", "Кино без всяких возрастных ограничений.")',
                '(2, "PG", "Кино разрешённое для просмотра всем, но маленьким детям рекомендуется просмотр с родителями.")',
                '(3, "PG-13", "Детям до 13 просмотр не желателен.")',
                '(4, "R", "Зрители до 17 лет должны присутствовать в зале с сопровождением родителей.")',
                '(5, "NC-17", "Зрители до 18 не допускаются.")'
            ],
        },  # AgeRatings
        {
            'name': '"Countries"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "США", NULL)',
                '(2, "Республика Корея", NULL)',
                '(3, "Германия", NULL)',
                '(4, "Россия", NULL)',
                '(5, "Белоруссия", NULL)',
                '(6, "Великобритания", NULL)',
                '(7, "Франция", NULL)'
            ]
        },  # Countries
        {
            'name': '"FilmCompanies"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Gordon company", NULL)',
                '(2, "Silver Pictures", NULL)',
                '(3, "Cinergi Pictures", NULL)',
                '(4, "Cheyenne Enterprises", NULL)',
                '(5, "Dune Entertainment", NULL)',
                '(6, "Ingenious Film Partners", NULL)',
                '(7, "Giant Pictures", NULL)',
                '(8, "New Line Cinema", NULL)',
                '(9, "Castle Rock Entertainment", NULL)',
                '(10, "DreamWorks Pictures", NULL)',
                '(11, "Metro-Goldwyn-Mayer", NULL)',
                '(12, "Next Entertainment World", NULL)',
                '(13, "RedPeter Films", NULL)',
                '(14, "MacDonald/Parkes Productions", NULL)',
                '(15, "Беларусьфильм", NULL)',
                '(16, "Yellow, Black and White", NULL)',
                '(17, "Fox 2000 Pictures", NULL)',
                '(18, "M6 Films", NULL)',
                '(19, "Panteleon Films", NULL)'
            ]
        },  # FilmCompanies
        {
            'name': '"Distributors"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "20th Century Fox", NULL)',
                '(2, "Cinergi Pictures", NULL)',
                '(3, "Warner Bros", NULL)',
                '(4, "United International Pictures", NULL)',
                '(5, "Universal Pictures", NULL)',
                '(6, "Metro-Goldwyn-Mayer", NULL)',
                '(7, "Next Entertainment World", NULL)',
                '(8, "ADS Service", NULL)',
                '(9, "DreamWorksPictures", NULL)',
                '(10, "Cirko Film", NULL)',
                '(11, "Централ Партнершип", NULL)',
                '(12, "InterCom", NULL)',
                '(13, "UIP Duna", NULL)',
                '(14, "IFC Film", NULL)',
                '(15, "Wild Bunch", NULL)'
            ]
        },  # Distributors
        {
            'name': '"Cinematographers"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"FirstName" TEXT NOT NULL',
                '"LastName" TEXT',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Ян де", "Бонт", NULL)',
                '(2, "Оливер", "Вуд", NULL)',
                '(3, "Питер", "Мензес-младший", NULL)',
                '(4, "Саймон", "Дагган", NULL)',
                '(5, "Джонатан", "Села", NULL)',
                '(6, "Чон", "Джон-Хун", NULL)',
                '(7, "Дэвид", "Таттерсолл", NULL)',
                '(8, "Шон", "Портер", NULL)',
                '(9, "Джозеф", "Руттенберг", NULL)',
                '(10, "Ли", "Хён Док", NULL)',
                '(11, "Гэбриэл", "Бериштейн", NULL)',
                '(12, "Боян", "Бацелли", NULL)',
                '(13, "Владислав", "Опельянц", NULL)',
                '(14, "Юрий", "Никогосов", NULL)',
                '(15, "Дон", "Бёрджесс", NULL)',
                '(16, "Дмитрий", "Цхай", NULL)',
                '(17, "Флориан", "Баллхаус", NULL)',
                '(18, "Мигель", "Менс", NULL)',
                '(19, "Дени", "Рубен", NULL)'
            ]
        },  # Cinematographers
        {
            'name': '"Directors"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"FirstName" TEXT NOT NULL',
                '"LastName" TEXT',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Джон", "Мактирнан", NULL)',
                '(2, "Ренни", "Харлин", NULL)',
                '(3, "Лен", "Уйазман", NULL)',
                '(4, "Джон", "Мур", NULL)',
                '(5, "Энди", "Мускетти", NULL)',
                '(6, "Фрэнк", "Дарабонт", NULL)',
                '(7, "Питер", "Фаррелли", NULL)',
                '(8, "Джордж", "Кьюкор", NULL)',
                '(9, "Ён", "Сан Хо", NULL)',
                '(10, "Гор", "Вербински", NULL)',
                '(11, "Вадим", "Перельман", NULL)',
                '(12, "Клим", "Шипенко", NULL)',
                '(13, "Братья", "Хьюз", NULL)',
                '(14, "Хидэо", "Наката", NULL)',
                '(15, "Максим", "Кулагин", NULL)',
                '(16, "Дэвид", "Френкель", NULL)',
                '(17, "Джонатан", "Якубович", NULL)',
                '(18, "Лоран", "Тирар", NULL)'
            ]
        },  # Directors
        {
            'name': '"Producers"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"FirstName" TEXT NOT NULL',
                '"LastName" TEXT',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Лоуренс", "Гордон", NULL)',
                '(2, "Майкл", "Тадросс", NULL)',
                '(3, "Майкл", "Фоттрелл", NULL)',
                '(4, "Алекс", "Юнг", NULL)',
                '(5, "Рой", "Ли", NULL)',
                '(6, "Фрэнк", "Дарабонт", NULL)',
                '(7, "Джим", "Берк", NULL)',
                '(8, "Артур", "Хорнблоу", NULL)',
                '(9, "Ли", "Дон Ха", NULL)',
                '(10, "Уолтер", "Паркс", NULL)',
                '(11, "Илья", "Стюарт", NULL)',
                '(12, "Эдуард", "Илоян", NULL)',
                '(13, "Гари", "Олдман", NULL)',
                '(14, "Антон", "Лапенко", NULL)',
                '(15, "Венди", "Финерман", NULL)',
                '(16, "Дан", "Мааг", NULL)',
                '(17, "Эрик", "Йехельманн", NULL)'
            ]
        },  # Producers
        {
            'name': '"Musicians"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"FirstName" TEXT NOT NULL',
                '"LastName" TEXT',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Майкл", "Камен", NULL)',
                '(2, "Марко", "Бельтрами", NULL)',
                '(3, "Бенджамин", "Уоллфиш", NULL)',
                '(4, "Томас", "Ньюман", NULL)',
                '(5, "Крис", "Бауэрс", NULL)',
                '(6, "Бронислав", "Капер", NULL)',
                '(7, "Чан", "Ён Гю", NULL)',
                '(8, "Моуг", NULL, NULL)',
                '(9, "Ганс", "Циммер", NULL)',
                '(10, "Иван", "Бурляев", NULL)',
                '(11, "Аттикус", "Росс", NULL)',
                '(12, "Хеннинг", "Лонер", NULL)',
                '(13, "Теодор", "Шапиро", NULL)',
                '(14, "Анхело", "Мильи", NULL)',
                '(15, "Клаус", "Бадельт", NULL)',
                '(16, "Эрик", "Невё", NULL)'
            ]
        },  # Musicians
        {
            'name': '"Editors"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"FirstName" TEXT NOT NULL',
                '"LastName" TEXT',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Франк", "Уриосте", NULL)',
                '(2, "Стюарт", "Бэрд", NULL)',
                '(3, "Джон", "Райт", NULL)',
                '(4, "Николя", "Де Тот", NULL)',
                '(5, "Дэн", "Циммерман", NULL)',
                '(6, "Джейсон", "Баллантайн", NULL)',
                '(7, "Ричард", "Френсис-Брюс", NULL)',
                '(8, "Патрик", "Дон Вито", NULL)',
                '(9, "Ральф", "Винтерс", NULL)',
                '(11, "Ян", "Джин Мо", NULL)',
                '(12, "Крейг", "Вуд", NULL)',
                '(13, "Весела", "Марчевский", NULL)',
                '(14, "Тим", "Павелко", NULL)',
                '(15, "Синди", "Молло", NULL)',
                '(16, "Майкл", "Кню", NULL)',
                '(17, "Марк", "Ливолси", NULL)',
                '(18, "Александр", "Бернер", NULL)',
                '(19, "Валери", "Дезен", NULL)'
            ]
        },  # Editors
        {
            'name': '"Movies"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT',
                '"RunningTime" TEXT',
                '"ReleaseDate" TEXT',
                '"GenreID" INTEGER REFERENCES "Genres"',
                '"AgeRatingID" INTEGER REFERENCES "AgeRatings"',
                '"CountryID" INTEGER REFERENCES "Countries"',
                '"FilmCompanyID" INTEGER REFERENCES "FilmCompanies"',
                '"DistributorID" INTEGER REFERENCES "Distributors"',
                '"CinematographerID" INTEGER REFERENCES "Cinematographers"',
                '"DirectorID" INTEGER REFERENCES "Directors"',
                '"ProducerID" INTEGER REFERENCES "Producers"',
                '"MusicianID" INTEGER REFERENCES "Musicians"',
                '"EditorID" INTEGER REFERENCES "Editors"',
            ],
            'default': []
        },  # Movies
        {
            'name': '"Adapters"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"RTitle" TEXT UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "CD-ROM", "Сиди-диск", "Compact Disc Read-Only Memory — компакт диск.")',
                '(2, "DVD-ROM", "Дивиди-диск", "Digital Versatile Disc Read-Only Memory — цифровой многоцелевой диск.")',
                '(3, "Blu-Ray", "Блю-рей", "Формат оптического носителя, используемый для записи с повышенной плотностью хранения цифровых данных.")',
                '(21, "FlashUSB", "Флешка", "Флеш-носитель с USB переходником.")',
                '(41, "Diskette", "Дискета", "Гибкий магнитный диск. Для чтения нужен специальный дисковод.")',
                '(61, "SD", "Сиди-карта", NULL)',
                '(62, "miniSD", "Мини-сиди", NULL)',
                '(63, "microSD", "Микро-сиди", NULL)'
            ],
        },  # Adapters
        {
            'name': '"Languages"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Short" TEXT UNIQUE'
            ],
            'default': [
                '(1, "Русский", "ru")',
                '(2, "Английский", "en")',
                '(3, "Французский", "fr")'
            ]
        },  # Languages
        {
            'name': '"DubbingStudios"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Кубик в кубе", NULL)'
            ]
        },  # DubbingStudios
        {
            'name': '"MovieInstances"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"MovieID" INTEGER NOT NULL REFERENCES "Movies"',
                '"AdapterID" INTEGER NOT NULL REFERENCES "Adapters"',
                '"LanguageID" INTEGER REFERENCES "Languages"',
                '"DubbingStudioID" INTEGER REFERENCES "DubbingStudios"'
            ],
            'default': []
        },  # MovieInstances
        {
            'name': '"TrustStatuses"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Высокий", NULL)',
                '(2, "Средний", NULL)',
                '(3, "Низкий", NULL)',
                '(4, "Черный список", NULL)'
            ]
        },  # TrustStatuses
        {
            'name': '"Specialities"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Title" TEXT NOT NULL UNIQUE',
                '"Description" TEXT'
            ],
            'default': [
                '(1, "Старший-библиотекарь", NULL)',
                '(2, "Библиотекарь", NULL)',
                '(3, "Стажер", NULL)',
                '(4, "Архивариус", NULL)'
            ]
        },  # Specialities
        {
            'name': '"WorkSchedules"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Monday" INTEGER NOT NULL',
                '"Tuesday" INTEGER NOT NULL',
                '"Wednesday" INTEGER NOT NULL',
                '"Thursday" INTEGER NOT NULL',
                '"Friday" INTEGER NOT NULL',
                '"Saturday" INTEGER NOT NULL',
                '"Sunday" INTEGER NOT NULL'
            ],
            'default': [
                '(1, "True", "True", "True", "True", "True", "False", "False")',
                '(2, "True", "False", "True", "False", "True", "False", "False")',
                '(3, "False", "True", "True", "True", "True", "False", "False")',
                '(4, "False", "False", "False", "False", "True", "True", "True")',
                '(5, "True", "True", "False", "True", "False", "True", "True")',
                '(6, "False", "True", "False", "True", "False", "True", "False")',
                '(7, "False", "False", "True", "True", "True", "False", "True")',
                '(8, "False", "True", "True", "False", "False", "True", "True")'
            ]
        },  # WorkSchedules
        {
            'name': '"Users"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"FirstName" TEXT NOT NULL',
                '"LastName" TEXT NOT NULL',
                '"Sex" TEXT',
                '"PhoneNumber" TEXT UNIQUE',
                '"Email" TEXT UNIQUE',
                '"BirthDay" TEXT'
            ],
            'default': []
        },  # Users
        {
            'name': '"Clients"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"RegistrationDate" TEXT NOT NULL',
                '"UserID" INTEGER NOT NULL UNIQUE REFERENCES "Users"',
                '"TrustStatusID" INTEGER REFERENCES "TrustStatuses"'
            ],
            'default': []
        },  # Clients
        {
            'name': '"Librarians"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"UserID" INTEGER NOT NULL UNIQUE REFERENCES "Users"',
                '"SpecialityID" INTEGER REFERENCES "Specialities"',
                '"WorkScheduleID" INTEGER REFERENCES "WorkSchedules"',
            ],
            'default': []
        },  # Librarians
        {
            'name': '"Issuances"',
            'columns': [
                '"ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                '"Active" INTEGER NOT NULL',
                '"DateTime" TEXT NOT NULL',
                '"Duration" TEXT NOT NULL',
                '"MovieInstanceID" INTEGER NOT NULL REFERENCES "MovieInstances"',
                '"ClientID" INTEGER NOT NULL REFERENCES "Clients"',
                '"LibrarianID" INTEGER NOT NULL REFERENCES "Librarians"'
            ],
            'default': []
        }  # Issuances
    ]

    def __init__(self):
        self.__connection = FLDBConnection()

    def reset_to_default(self):
        self.drop_tables()
        self.create_tables()
        self.insert_defaults()
        loger.write(200, 'Reset to default success')

    def create_tables(self):
        sep = ',\n\t'
        for table in filter(lambda t: t.get("columns"), self.__tables):
            query = (f'CREATE TABLE {table.get("name")} '
                     f'(\n\t{sep.join(table.get("columns"))}\n)')
            self.__connection.rich_execute(query, self.__debug)

    def drop_tables(self):
        for table in self.__tables:
            query = f'DROP TABLE {table.get("name")}'
            self.__connection.rich_execute(query, self.__debug)

    def insert_defaults(self):
        sep = ',\n\t'
        for table in filter(lambda t: t.get('default'), self.__tables):
            query = (f'INSERT INTO {table.get("name")} '
                     f'VALUES \n\t{sep.join(table.get("default"))}')
            self.__connection.rich_execute(query, self.__debug)

    def clear_tables(self):
        for table in self.__tables:
            query = f'DELETE FROM {table.get("name")}'
            self.__connection.rich_execute(query, self.__debug)


rt_names = {
    'Adapters': 'Носители',
    'AgeRatings': 'Возрастные рейтинги',
    'Cinematographers': 'Операторы',
    'Countries': 'Страны',
    'Directors': 'Режиссеры',
    'Distributors': 'Дистрибьюторы',
    'DubbingStudios': 'Студии дубляжа',
    'Editors': 'Редакторы',
    'FilmCompanies': 'Кинокомпании',
    'Genres': 'Жанры',
    'Languages': 'Языки',
    'Musicians': 'Композиторы',
    'Producers': 'Продюсеры',
    'Specialities': 'Специальности',
    'TrustStatuses': 'Статус доверия',
    'WorkSchedules': 'Расписание',
    'Users': 'Пользователи',
    'Clients': 'Клиенты',
    'Librarians': 'Библиотекари',
    'Movies': 'Фильмы',
    'MovieInstances': 'Имеющиеся диски',
    'Issuances': 'Журнал выдач'
}
rt_fields = {
    'ID': '#',
    'Title': 'Название',
    'RTitle': 'На русском',
    'Description': 'Описание',
    'FirstName': 'Имя',
    'LastName': 'Фамилия',
    'Short': 'Кратко',
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье',
    'Sex': 'Пол',
    'PhoneNumber': 'Телефонный номер',
    'Email': 'Почта',
    'BirthDay': 'День рождения',
    'RegistrationDate': 'Дата регистрации',
    'UserID': '# Пользователя',
    'TrustStatusID': '# Статуса доверия',
    'SpecialityID': '# Специальности',
    'WorkScheduleID': '# Расписания',
    'RunningTime': 'Длина',
    'ReleaseDate': 'Дата релиза',
    'GenreID': '# Ж-ра',
    'AgeRatingID': '# Воз. р-га',
    'CountryID': '# Страны',
    'FilmCompanyID': '# Кинок.',
    'DistributorID': '# Дист.',
    'CinematographerID': '# Опер.',
    'DirectorID': '# Реж.',
    'ProducerID': '# Прод.',
    'MusicianID': '# Композ.',
    'EditorID': '# Ред.',
    'LanguageID': '# Языка',
    'DubbingStudioID': '# Студии дубляжа',
    'MovieID': '# Фильма',
    'Active': 'Активен',
    'DateTime': 'Дата выдачи',
    'Duration': 'Срок возврата',
    'MovieInstanceID': '# Диска',
    'ClientID': '# Клиента',
    'LibrarianID': '# Библиотекаря',
    'AdapterID' : '# Носителя'
}


def translate_table(table):
    return rt_names.get(table)


def translate_field(field):
    return rt_fields.get(field)
