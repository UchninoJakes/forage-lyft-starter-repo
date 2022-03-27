from car import Car


class CarFactory(Car):
    def __init__(self, current_date, last_service_date, current_mileage,
                 last_service_mileage, warning_light_is_on,
                 engine, battery):
        super().__init__(engine, battery)
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_is_on = warning_light_is_on

    def create_calliope(self):
        return self.create_calliope()

    def create_glissade(self):
        return self.create_glissade()

    def create_palindrome(self):
        return self.create_palindrome()

    def create_rorschach(self):
        return self.create_rorschach()

    def create_thovex(self):
        return self.create_thovex()
    