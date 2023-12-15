import os
import sqlite3
import pandas as pd

documentspath = os.path.expanduser('~\Documents\RevasDataBase')
isExist = os.path.exists(documentspath)
if(not isExist):
    os.makedirs(documentspath)
    connection = sqlite3.connect(fr'{documentspath}\revas.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE wspolczynnik(
            wspolczynnik_id integer NOT NULL AUTO_INCREMENT,
            styczen float NOT NULL,
            luty float NOT NULL,
            marzec float NOT NULL,
            kwiecien float NOT NULL,
            maj float NOT NULL,
            czerwiec float NOT NULL,
            lipiec float NOT NULL,
            sierpien float NOT NULL,
            wrzesien float NOT NULL,
            pazdziernik float NOT NULL,
            listopad float NOT NULL,
            grudzie float NOT NULL,
            PRIMARY KEY (wspolczynnik_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE oferty(
            id integer NOT NULL AUTO_INCREMENT,
            nazwa string NOT NULL,
            popyt_roczny integer NOT NULL,
            cena_za_usluge integer NOT NULL,
            robogodziny float NOT NULL,
            wspolczynniki integer,
            PRIMARY KEY(id)                  
        )
    """)
    cursor.execute("""
        CREATE TABLE zasoby(
            oferta_id integer NOT NULL,
            nazwa string NOT NULL,
            jakosc integer NOT_NULL,
            cena float NOT_NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE pracownicy(
            id inetger NOT NULL AUTO_INCREMENT,
            imie string NOT NULL,
            nazwisko string NOT NULL,
            wynagrodzenie integer NOT NULL,
            PRIMARY KEY(id)
        )
    """)
    cursor.execute("""
        CREATE TABLE oplaty(
            nazwa string NOT NULL,
            oplata float NOT NULL,
            miesieczna float NOT NULL
        )
    """)
    connection.commit()
else:
    connection = sqlite3.connect(fr'{documentspath}\revas.db')