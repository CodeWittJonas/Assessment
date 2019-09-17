from abc import ABC, abstractmethod
import shelve


class CarWash(object):

    def __init__(self, persistence):
        self.persistence = persistence
        self.sms_sender = SmsSender()

    def register_car_for_wash(self, car, customer):
        job = CarWashJob(car, customer)
        self.persistence[job.job_id] = job
        return job.job_id

    def complete_wash(self, job_id):
        job = self.persistence[job_id]
        self.sms_sender.send(job.contact_details(), job.notification_message())

    def shit(self):
        print("shit")


class Customer(object):

    def __init__(self, name, mobile_phone):
        self.name = name
        self.mobile_phone = mobile_phone


class Car(object):

    def __init__(self, plate):
        self.plate = plate


class Notifier(ABC):

    @abstractmethod
    def send(self, recipient, msg):
        pass


class SmsSender(Notifier):

    def send(self, phone_number, msg):
        print(f'Sending text message to {phone_number}: {msg}')
        # ... do some weird SMS magic


class CallSender(Notifier):

    def send(self, phone_number, msg):
        print(f'Calling {phone_number}: {msg}')


class MailSender(Notifier):

    def send(self, mail_address, msg):
        print(f'Sending Email to {mail_address}: {msg}')


class CarWashJob:
    job_counter = 0

    def __init__(self, car, customer):
        self.car = car
        self.customer = customer
        self.job_id = self.new_job_id()

    def contact_details(self):
        return self.customer.mobile_phone

    def notification_message(self):
        return f'Job {self.job_id}, Car {self.car.plate} washed.'

    @staticmethod
    def new_job_id():
        job_id = CarWashJob.job_counter
        CarWashJob.job_counter += 1
        return f'#{job_id}'


class CarJobRepository(ABC):

    @abstractmethod
    def save(self, car_wash_job):
        pass

    @abstractmethod
    def find_by_id(self, job_id):
        pass


class InMemoryCarJobRepository(CarJobRepository):

    def __init__(self):
        self.jobs = {}

    def save(self, car_wash_job):
        self.jobs[car_wash_job.job_id] = car_wash_job

    def find_by_id(self, job_id):
        if job_id in self.jobs:
            return self.jobs[job_id]
        else:
            raise ValueError(f'No Job with ID {job_id} found.')


class FileCarJobRepository(CarJobRepository):

    def __init__(self, filename, drop_on_startup=True):
        self.filename = filename
        if drop_on_startup:
            self.drop_db()

    def save(self, car_wash_job):
        with shelve.open(self.filename) as db:
            db[car_wash_job.job_id] = car_wash_job
            db.close()

    def find_by_id(self, job_id):
        with shelve.open(self.filename) as db:
            try:
                car_wash_job = db[job_id]
                return car_wash_job
            except KeyError:
                raise ValueError(f'Job ID {job_id} does not exist.')
            finally:
                db.close()

    def drop_db(self):
        with shelve.open(self.filename) as db:
            db.clear()
            db.close()


if __name__ == '__main__':
    car_wash = CarWash()
    car1 = Car('ZH 123456')
    car2 = Car('AG 654321')
    customer1 = Customer('Foo', '079 xxx xxxx')
    customer2 = Customer('Bar', '078 xxx xxxx')

    job_id1 = car_wash.register_car_for_wash(car1, customer1)
    job_id2 = car_wash.register_car_for_wash(car2, customer2)
    assert job_id1 != job_id2

    job = CarWashJob(car1, customer1)



    car_wash.complete_wash(job_id1)
