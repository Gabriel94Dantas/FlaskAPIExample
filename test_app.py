import pytest
from provaModec import app
from app.entity.vessel import Vessel
from app.entity.equipment import Equipment


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_index(client):
    response = client.get("/index")
    json = response.get_json()
    assert 201 == json['status']
    assert 'Database and tables created!' == json['msg']


def test_insert_vessels(client):
    vessel = Vessel()
    vessel.delete_all()
    vessel_json1 = {'code': 'MV100'}
    vessel_json2 = {'code': 'MV101'}
    vessel_json3 = {'code': 'MV102'}
    response = client.post("/add/vessel", json=vessel_json1)
    json = response.get_json()
    assert 201 == json['status']
    assert 'Vessel created with success' == json['msg']
    response = client.post("/add/vessel", json=vessel_json2)
    json = response.get_json()
    assert 201 == json['status']
    assert 'Vessel created with success' == json['msg']
    response = client.post("/add/vessel", json=vessel_json3)
    json = response.get_json()
    assert 201 == json['status']
    assert 'Vessel created with success' == json['msg']


def test_insert_equal_vessel(client):
    vessel_json = {'code': 'MV100'}
    response = client.post("/add/vessel", json=vessel_json)
    json = response.get_json()
    assert 409 == json['status']
    assert 'Vessel already created.' == json['msg']


def test_insert_equipment_correct_vessel(client):
    equipment_class = Equipment()
    equipment_class.delete_all()
    equipment1 = {
        'name': 'compressor',
        'code': '5310B9D7',
        'status': True,
        'location': 'Brazil',
        'vessel_code': 'MV100'
    }

    equipment2 = {
        'name': 'decompressor',
        'code': '3410B9R4',
        'status': True,
        'location': 'Brazil',
        'vessel_code': 'MV100'
    }

    equipment3 = {
        'name': 'valve',
        'code': '8760B9R4',
        'status': True,
        'location': 'Brazil',
        'vessel_code': 'MV100'
    }

    response = client.post("/add/equipment", json=equipment1)
    json = response.get_json()
    assert 201 == json['status']
    assert 'Equipment created with success' == json['msg']

    response = client.post("/add/equipment", json=equipment2)
    json = response.get_json()
    assert 201 == json['status']
    assert 'Equipment created with success' == json['msg']

    response = client.post("/add/equipment", json=equipment3)
    json = response.get_json()
    assert 201 == json['status']
    assert 'Equipment created with success' == json['msg']


def test_insert_equipment_wrong_vessel(client):
    equipment = {
        'name': 'compressor',
        'code': '5310B9D7',
        'status': True,
        'location': 'Brazil',
        'vessel_code': 'MV109'
    }

    response = client.post("/add/equipment", json=equipment)
    json = response.get_json()
    assert 404 == json['status']
    assert 'Vessel not found' == json['msg']


def test_deactivation(client):
    equipment = {'code': '8760B9R4'}
    response = client.put("/update/equipment", json=equipment)
    json = response.get_json()
    assert 200 == json['status']
    assert 'Equipment deactivated.' == json['msg']


def test_return_equipments_actived_by_vessel_code(client):
    response = client.get("/get/equipment/?vesselCode=MV100")
    json = response.get_json()
    assert 200 == json['status']
    assert [{
        'name': 'compressor',
        'code': '5310B9D7',
        'status': True,
        'location': 'Brazil',
        'vessel': {'code': 'MV100'}
    }, {
        'name': 'decompressor',
        'code': '3410B9R4',
        'status': True,
        'location': 'Brazil',
        'vessel': {'code': 'MV100'}
    }] == json['list']
