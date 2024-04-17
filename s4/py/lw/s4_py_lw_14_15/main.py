from fldb.initializer import *
from fldb.connection import *
from fldb.generator import *

init = FLDBInitializer()
con = FLDBConnection()

init.reset_to_default()

for i in range(1, 401):
    con.insert_rows("Users", random_user(i))
    if randint(1, 100) > 97:
        con.insert_rows("Librarians", random_librarian(i))
    else:
        con.insert_rows("Clients", random_client(i))

for i in range(1, 61):
    con.insert_rows("Movies", random_movie(i))
