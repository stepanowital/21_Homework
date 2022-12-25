class Request:
	def __init__(self, basic_request, storages):
		self.departure = basic_request.split(" ")[3].lower()
		self.destination = basic_request.split(" ")[5].lower()
		self.amount = int(basic_request.split(" ")[0])
		self.product = basic_request.split(" ")[1].lower()
		self.storages = storages

	def full_request(self):
		return {
			"from": self.departure,
			"to": self.destination,
			"amount": self.amount,
			"product": self.product
		}
