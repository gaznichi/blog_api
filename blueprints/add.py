from flask import Blueprint, request
from flask.json import jsonify
from peewee import Delete
from models import Article

bp = Blueprint('add', __name__)

@bp.route('/add', methods=['POST'])
def Add():
    if not  request.is_json:
        return jsonify(msg="Missing JSON in headers")

    _id = request.json.get('id')

    try:
        article = Article.get(Article.id == _id)
    except:
        return jsonify(msg="Not Identified User"), 401

    _title = request.json.get('title', -1)
    _text = request.json.get('text',-1)

    if _title == -1 or _text == -1:
        return jsonify(msg="Didn't fill something"), 400

    article.title = _title
    article.text = _text
    article.save()

    return jsonify('Article Created')


@bp.route('/patch', methods=['PATCH'])
def Change():
    if not  request.is_json:
        return jsonify(msg="Missing JSON in headers")

    _id = request.json.get('id')

    try:
        article = Article.get(Article.id == _id)
    except:
        return jsonify(msg="Not Identified User"), 401

    what = request.json.get('what')
    
    if what == 'title':
        _title = request.json.get(what)
        article.title = _title

    elif what == 'text':
        _text = request.form.get(what)
        article.text = _text

    article.save()
    return jsonify(msg="Article Changed")


@bp.route('/delete', methods=['DELETE'])
def Delete():
    _id = request.json.get('id')
    Article.get(Article.id == _id).delete_instance()
    return jsonify('Deleted')

if __name__ == '__main__':
    bp.run()
