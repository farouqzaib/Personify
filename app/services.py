from config import db

class EventService():

	def create(self, event):
		try:
			res = db.es.index(index="events", doc_type='event', id='', body=event)
		except Exception as e:
			print e
			raise Exception('Event could not be saved.')
