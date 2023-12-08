# sqlalchemy  system orm do wspólparcy z bazami danych
# ORM - Object-Relational Mapping
# pip install sqlalchemy
from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine
)

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


# encje - klasy odwzorowujące tabele w bazie danych
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship('Address',
                             back_populates='person',
                             order_by='Address.email',
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

anakin = Person(name='Anakin', age=38)
obi = Person(name="Obi Wan Kenobi", age=45)

obi.addresses = [
    Address(email='obi@example.com'),
    Address(email='waka@wp.pl')
]
obi2 = Person(name="obi", age=54)
session.add(anakin)
session.add(obi)
session.add(obi2)
session.commit()

all_ = session.query(Person).all()
print(all_)  # [Anakin (id=1), Obi Wan Kenobi (id=2)]

an1 = session.query(Person).first()
print(an1)
print(type(an1))  # <class '__main__.Person'>
print(an1.id, an1.name, an1.addresses)  # 1 Anakin []

obi_list = session.query(Person).filter(
    Person.name.like('Obi%')
).all()
print(obi_list)  # [Obi Wan Kenobi (id=2), Obi (id=3)]
for o in obi_list:
    print("id=", o.id, "name:", o.name, "age:", o.age, "email:", o.addresses)

# id= 2 name: Obi Wan Kenobi age: 45 email: [obi@example.com, waka@wp.pl]
# id= 3 name: obi age: 54 email: []
