from database import Database
from main_window import Window

window = Window()

db = Database()
db.get_all_users()
db.get_all_orders()
print(db.get_all_orders_with_names())

window.mainloop()

