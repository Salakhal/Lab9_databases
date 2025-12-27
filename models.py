from sqlalchemy import (
    create_engine, Column, Integer, String,
    ForeignKey, Date
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
engine = create_engine(
    "mysql+pymysql://root:12@localhost/universite"
)

Session = sessionmaker(bind=engine)
Base = declarative_base()

class Etudiant(Base):
    __tablename__ = "ETUDIANT"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    inscriptions = relationship("Inscription", back_populates="etudiant")

class Professeur(Base):
    __tablename__ = "PROFESSEUR"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)

class Cours(Base):
    __tablename__ = "COURS"
    id = Column(Integer, primary_key=True)
    titre = Column(String(150), nullable=False)
    credits = Column(Integer, default=3)

class Inscription(Base):
    __tablename__ = "INSCRIPTION"
    id = Column(Integer, primary_key=True)
    etudiant_id = Column(Integer, ForeignKey("ETUDIANT.id"))
    cours_id = Column(Integer, ForeignKey("COURS.id"))

    etudiant = relationship("Etudiant", back_populates="inscriptions")
    cours = relationship("Cours")

class Examen(Base):
    __tablename__ = "EXAMEN"
    id = Column(Integer, primary_key=True)
    date_exam = Column(Date)
    cours_id = Column(Integer, ForeignKey("COURS.id"))
