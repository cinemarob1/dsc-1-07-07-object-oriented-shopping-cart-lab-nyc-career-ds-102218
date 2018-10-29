import statistics

# class ShoppingCart:
# 	def __init__(self,total = 0, employee_discount = None):
# 		self._total = total
# 		self._items = []
# 		self._employee_discount = employee_discount
# 		self._item_prices = []

class ShoppingCart:
	def __init__(self, employee_discount = 0):
		self._items = []
		self._item_names = []
		self._item_prices = []
		self._total = 0
		self._employee_discount = employee_discount*.01
		self._cart_total = 0

	def get_total(self):
		return self._total

	def set_total(self, quantity):
		self._total += quantity

	def get_items(self):
		return self._items

	def set_items(self, item):
		self._items.append(item)

	def get_employee_discount(self):
		return self._employee_discount

	def set_employee_discount(self, employee_discount):
		self._employee_discount = employee_discount

	def item_names(self):
		return self._item_names

	def add_item(self, item, price, quantity = 1):
		self.total = quantity
		self.items = item
		for clothings in range (0, quantity):
			self._item_prices.append(price)
			self._item_names.append(item)
		self._cart_total += price*quantity
		return float(self._cart_total)

	def mean_item_price(self):
		mean = sum(self._item_prices) / self.total
		return mean

	def median_item_price(self):
		median = statistics.median(self._item_prices)
		return median

	def apply_discount(self):
		if self._employee_discount == 0:
			return "Sorry, there is no discount to apply to your cart"
		else:
			subtotal = (sum(self._item_prices)) * (1-self._employee_discount)
			return subtotal

	def void_last_item(self):
		if len(self.items) == 0:
			return "There are no items in your cart!"
		else:
			self._item_names.pop()
			self._item_prices.pop()
			self._cart_total = sum(self._item_prices)
			# self._total += -1

	items = property(get_items, set_items)
	total = property(get_total, set_total)
	employee_discount = property(get_employee_discount, set_employee_discount)

	# @property
	# def total(self):
	# 	return self._total

	# @property
	# def items(self):
	# 	return self._items

	# @property
	# def employee_discount(self):
	# 	return self._employee_discount