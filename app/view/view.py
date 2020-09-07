from app.service.vessel_service import VesselService
from app.service.equipment_service import EquipmentService


class VesselView:

    vessel_service = VesselService()

    def create_table(self):
        self.vessel_service.create_table()

    def insert_vessel(self, code):
        return self.vessel_service.insert_vessel(code)


class EquipmentView:

    equipment_service = EquipmentService()

    def create_table(self):
        self.equipment_service.create_table()

    def insert_equipment(self, equipment_json):
        return self.equipment_service.insert_equipment(equipment_json)

    def update_equipment(self, equipment_json):
        return self.equipment_service.update_equipment(equipment_json)

    def return_all_equipments_actives_by_vessel(self, equipment_json):
        return self.equipment_service.return_active_equipment_by_vessel(equipment_json)
