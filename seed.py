from app import app
from models import db, Product

db.drop_all()
db.create_all()

p1 = Product(name="brand face wash", price=30.55)
p2 = Product(name="brand toner", price=44.55)
p3 = Product(name="brand essence", price=50.55)
p4 = Product(name="brand eyecream", price=45.55)
p5 = Product(name="brand vitaminC", price=53.55)
p6 = Product(name="brand retinol", price=60.55)
p7 = Product(name="brand sunblock", price=30.55)
p8 = Product(name="brand lip mask", price=25.55)
p9 = Product(name="brand sheet mask", price=5.55)

db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9])
db.session.commit()