from app.entity.vessel import Vessel


class VesselService:

    vessel_class = Vessel()

    def insert_vessel(self, code):
        vessel = Vessel()
        returned_code = self.vessel_class.select_vessel_by_code(code)
        if returned_code:
            return 409
        vessel.code = code
        self.vessel_class.insert(vessel)
        return 201

    def create_table(self):
        self.vessel_class.create_table()
