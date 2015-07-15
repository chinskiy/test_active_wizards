from flask import Flask, render_template
import pymongo

client = pymongo.MongoClient()
db = client.zipcode

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def mainpage():
    pipe = [{'$group': {'_id': '$city', 'popul': {'$sum': '$pop'}}}]
    query = db.code.aggregate(pipeline=pipe)['result']
    query = sorted(query, key=lambda k: k['popul'], reverse=True)
    query = [{'key': 'Population', 'values': query[0:20]}]
    return render_template('main.html', query=query[0:20])


if __name__ == '__main__':
    app.run()