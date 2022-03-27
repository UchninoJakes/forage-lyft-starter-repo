from carfactory import CarFactory


class Engine(CarFactory):
    def needs_service(self):
        return self.needs_service()