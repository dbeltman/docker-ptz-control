from flask import Flask

import components.presets as presets

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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
