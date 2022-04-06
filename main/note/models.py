from main import db

class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    detail = db.Column(db.String(200))
    author = db.Column(db.String(20))

    def __init__(self, title, detail, author):
        self.title = title
        self.detail = detail
        self.author = author
