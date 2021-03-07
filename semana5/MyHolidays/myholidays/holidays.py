from datetime import date, datetime

class MyCalendar:
	def __init__(self, *args):
		self.datas = []
	#	self.add_holiday(*args)



	def check_holiday(self, data):
		return self.validate_data(data) in self.datas

	def validate_data(self, data):
		if isinstance(data, date):
			return data
		elif isinstance(data, str):
			try:
				return datetime.strptime(data, '%d/%m/%Y').date()
			except:
				return None
