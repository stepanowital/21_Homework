from time import sleep


class Storage:
	def __init__(self, capacity=500000):
		self.name = None
		self.items = {}
		self.capacity = capacity
		self.filling = 0

	def add(self, title, quantity):
		if self.get_free_space() >= quantity:
			self.items[title] = self.items.get(title, 0) + quantity
			self.filling += quantity
			print(f"Курьер доставил {quantity} {title} в {self.name}")
		else:
			print(f"Недостаточно места на складе ({self.get_free_space()})")

	def remove(self, title, quantity):
		if not self._check_item(title):
			return print("Запрашиваемого товара нет на складе")

		print("Данный товар есть на складе")
		sleep(1)

		current_qnt = self._check_quantity_limits(title)

		if current_qnt > quantity:
			self.items[title] -= quantity
			self.filling -= quantity
			print(f"Курьер забрал {quantity} {title} со {self.name}")
		elif current_qnt < quantity:
			print(f"На {self.name} недостаточно товара, отгрузили всё, что было")
			self.items[title] -= current_qnt
			self.filling -= current_qnt
			print(f"Курьер забрал {current_qnt} {title} со {self.name}")
			# del self.items[title]
		elif current_qnt == quantity:
			self.items[title] -= current_qnt
			self.filling -= current_qnt
			del self.items[title]
		sleep(1)

	def _check_quantity_limits(self, title):
		current_qnt = self.items[title]
		# if current_qnt < quantity:
		# 	quantity = current_qnt
		return current_qnt

	def get_free_space(self):
		return self.capacity - self.filling

	def get_items(self):
		return self.items

	def get_unique_items_count(self):
		return len(self.items)

	def _check_item(self, title):
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


store = Store()
#
store.add("вафли", 20)
store.add("печеньки", 10)
store.add("пирожки", 40)
store.add("крендельки", 10)
store.add("пирожки", 20)



class Shop(Storage):
	def __init__(self, capacity=20):
		super().__init__(capacity)
		self.unique_items_count = 5
		self.name = "магазин"

	def add(self, title, quantity):
		if self.get_unique_items_count() >= self.unique_items_count:
			print(f"В данном магазине уже есть {self.unique_items_count} разных наименований.")
		else:
			super().add(title, quantity)

	def __repr__(self):
		return print(self.name)


shop = Shop()

# shop.add("Вафли", 3)
# shop.add("Пряники", 3)
# shop.add("Пирожки", 3)
# shop.add("Крендельки", 3)
# shop.add("Вареники", 5)
# shop.add("Пельмени", 7)
# shop.get_full_report()
# shop.remove("Крендельки", 3)
# shop.get_full_report()


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


def main():
	"""
	Интерфейс для работы с клиентом
	"""
	print()
	print("Здравствуйте.")
	print(
		"Вас приветствует программа по перемещению "
		"запасов со склада до выбранного вами магазина.")
	print()

	while True:
		basic_request = input('Введите запрос (Пример: "5 вафли из склад в магазин")\n')

		request = Request(basic_request)

		if request.full_request()["from"] == "склад":
			store.remove(request.full_request()["product"], request.full_request()["amount"])
			sleep(1)
			# if store.remove(request.full_request()["product"], request.full_request()["amount"]) == "Запрашиваемого товара нет на складе":
			# 	break

			print(f'Курьер везет {request.full_request()["amount"]} {request.full_request()["product"]} со склад в магазин')
			sleep(1)

			shop.add(request.full_request()["product"], request.full_request()["amount"])
			sleep(1)

		store.get_full_report()
		sleep(1)
		shop.get_full_report()
		sleep(1)


main()

