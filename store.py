from abstract_class import Storage


class Store(Storage):
	def __init__(self, capacity=100):
		super().__init__(capacity)
		self.name = "склад"

	def __repr__(self):
		return print(self.name)
