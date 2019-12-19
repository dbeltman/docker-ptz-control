import json


def update_value_to_db(target_key, database, value):
	db_path = ''
	root_key = ''
	if database == 'states':
		db_path = 'state_db.json'
		root_key = 'states'
	elif database == 'presets':
		db_path = 'preset_db.json'
		root_key = 'presets'
	db = open(db_path, "r")
	json_db = json.load(db)
	db.close()
	json_db[root_key][target_key] = value
	db = open(db_path, 'w')
	json.dump(json_db, db)
	db.close()
	return value


def get_value_from_db(target_key, database):
	db_path = ''
	root_key = ''
	if database == 'states':
		db_path = 'state_db.json'
		root_key = 'states'
	elif database == 'presets':
		db_path = 'preset_db.json'
		root_key = 'presets'

	db = open(db_path, 'r')
	dict_db = json.load(db)
	db.close()
	value = dict_db[root_key][target_key]
	return value
