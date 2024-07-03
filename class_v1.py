# class_v1.py
# some experiments defining basic classes using functions
# classes have a very basic inheritance and polymorphism

# ----------------------------------------------
# Utils

def till_func(ground):
	if get_ground_type() != ground:
		till()

def trade_func(item, num = 100):
	if item and num_items(item) < 50:
		trade(item, num)

def plant_func(entity):
	if entity:
		plant(entity)

def water_func():
	if get_water() == 0:
		use_item(Items.Water_Tank)

# ----------------------------------------------
# Class

def c_call(self):
    def aux(key):
        return self[key](self)
    return aux

def c_get(self):
    def aux(key):
        return self[key]
    return aux

def c_set(self):
    def aux(key, value):
        self[key] = value
    return aux

def f_init(self):
    def init():
        return self
    return init

def c_base():
    return {
        "__init__": f_init
    }

def c_class(super = c_base()):
    return dict(super)

def c_init(self):
    obj = dict(self)
    return obj["__init__"](obj)

# ----------------------------------------------
# Farmeable

cicle = c_class()

def f_cicle(self):
    def aux(func):
        for _ in range(c_get(self)("times") * get_world_size()):
            move(North)
            c_call(self)(func)()  
    return aux
c_set(cicle)("cicle", f_cicle)

farmeable = c_class(cicle)

def f_farmeable_init(self):
    def aux(times = 1):
        self["times"] = times
        return self
    return aux
c_set(farmeable)("__init__", f_farmeable_init)

def f_farmeable(self):
    def aux():
        harvest()
        water_func()
        till_func(c_get(self)("ground"))
        trade_func(c_get(self)("seed"))
        plant_func(c_get(self)("plant"))
        return True
    return aux
c_set(farmeable)("farm", f_farmeable)

grass = c_class(farmeable)
grass["ground"] = Grounds.Turf
grass["seed"] = None
grass["plant"] = Entities.Grass

tree = c_class(farmeable)
tree["ground"] = Grounds.Soil
tree["seed"] = None
tree["plant"] = Entities.Tree

carrots = c_class(farmeable)
carrots["ground"] = Grounds.Soil
carrots["seed"] = Items.Carrot_Seed
carrots["plant"] = Entities.Carrots

pumpkin = c_class(farmeable)
pumpkin["ground"] = Grounds.Soil
pumpkin["seed"] = Items.Pumpkin_Seed
pumpkin["plant"] = Entities.Pumpkin

farm_data = {
    0: c_init(grass)(3),
    1: c_init(tree)(),
    2: c_init(tree)(),
    3: c_init(carrots)(),
    4: c_init(carrots)(),
    5: c_init(pumpkin)(),
    6: c_init(pumpkin)(),
    7: c_init(pumpkin)(),
    8: c_init(pumpkin)(),
    9: c_init(pumpkin)()
}

def farm_main():
    while(True):
        obj = farm_data[get_pos_x()]
        c_call(obj)("cicle")("farm")
        move(East)

farm_main()