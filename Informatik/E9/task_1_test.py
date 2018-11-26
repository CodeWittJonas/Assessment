import os
from unittest import TestCase

import task_1 as car_wash_service


class CarWashJobTest(TestCase):

    def setUp(self):
        self.car1 = car_wash_service.Car('ZH 123456')
        self.car2 = car_wash_service.Car('AG 654321')
        self.customer1 = car_wash_service.Customer('Foo', '079 xxx xxxx')

    def test_car_wash_job_unique_ids(self):
        ids = [car_wash_service.CarWashJob(None, None).job_id for i in range(1000)]
        self.assertEqual(len(set(ids)), len(ids), 'Ids should be unique for each car wash job!')

    def test_car_wash_job_without_id(self):
        job = car_wash_service.CarWashJob(self.car1, self.customer1)
        self.assertIsNotNone(job.job_id, 'The constructor should create a new id if none was given!')

    def test_notification_message(self):
        job = car_wash_service.CarWashJob(self.car1, self.customer1)
        self.assertEqual(f'Job {job.job_id}, Car {self.car1.plate} washed.', job.notification_message(),
                         'The notification message seems wrong...')

    def test_contact_details(self):
        job = car_wash_service.CarWashJob(self.car1, self.customer1)
        self.assertEqual(self.customer1.mobile_phone, job.contact_details(), 'Wrong phone number!')


class CarJobRepositoryTest(TestCase):

    def setUp(self):
        self.car1 = car_wash_service.Car('ZH 123456')
        self.car2 = car_wash_service.Car('AG 654321')
        self.customer1 = car_wash_service.Customer('Foo', '079 xxx xxxx')
        self.customer2 = car_wash_service.Customer('Bar', '078 xxx xxxx')
        self.filename = 'test-db.tsv'

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_file_db_save_and_retrieve(self):
        file_db = car_wash_service.FileCarJobRepository(self.filename)
        job = car_wash_service.CarWashJob(self.car1, self.customer1)

        file_db.save(job)

        retrieved_job = file_db.find_by_id(job.job_id)

        self.assert_job_equals(retrieved_job, job)

    def test_inmemory_save_and_retrieve(self):
        in_memory_db = car_wash_service.InMemoryCarJobRepository()
        job = car_wash_service.CarWashJob(self.car1, self.customer1)

        in_memory_db.save(job)

        retrieved_job = in_memory_db.find_by_id(job.job_id)

        self.assert_job_equals(retrieved_job, job)

    def test_drop_db(self):
        file_db = car_wash_service.FileCarJobRepository(self.filename)
        job1 = car_wash_service.CarWashJob(self.car1, self.customer1)
        job2 = car_wash_service.CarWashJob(self.car2, self.customer2)

        file_db.save(job1)
        file_db.save(job2)

        file_db.drop_db()

        with self.assertRaises(ValueError):
            file_db.find_by_id(job1.job_id)

        with self.assertRaises(ValueError):
            file_db.find_by_id(job2.job_id)

    def assert_job_equals(self, left, right):
        self.assertEqual(left.job_id, right.job_id)
        self.assertEqual(left.car.plate, right.car.plate)
        self.assertEqual(left.customer.name, right.customer.name)
        self.assertEqual(left.customer.mobile_phone, right.customer.mobile_phone)
