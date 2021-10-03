from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm

from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Length,Email

app=Flask(__name__)
app.secret_key='yes'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:love520wenyu@localhost:3306/db"

db=SQLAlchemy(app)


class Member(db.Model):
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)

    name = db.Column(db.String(30), unique=True, nullable=False)
    
    password = db.Column(db.String(30), unique=True, nullable=False)

    email=db.Column(db.String(30))
    

    def __init__(self,email,name,password):
        self.email =email
        self.name = name
        self.password=password

db.create_all()

class Form(FlaskForm):
    username=StringField(label='用戶名',validators=[DataRequired()])
    email=StringField(label='電子信箱',validators=[DataRequired(),Email(message='電子信箱格式錯誤')])
    password=StringField(label='密碼',validators=[DataRequired,Length(6,16,message='密碼格式錯誤')])
    password=StringField(label='確認密碼',validators=[DataRequired,Length(6,16,message='密碼格式錯誤'),EqualTo('password',message='密碼不一致')])

    submit=SubmitField(label='註冊')

@app.route('/',method=['GET','POST'])
def register():
    register_form=Form()

    if request.method=='POST':
        if register_form.validate_on_submit():
            username=request.form.get('username')
            email=request.form.get('email')
            password=request.form.get('password')

            if Member.query.filter_by(username=username).all():
                return 'already have account'
            
            member=Member(username=username,email=email,password=password)
            db.session.add(member)
            db.session.commit()

            return 'success'

        else:
            return 'Invalid'

    return render_template('register.html',form=register_form)


if __name__ == "__main__":
    app.run(debug=True)