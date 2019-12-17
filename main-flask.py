from flask import Flask
import os
import components.ptz as presets

app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello, World!"


@app.route("/presets")
def list_presets():
	preset_list = presets.get_presets_by_id()
	return str(preset_list)


@app.route("/goto/<id>")
def goto_preset(id):
	result = presets.goto_preset(id)
	return result

@app.route("/sweep/<home>")
def sweep(home):
	result =


if __name__ == '__main__':
	if os.environ['env'] == 'prod':
		debug_state = False
	elif os.environ['env'] == 'dev':
		debug_state = True
	else:
		debug_state = True
	app.run(debug=debug_state, host='0.0.0.0')
