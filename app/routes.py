from app import app
from app.view.view import VesselView, EquipmentView
import flask


@app.route('/')
@app.route('/index')
def index():
    vessel_view = VesselView()
    equipment_view = EquipmentView()
    vessel_view.create_table()
    equipment_view.create_table()
    response_json = {'status': 201, 'msg': 'Database and tables created!'}
    return flask.jsonify(response_json)


@app.route('/add/vessel', methods=['POST'])
def insert_vessel():
    json_code = flask.request.get_json()
    vessel_view = VesselView()
    status = vessel_view.insert_vessel(json_code['code'])
    if status == 201:
        response_json = {'status': status, 'msg': 'Vessel created with success'}
    else:
        response_json = {'status': status, 'msg': 'Vessel already created.'}
    return flask.jsonify(response_json)


@app.route('/add/equipment', methods=['POST'])
def insert_equipment():
    json_code = flask.request.get_json()
    equipment_view = EquipmentView()
    status = equipment_view.insert_equipment(json_code)
    if status == 201:
        response_json = {'status': status, 'msg': 'Equipment created with success'}
    else:
        response_json = {'status': status, 'msg': 'Vessel not found'}
    return flask.jsonify(response_json)


@app.route('/update/equipment', methods=['PUT', 'POST'])
def update_equipment():
    json_code = flask.request.get_json()
    equipment_view = EquipmentView()
    status = equipment_view.update_equipment(json_code)
    response_json = {'status': status, 'msg': 'Equipment deactivated.'}
    return flask.jsonify(response_json)


@app.route('/get/equipment/')
def return_actives_equipments_by_vessel():
    vessel_code = {'vessel_code': flask.request.args['vesselCode']}
    equipment_view = EquipmentView()
    equipments_json = equipment_view.return_all_equipments_actives_by_vessel(vessel_code)
    response_json = {'status': 200, 'list': equipments_json}
    return flask.jsonify(response_json)
