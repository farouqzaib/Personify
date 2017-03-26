from config import db

class EventService():

	@staticmethod
	def create(event):
		try:
			res = db.es.index(index="events", doc_type='event', id='', body=event)
		except Exception as e:
			print e
			raise Exception('Event could not be saved.')
