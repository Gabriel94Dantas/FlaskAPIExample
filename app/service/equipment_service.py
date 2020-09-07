from app.entity.equipment import Equipment
from app.entity.vessel import Vessel


def equipment_json_generator(equipment):
    equipment_json = {
        'name': equipment.name,
        'code': equipment.code,
        'status': bool(equipment.status),
        'location': equipment.location,
        'vessel': {
            'code': equipment.vessel.code
        }
    }
    return equipment_json



class EquipmentService:
    equipment_class = Equipment()
    vessel_class = Vessel()

    def insert_equipment(self, equipment_json):
        equipment = Equipment()
        equipment.name = equipment_json['name']
        equipment.code = equipment_json['code']
        equipment.status = equipment_json['status']
        equipment.location = equipment_json['location']
        vessel = Vessel()
        code = self.vessel_class.select_vessel_by_code(equipment_json['vessel_code'])
        if code:
            vessel.code = equipment_json['vessel_code']
            equipment.vessel = vessel
            self.equipment_class.insert(equipment)
            return 201
        return 404

    def create_table(self):
        self.equipment_class.create_table()

    def update_equipment(self, equipment_json):
        status = False
        code = str(equipment_json['code'])
        self.equipment_class.update(status, code)
        return 200

    def return_active_equipment_by_vessel(self, equipment_json):
        vessel_code = equipment_json['vessel_code']
        equipments = self.equipment_class.select_active_equipment_of_vessel(vessel_code)
        equipments_json = []
        for equipment in equipments:
            equipment_generated = equipment_json_generator(equipment)
            equipments_json.append(equipment_generated)
        return equipments_json
