import os

from onvif import ONVIFCamera

IP = os.environ['CAMIP']
PORT = os.environ['CAMPORT']  # Port
USER = os.environ['CAMUSER']  # Username
PASS = os.environ['CAMPASS']  # Password


def get_presets_by_id(self):
	mycam = ONVIFCamera(IP, PORT, USER, PASS, 'wsdl/')
	ptz_service = mycam.create_ptz_service()
	preset_list = ptz_service.GetPresets('000')
	preset_list = str(preset_list).replace("\'", "\"")
	print(preset_list)
	return preset_list


def goto_preset(id):
	mycam = ONVIFCamera(IP, PORT, USER, PASS, 'wsdl/')
	ptz_service = mycam.create_ptz_service()
	ptz_params = {'ProfileToken': '000', 'PresetToken': id}
	go = ptz_service.GotoPreset(ptz_params)

	return 'ok'
