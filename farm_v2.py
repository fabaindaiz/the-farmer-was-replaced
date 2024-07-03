# farm_v2.py
# farm without dictionaries

# ----------------------------------------------
# Logic

def fun_buy(item, num):
	if num_items(item) < 5:
		trade(item, num)

def fun_till(ground):
	if get_ground_type() != ground:
		till()

def fun_water():
	if get_water() == 0:
		use_item(Items.Water_Tank)

def fun_move(func):
	for i in range(get_world_size()):
		cond = move(North)
		func(cond)

def fun_none():
	pass

def fun_harvest(entity, func):
	fun_water()
	if can_harvest() or get_entity_type() != entity:
		harvest()
		func()

# ----------------------------------------------
# Harvest

def fun_tree():
		fun_till(Grounds.Soil)
		plant(Entities.Tree)

def fun_carrot():
		fun_till(Grounds.Soil)
		fun_buy(Items.Carrot_Seed, 100)
		plant(Entities.Carrots)

def fun_pumpkin():
		fun_till(Grounds.Soil)
		fun_buy(Items.Pumpkin_Seed, 100)
		plant(Entities.Pumpkin)

def grass():
	fun_harvest(Entities.Grass, fun_none)

def tree():
	fun_harvest(Entities.Tree, fun_tree)

def carrot():
	fun_harvest(Entities.Carrots, fun_carrot)

def pumpkin():
	fun_harvest(Entities.Pumpkin, fun_pumpkin)

# ----------------------------------------------
# Farm

crops = {0: grass, 
		 1: tree,
		 2: tree,
		 3: carrot,
		 4: carrot,
		 5: pumpkin,
		 6: pumpkin,
		 7: pumpkin,
		 8: pumpkin,
		 9: pumpkin}

def main_farm():
	def fun_farm(cond):
		crops[get_pos_x()]()

	while(True):
		fun_move(fun_farm)
		if get_entity_type() == Entities.Grass:
			for i in range(3):
				fun_move(fun_farm)
		move(East)

# ----------------------------------------------
# Maze
complement = {North: South, South: North, East: West, West: East}

def backtracking(last):
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
	
	routes = [North, South, East, West]
	routes.remove(last)
	while(len(routes) > 0):
		next = routes.pop()
		comp = complement[next]
		if move(next):
			if backtracking(comp):
				return True
			move(comp)
	return False

def maze_bush():
	fun_till(Grounds.Turf)
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	fun_buy(Items.Fertilizer, 100)
	use_item(Items.Fertilizer)

def main_maze():
	def fun_maze(cond):
		if not cond:
			backtracking(North)

	while(True):
		maze_bush()
		fun_move(fun_maze)

main_maze()	