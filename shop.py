from abstract_class import Storage


class Shop(Storage):
	def __init__(self, capacity=20):
		super().__init__(capacity)
		self.unique_items_count = 5
		self.name = "магазин"

	def __repr__(self):
		return print(self.name)
