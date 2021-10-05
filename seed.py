from app import app
from models import db, Product

db.drop_all()
db.create_all()

p1 = Product(name="brand face wash")
p2 = Product(name="brand toner")
p3 = Product(name="brand essence")
p4 = Product(name="brand eyecream")
p5 = Product(name="brand vitaminC")
p6 = Product(name="brand retinol")
p7 = Product(name="brand sunblock")
p8 = Product(name="brand moisturizer")

db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
db.session.commit()