from flask import Flask, render_template

app = Flask(__name__)


@app.route('/table/<p>/<int:age>')
def table(p, age):
    return render_template('dz2.html', p=p, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')