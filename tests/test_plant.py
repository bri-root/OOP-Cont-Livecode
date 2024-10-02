from classes.plant import Plant


def test_plant_initialization():
    
    # Arrange
    name = "Butterfly pear flower"
    water_level = 7
    sunlight_hours = 6
    is_blooming = True

    # Act
    plant = Plant(name, water_level, sunlight_hours, is_blooming)

    plant_2 = Plant(name, water_level, sunlight_hours)

    # Assert
    assert plant.name == name 
    assert plant.water_level == water_level 
    assert plant.sunlight_hours == sunlight_hours 
    assert plant.is_blooming  # don't need to check against it because it is True


    assert not plant_2.is_blooming # because fasly should result to True


def test_plant_watering():

    # Arrange
    amount = 3
    air_plant = Plant("Air Plant", 0, 8, False)
    expected = 3

    # Act
    result = air_plant.water(amount)
    # Assert
    assert result == f"Air Plant new water level: {expected}"
    assert air_plant.water_level == expected


def test_growth_stage_after_watering():
    # Arrange
    baby_tears = Plant("Baby Tears", 3, 6, True)
    amount = 3

    # Act
    before_water = baby_tears.check_growth()
    baby_tears.water(amount)
    after_water = baby_tears.check_growth()

    # Assert
    assert before_water == "sprout"
    assert after_water == "mature"