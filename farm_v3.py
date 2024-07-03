# farm_v3.py
# some optimizations and improvements

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
# Backtracking

complement = {
	North: South,
	South: North,
	East: West,
	West: East
}

def backtracking(cond):
	# backtracking algorithm
	# cond: condition to stop
	# ret: function to travel
	def travel(last = North):
		if cond():
			return True
		routes = [North, South, East, West]
		routes.remove(last)
		while(len(routes) > 0):
			next = routes.pop()
			comp = complement[next]
			if move(next):
				if travel(comp):
					return True
				move(comp)
		return False
	return travel

# ----------------------------------------------
# Maze backtracking

def maze_cond():
	return get_entity_type() == Entities.Treasure

def maze_init():
	till_func(Grounds.Turf)
	plant(Entities.Bush)

def maze_loop():
	while(get_entity_type() == Entities.Bush):
		trade_func(Items.Fertilizer, 100)
		use_item(Items.Fertilizer)

def maze_travel():
	backtracking(maze_cond)()
	harvest()

def maze_main():
	while(True):
		maze_init()
		maze_loop()
		maze_travel()

# ----------------------------------------------
# Item

items_data = {
	Items.Fertilizer: {
		"condition": None,
		"trade": Items.Fertilizer,
		"item": Items.Fertilizer
	}
}

def fun_item(item):
	def aux():
		trade_func(items_data[item]["trade"])
		use_item(items_data[item]["item"])
	return aux

# ----------------------------------------------
# Harvest

def harvest_cond(entity):
	return can_harvest() or get_entity_type() != entity

petals_har = False
petals_max = 0
def sunflower_cond(entity):
	petals_max = max(petals_max, measure())
	if get_entity_type() != entity:
		return True
	if petals_har and measure() == petals_max:
		return True
	return False


harvest_data = {
	Entities.Grass: {
		"condition": harvest_cond,
		"ground": Grounds.Turf,
		"seed": None,
		"plant": None
	},
	Entities.Tree: {
		"condition": harvest_cond,
		"ground": Grounds.Soil,
		"seed": None,
		"plant": Entities.Tree
	},
	Entities.Carrots: {
		"condition": harvest_cond,
		"ground": Grounds.Soil,
		"seed": Items.Carrot_Seed,
		"plant": Entities.Carrots
	},
	Entities.Pumpkin: {
		"condition": harvest_cond,
		"ground": Grounds.Soil,
		"seed": Items.Pumpkin_Seed,
		"plant": Entities.Pumpkin
	},
	Entities.Sunflower: {
		"condition": harvest_cond,
		"ground": Grounds.Soil,
		"seed": Items.Sunflower_Seed,
		"plant": Entities.Sunflower
	},
}

def harvest_func(entity):
	data = harvest_data[entity]
	def aux():
		if data["condition"](entity):
			harvest()
			water_func()
			till_func(data["ground"])
			trade_func(data["seed"], 100)
			plant_func(data["plant"])
			return True
		return False
	return aux

# ----------------------------------------------
# Farm

def farm_func(entity, times = 1):
	action = harvest_func(entity)
	def aux():
		for _ in range(times * get_world_size()):
			move(North)
			action()
	return aux

farm_data = {
	0: farm_func(Entities.Grass, 3),
	1: farm_func(Entities.Tree),
	2: farm_func(Entities.Tree),
	3: farm_func(Entities.Carrots),
	4: farm_func(Entities.Carrots),
	5: farm_func(Entities.Pumpkin),
	6: farm_func(Entities.Pumpkin),
	7: farm_func(Entities.Pumpkin),
	8: farm_func(Entities.Pumpkin),
	9: farm_func(Entities.Pumpkin),
}

def farm_main():
	while(True):
		farm_data[get_pos_x()]()
		move(East)

# ----------------------------------------------
# Entrypoint

maze_main()