from data.data import Person
from faker import Faker

faker_en = Faker('en_US')

def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        email=faker_en.email(),
        currents_address=faker_en.address(),
        permanent_address=faker_en.address(),
    )
