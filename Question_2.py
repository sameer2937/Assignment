class FuelStation():
    def __init__(self,diesel,petrol,electric):
        self.diesel=diesel
        self.petrol=petrol
        self.electric=electric
        self.diesel_=0
        self.electric_=0
        self.petrol_=0
        
    def fuel_vehicle(self,vehicle):
        if vehicle=='diesel':
            if self.diesel_<self.diesel:
                self.diesel_+=1
                return True
            else:
                return False
        elif vehicle=='petrol':
            if self.petrol_<self.petrol:
                self.petrol_+=1
                return True
            else:
                return False
        elif vehicle=='electric':
            if self.electric_<self.electric:
                self.electric_+=1
                return True
            else:
                return False
            
    def open_fuel_slot(self,vehicle):
        if vehicle=='diesel':
            if self.diesel_>0:
                self.diesel_-=1
                return True
            else:
                return False
        elif vehicle=='petrol':
            if self.petrol_>0:
                self.petrol_-=1
                return True
            else:
                return False
        elif vehicle=='electric':
            if self.electric_>0:
                self.electric_-=1
                return True
            else:
                return False


fuel_station=FuelStation(diesel=2,petrol=2,electric=1)
print(fuel_station.fuel_vehicle('petrol'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.fuel_vehicle('electric'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.open_fuel_slot('diesel'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.open_fuel_slot('electric'))
print(fuel_station.open_fuel_slot('electric'))