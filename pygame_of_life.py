import sys, time, pygame

BOARD_WIDTH  = 640
BOARD_HEIGHT = 480
TILE_SIZE = 10
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 0, 255, 255

class Life(dict): # making it a dictionary makes it faster. don't have to represent empty arrays, saves time iterating
	def __init__(self, *args, **kwargs):
		super(Life, self).__init__(*args, **kwargs)

	def __missing__(self, *args, **kwargs): 
		return 0

	def check_neighbors(self, x: int, y: int):
		x_coords = (x - 1, x, x + 1)
		y_coords = (y - 1, y, y + 1)
		count = 0

		for x_coord in x_coords:
			for y_coord in y_coords:
				count += self[x_coord, y_coord]
		
		live, dead = [], []
		cell = self[x, y]
		if count == 3 and not cell:
			live.append((x, y))
		elif count < 2 or count > 4 and cell:
			dead.append((x, y))
		elif cell: # this catches the case where it's alive and has 3 neighbors
			pass
		return live, dead

	def queue_cells(self):
		cells = []
		for x, y in self.keys():
			x_coords = (x - 1, x, x + 1)
			y_coords = (y - 1, y, y + 1)
			for x_coord in x_coords:
				for y_coord in y_coords:
					cells.append((x_coord, y_coord))
		return cells

	def play_game(self):
		live, dead = [], []
		for x, y in self.queue_cells():
			step_live, step_dead = self.check_neighbors(x, y)
			live += step_live
			dead += step_dead
		for x, y in dead:
			if self[x, y]:
				del self[x, y]
		for x, y in live:
			self[x, y] = 1

	def clear_screen(self):
		self.screen.fill(DEAD_COLOR)

	def draw_game(self):
		for x, y in self.keys():
			pygame.draw.circle(self.screen, ALIVE_COLOR, (x * TILE_SIZE, y * TILE_SIZE), TILE_SIZE / 2)
		pygame.display.flip()

	def run(self):
		pygame.init()
		self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
		pygame.display.set_caption("Conway's Game of Life")

		while True:
			self.clear_screen()
			self.play_game()
			self.draw_game()

			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()

if __name__ == '__main__':
	game = Life(
		{
			(25, 25): 1,
			(26, 25): 1,
			(25, 26): 1,
			(24, 26): 1,
			(25, 27): 1
		}
	) # this is a stable pattern, so not so much fun.  but you can put other stuff in here too
	game.run()
