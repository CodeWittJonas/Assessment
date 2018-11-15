# ========= Your classes ==========
class UniPerson:

    def __init__(self, name):
        self._name = name
        self.__inbox = []

    def receive_email(self, text):
        self.__inbox.append(text)

    def read_emails(self):
        emails = []
        for email in self.__inbox:
            emails.append(email)

        self.__inbox.clear()
        return emails

    def __str__(self):
        return "Name: {}".format(self._name)


class Student(UniPerson):

    students_per_year = {}

    def __init__(self, name, start_year, has_graduated, ects):
        super().__init__(name)
        self.start_year = start_year
        self.has_graduated = has_graduated
        self.__ects = ects
        number = Student.get_update_students_per_year(self, start_year)
        self.__legi_nr = "{}-{}".format(self.start_year, str(number).zfill(5))

    def __str__(self):
        name = super(Student, self).__str__()
        return "{}, Legi-Nr.: {}, Graduated: {}, Ects: {}".format(name, self.__legi_nr,
                                                                  self.has_graduated, self.__ects)

    def receive_email(self, text):
        super().receive_email(text)

    def read_emails(self):
        return super().read_emails()

    @staticmethod
    def get_update_students_per_year(self, year):
        if year in Student.students_per_year:
            Student.students_per_year[year] += 1

        else:
            Student.students_per_year[year] = 0

        return Student.students_per_year[year]


class Lecturer(UniPerson):

    def __init__(self, name, lecture_name):
        super().__init__(name)
        self.__lecture_name = lecture_name

    def __str__(self):
        return super().__str__() + ": " + self.__lecture_name

    def receive_email(self, text):
        super().receive_email(text)

    def read_emails(self):
        return super().read_emails()


class UniManagement:

    def __init__(self):
        self.__persons = []

    def add_person(self, person):
        if isinstance(person, UniPerson):
            self.__persons.append(person)

    def list_persons(self):
        persons = []
        for person in self.__persons:
            persons.append(person.__str__())

        return persons

    def send_email(self, text):
        for person in self.__persons:
            person.receive_email(text)

    def count_alumni(self):
        alumni_counter = 0
        for person in self.__persons:
            if isinstance(person, Student):
                if person.has_graduated:
                    alumni_counter += 1

        return alumni_counter


# ======================================================================================================================


if __name__ == '__main__':
    p1 = UniPerson("Hans Muster")
    assert p1.__str__() == "Name: Hans Muster"

    p1.receive_email("Email 1")
    p1.receive_email("Email 2")
    assert p1.read_emails() == ["Email 1", "Email 2"]
    assert p1.read_emails() == []  # Because inbox was emptied after reading the first time

    s1 = Student("Student 1", 2017, False, 40)
    assert "Student 1" in s1.__str__()
    assert "2017-00000" in s1.__str__()
    assert "False" in s1.__str__()
    assert "40" in s1.__str__()

    s2 = Student("Student 2", 2017, True, 120)
    assert "Student 2" in s2.__str__()
    assert "2017-00001" in s2.__str__()
    assert "True" in s2.__str__()
    assert "120" in s2.__str__()

    s3 = Student("Student 3", 2016, True, 180)
    assert "Student 3" in s3.__str__()
    assert "2016-00000" in s3.__str__()
    assert "True" in s3.__str__()
    assert "180" in s3.__str__()

    mgmt = UniManagement()

    lecturer = Lecturer("Prof. Dr. Harald Gall", "Informatik 1")

    mgmt.add_person(s1)
    mgmt.add_person(s2)
    mgmt.add_person(s3)
    mgmt.add_person(lecturer)

    assert mgmt.count_alumni() == 2

    mgmt.send_email("This test email is sent to all university persons.")
    assert s1.read_emails() == ["This test email is sent to all university persons."]
    assert s2.read_emails() == ["This test email is sent to all university persons."]
    assert s3.read_emails() == ["This test email is sent to all university persons."]
    assert lecturer.read_emails() == ["This test email is sent to all university persons."]
