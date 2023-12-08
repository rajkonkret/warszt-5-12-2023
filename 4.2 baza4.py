from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///moja_baza_danych.db")
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')


class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates='publisher')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')
    publisher = relationship("Publisher", back_populates='books')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# new_author = Author(name='Adam Mickiewicz')
# new_publisher = Publisher(name='Wydawnictwo Pruszyński')
# new_book = Book(title="Pan Tadeusz", author=new_author, publisher=new_publisher)
#
# session.add_all(
#     [new_author, new_publisher, new_book]
# )

session.commit()

# odczytac z bazy autorow i z autorow ksiazki i wypisac ładnie
authors = session.query(Author).all()
print(authors)

for author in authors:
    print(f"Author: {author.name}")
    for b in author.books:
        print(f"Kaiązka {b.title}, wydawca: {b.publisher.name}")
# [<__main__.Author object at 0x0000014CC9B4D810>]
# Author: Adam Mickiewicz
# Kaiązka Pan Tadeusz, wydawca: Wydawnictwo Pruszyński
print("---------")
publishers = session.query(Publisher).all()
for publisher in publishers:
    print(f"Wydawca: {publisher.name}")
    for book in publisher.books:
        print(f"""Ksiązka: {book.title}
Author: {book.author.name}""")
# ---------
# Wydawca: Wydawnictwo Pruszyński
# Ksiązka: Pan Tadeusz
# Author: Adam Mickiewicz
# 11:15
