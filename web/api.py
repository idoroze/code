from flask import request, jsonify, redirect, url_for,Blueprint

app_api = Blueprint('api',__name__)

@app_api.route('/set_stat', methods=['GET', 'POST'])
def setVal():
    if request.method == 'POST':
        i = request.form['num']
        i = int(i)
        if i >= 1 and i <= 3:
            with open('test.txt', 'w+') as db:
                db.write(f"{i}")
                db.close()
            return jsonify({"data": i})
        else:
            return redirect(url_for('/get_stat'))


@app_api.route('/get_stat', methods=['GET'])
def getVal():
    with open('test.txt', 'r') as db:
        x = db.read()
        print(x)
        db.close()
        return jsonify({"data": x})
