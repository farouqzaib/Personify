from services import EventService

service_locator = dict()

eventService = EventService()

service_locator['eventService'] = eventService
