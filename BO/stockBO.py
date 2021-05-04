
from datetime import date

class Stock:

	def __init__(self):
		super().__init__()
		self._name = None
		self._wkn = None
		self._bought_at = None
		self._currency = None
		self._amount = None
		self._ticker = None
		self._quote = None
		#Profit per stock
		self._profitPS = None

	def get_name(self):
		return self._name

	def set_name(self, name):
		self._name = name

	def get_wkn(self):
		return self._wkn

	def set_wkn(self, wkn):
		self._wkn = wkn

	def get_date(self):
		return self._bought_at

	def set_date(self, day, month, year):
		self._bought_at = date.fromisoformat('{1}-{2}-{3}'.format(year, month, day))

	def set_bought_at(self, amount):
		self._bought_at = amount

	def get_bought_at(self):
		return self._bought_at

	def set_currency(self, currency):
		self._currency = currency

	def get_currency(self):
		return self._currency

	def set_amount(self, amount):
		self._amount = amount

	def get_amount(self):
		return self._amount

	def get_ticker(self):
		return self._ticker

	def set_ticker(self, ticker):
		self._ticker = ticker

	def get_quote(self):
		return self._quote

	def set_quote(self, quote):
		self._quote = quote

	def get_profitPS(self):
		return self._profitPS

	def set_profitPS(self, profit):
		self._profitPS = profit
