from flask import Flask, url_for, jsonify, Response, json

app = Flask(__name__)


class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


@app.route('/')
def api_home():
    return 'Welcome to the API !'


@app.route('/person/all')
def getPerson():
    person = Person('Delano', 'Junior', 22)

    json = [
        {
            'name': person.name,
            'surname': person.surname,
            'age': person.age
        }
    ]

    return jsonify({'person': json})


@app.route('/getDocument/<movies>')
def getDocumentToRecommend(self, movies: list):

    if __name__ == '__main__':
        app.run()
