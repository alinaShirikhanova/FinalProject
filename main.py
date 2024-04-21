from database import Database
from main_window import Window

window = Window()

db = Database()
db.get_all_users()


window.mainloop()

