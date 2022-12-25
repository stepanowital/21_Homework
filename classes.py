class Storage:
	def __init__(self, capacity=500000):
		self.name = None
		self.items = {}
		self.capacity = capacity
		self.filling = 0

	def add(self, title, quantity):
		self._set_quantity_add(title, quantity)
		print(f"Курьер доставил {quantity} {title} в {self.name}")

	def remove(self, title, quantity):
		current_qnt = self.check_quantity_limits(title)

		if current_qnt > quantity:
			self._set_quantity_remove(title, quantity)
		elif current_qnt == quantity:
			self._set_quantity_remove(title, current_qnt)
			del self.items[title]
		print(f"Курьер забрал {quantity} {title} со {self.name}")

	def check_quantity_limits(self, title):
		current_qnt = self.items[title]
		return current_qnt

	def get_free_space(self):
		return self.capacity - self.filling

	def get_items(self):
		return self.items

	def get_unique_items_count(self):
		return len(self.items)

	def _set_quantity_add(self, title, quantity):
		self.items[title] = self.items.get(title, 0) + quantity
		self.filling += quantity

	def _set_quantity_remove(self, title, quantity):
		self.items[title] -= quantity
		self.filling -= quantity

	def check_item(self, title):
		return title in self.items

	def get_full_report(self):
		print("-" * 20)
		print(f"В {self.name} хранится: ")
		for title, quantity in self.items.items():
			print(quantity, title)
		print(f"Свободного места осталось: {self.get_free_space()}")
		print(f"Количество уникальных товаров {self.get_unique_items_count()}")
		print("-" * 20)


class Store(Storage):
	def __init__(self, capacity=100):
		super().__init__(capacity)
		self.items = {}
		self.name = "склад"

	def __repr__(self):
		return print(self.name)


class Shop(Storage):
	def __init__(self, capacity=20):
		super().__init__(capacity)
		self.unique_items_count = 5
		self.name = "магазин"

	def __repr__(self):
		return print(self.name)


class Request:
	def __init__(self, basic_request):
		self.departure = basic_request.split(" ")[3].lower()
		self.destination = basic_request.split(" ")[5].lower()
		self.amount = int(basic_request.split(" ")[0])
		self.product = basic_request.split(" ")[1].lower()

	def full_request(self):
		return {
			"from": self.departure,
			"to": self.destination,
			"amount": self.amount,
			"product": self.product
		}
