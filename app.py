from flask import Flask, render_template, request, redirect #импортируем сам фласк
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  #app = Flack() создаем приложене, (__name__) закладывам встроенный аргумент в функцию, название приложения соотвествует названию соданого файла  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mywebsite.db' #подключаем sql lite

db = SQLAlchemy(app) #наще приложение app оборачиваем в клас СКЛалхемик тем самым создаем переменную DB - сам ничего не понял вообщем

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) #создаем уникальный айди, для этого созлаем колонку в которой первый параметр тип данных, второй будет гененрировать уникальный айди
    title = db.Column(db.String(100), nullable=False) #здесь второй параметр, что без заголовка нельзя создать пост
    text = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all() 
@app.route("/")  #добавили декоратор
@app.route("/index")
def index():     #добавили новую функцию
    return render_template('index.html')


@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


@app.route("/create", methods=['POST','GET'])  #добавили декоратор
def create():     #добавили новую функцию
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)



        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print (e)


        return redirect('/')
    else:
        return render_template('create.html')

@app.route("/test")
def test():     #добавили новую функцию
    return render_template('test.html')


@app.route("/testcss")
def testcss():     #добавили новую функцию
    return render_template('testcss.html')

@app.route("/testjs")
def testjs():     #добавили новую функцию
    return render_template('testjs.html')

@app.route("/konfigen")
def konfigen():     #добавили новую функцию
    return render_template('konfigen.html')







if __name__ == '__main__': # зачем то делаем, чтоб если запускаем наш фаил, то выполнялся ццеликом код, а если запускаем подругому то только часть кода
    app.run(debug=True, host='0.0.0.0', port=8000)   #чтоб веб приложение при обновлении перезапускалось 