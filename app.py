from flask import Flask, request
import os
import components.db as database
from components.ptz import get_presets_by_id, goto_preset, get_preset_id_by_name

app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello, World!"


@app.route("/presets")
def list_presets():
	preset_list = get_presets_by_id()
	return str(preset_list)


@app.route("/goto/<id>")
def go_to_preset_by_id(id):
	result = goto_preset(id)
	return result


@app.route("/preset", methods=['POST', 'GET'])
def set_to_preset():
	if request.method == 'POST':
		preset_name = request.data.decode("utf-8")
		preset_id = get_preset_id_by_name(preset_name)
		goto_preset(preset_id)
		database.update_value_to_db('current_preset', 'states', str(preset_name))
		return 'ok'

	elif request.method == 'GET':
		preset_name = database.get_value_from_db('current_preset', 'states')
		return preset_name


if __name__ == '__main__':
	if os.environ['env'] == 'prod':
		debug_state = False
	elif os.environ['env'] == 'dev':
		debug_state = True
	else:
		debug_state = True
	app.run(debug=debug_state, host='0.0.0.0')
