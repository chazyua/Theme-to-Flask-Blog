from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(70))
    email = db.Column(db.String(700))
    comment = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Post: {self.name} | {self.email} | {self.comment}>'

