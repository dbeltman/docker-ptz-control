import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse

import components.ptz as presets

app = Starlette(debug=True)


@app.route('/')
async def homepage(request):
	return JSONResponse({'hello': 'world'})


@app.route('/presets')
async def list_presets(self=None):
	preset_list = presets.get_presets_by_id(self)
	return str(preset_list)


@app.route("/goto/<preset_id>")
async def goto_preset(preset_id):
	result = presets.goto_preset(preset_id)
	return result


if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=5000)
