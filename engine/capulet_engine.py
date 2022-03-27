from carfactory import CarFactory
from engine import Engine


class CapuletEngine(CarFactory, Engine):
    @property
    def needs_service(self):
        return self.needs_service()
