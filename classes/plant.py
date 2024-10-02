class Plant:

    def __init__(self, name, water_level, sunlight_hours, is_blooming=False):
        self.name = name
        self. water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.is_blooming = is_blooming


    def water(self, water_amount):
        self.water_level += water_amount 
        
        return f"{self.name} new water level: {self.water_level}"
    
    def give_sunlight(self, hours):
        self.sunlight_hours += hours

        return f"{self.name} new sunlight hours: {self.sunlight_hours}"
    
    # using attributes to produce new data 
    def check_growth(self):
        if self.sunlight_hours > 5 and self.water_level > 5:
            return "mature"
        else:
            return "sprout"


plant = Plant("Butterfly pear flower", 6, 7)

print(plant.check_growth())

# print(plant.name, plant.water_level, plant.sunlight_hours, plant.is_blooming)

# can rearrange the names:
# print(plant.name, plant.is_blooming, plant.sunlight_hours, plant.water_level)