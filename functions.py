from time import sleep
from store import Store
from shop import Shop
from request import Request

store = Store()
#
store.add("вафли", 10)
store.add("шоколад", 10)
store.add("печеньки", 10)
store.add("пирожки", 40)
store.add("крендельки", 10)
store.add("конфеты", 20)

shop = Shop()

shop.add("мороженое", 5)

storages = {
	"склад": store,
	"магазин": shop
}
store.get_full_report()
shop.get_full_report()


def main():
	"""
	Интерфейс для работы с клиентом
	"""
	print()
	print("Здравствуйте.")
	print(
		"Вас приветствует программа по перемещению "
		"запасов со склада до магазина или наоборот.")
	print()

	while True:
		basic_request = input(
			'Введите запрос (Пример: "5 вафли из склад в магазин")\n'
			'Введите "стоп" или "stop" чтобы прекратить\n')

		if basic_request in ["stop", "стоп"]:
			break

		request = Request(basic_request, storages)

		if request.destination not in storages or request.departure not in storages:
			print("Введено название неизвестного склада")
			print()
			sleep(1)
			continue

		if request.departure == "склад" and request.destination == "магазин":
			if not store.check_item(request.product):
				print("Данного товара нет на складе")
				print()
				sleep(1)
				continue
			if store.check_quantity_limits(request.product) < request.amount:
				print("Не хватает товара на складе, попробуйте заказать меньше")
				print()
				sleep(1)
				continue

			if shop.get_free_space() < request.amount:
				print(f"В {shop.name}е недостаточно места, попробуйте что-то другое)")
				print()
				sleep(1)
				continue
			if shop.get_unique_items_count() >= shop.unique_items_count:
				if not shop.check_item(request.product):
					print(f"В данном магазине уже есть {shop.unique_items_count} разных наименований.")
					print()
					sleep(1)
					continue
			print("Данный товар есть на складе")
			sleep(1)

			store.remove(
				request.product,
				request.amount)
			sleep(1)

			print(
				f'Курьер везет {request.amount} {request.product} со склада в магазин')
			sleep(1)

			shop.add(request.product, request.amount)
			sleep(1)

			store.get_full_report()
			sleep(1)
			shop.get_full_report()
			sleep(1)

		if request.departure == "магазин" and request.destination == "склад":
			if not shop.check_item(request.product):
				print("Данного товара нет в магазине")
				print()
				sleep(1)
				continue
			if shop.check_quantity_limits(request.product) < request.amount:
				print("Не хватает товара в магазине, попробуйте заказать меньше")
				print()
				sleep(1)
				continue
			if store.get_free_space() < request.amount:
				print(f"На {store.name}е недостаточно места, попробуйте что-то другое)")
				print()
				sleep(1)
				continue

			print("Данный товар есть в магазине")
			sleep(1)

			shop.remove(
				request.product,
				request.amount)
			sleep(1)

			print(
				f'Курьер везет {request.amount} {request.product} из магазина на склад')
			sleep(1)

			store.add(request.product, request.amount)
			sleep(1)

			store.get_full_report()
			sleep(1)
			shop.get_full_report()
			sleep(1)
