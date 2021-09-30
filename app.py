from models import Article
from flask.json import jsonify
from flask import Flask, session, redirect, render_template
from blueprints.auth import bp as AuthBlueprint
from blueprints.add import bp as AddBlueprint
from models import Article

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfasdjhghfdhfa'
app.register_blueprint(AuthBlueprint)
app.register_blueprint(AddBlueprint)

@app.route('/')
def Main():
    if not 'username' in session:
        return redirect('/login')

    _articles = Article.select()
    
    return jsonify(msg="Done", articles = _articles)

if __name__=='__main__':
    app.run()