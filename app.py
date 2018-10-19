from flask import Flask, jsonify
import db_connections


app = Flask(__name__, static_url_path='')


@app.route('/')
def homepage():
	return app.send_static_file('index.html')

@app.route("/pens/<pen_id>")
def data(pen_id):
	content = db_connections.get_pen(int(pen_id))

	return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')