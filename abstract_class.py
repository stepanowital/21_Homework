from abc import ABC


class Storage(ABC):
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
		print(f"Курьер забрал {quantity} {title} из {self.name}")

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
		print(f"В {self.name}е хранится: ")
		for title, quantity in self.items.items():
			print(quantity, title)
		print(f"Свободного места осталось: {self.get_free_space()}")
		print(f"Количество уникальных товаров {self.get_unique_items_count()}")
		print("-" * 20)
