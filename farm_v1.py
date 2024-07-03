# farm_v1.py
# farm without lists and dictionaries

def water():
	if get_water() == 0:
		use_item(Items.Water_Tank)

def grass():	
	if can_harvest() or get_entity_type() != Entities.Grass:
		harvest()

def tree():
	if can_harvest() or get_entity_type() != Entities.Tree:
		harvest()
		plant(Entities.Tree)

def carrot():
	if can_harvest() or get_entity_type() != Entities.Carrots:
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		trade(Items.Carrot_Seed)
		plant(Entities.Carrots)	

def pumpkin():
	if can_harvest() or get_entity_type() != Entities.Pumpkin:
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		trade(Items.Pumpkin_Seed)
		plant(Entities.Pumpkin)

def move_and_do(func):
	for i in range(get_world_size()):
		move(East)
		for j in range(get_world_size()):
			move(North)
			func()

def clear_and_set():
	clear()
	move_and_do(wait)
	move_and_do(rotate)

def wait():
	pass

def rotate():
	if get_pos_x() == 0:
		grass()
	if get_pos_x() == 1:
		tree()
	if get_pos_x() == 2 or get_pos_x() == 3:
		carrot()
	if get_pos_x() == 4 or get_pos_x() == 5 or get_pos_x() == 6:
		pumpkin()

def converve():
	if get_entity_type() == Entities.Grass:
		return grass()
	if get_entity_type() == Entities.Tree:
		return tree()
	if get_entity_type() == Entities.Carrots:
		return carrot()
	if get_entity_type() == Entities.Pumpkin:
		return pumpkin()


def cycle():
	water()
	rotate()

def main():
	#clear_and_set()
	while(True):
		move_and_do(cycle)

main()	