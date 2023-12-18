import os
import sqlite3
import pandas as pd
from gui import *

app = Application()
documentspath = os.path.expanduser('~\Documents\RevasDataBase')
isExist = os.path.exists(documentspath)
if(not isExist):
    os.makedirs(documentspath)
    connection = sqlite3.connect(fr'{documentspath}\revas.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE wspolczynnik(
            wspolczynnik_id integer PRIMARY KEY,
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
            grudzie float NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE oferty(
            id integer PRIMARY KEY,
            nazwa string NOT NULL,
            popyt_roczny integer NOT NULL,
            cena_za_usluge integer NOT NULL,
            robogodziny float NOT NULL,
            wspolczynniki integer               
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
            id integer PRIMARY KEY,
            imie string NOT NULL,
            nazwisko string NOT NULL,
            wynagrodzenie integer NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE oplaty(
            nazwa string NOT NULL,
            oplata float NOT NULL,
            miesieczna float NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE kredyty(
            ilosc float NOT NULL,
            oprocentowanie float NOT NULL,
            ilosc_rat int NOT NULL
        )
    """)
    connection.commit()
    wspolczynnik_data = {
        'styczen': [],
        'luty': [],
        'marzec': [],
        'kwiecien': [],
        'maj': [],
        'czerwiec': [],
        'lipiec': [],
        'sierpien': [],
        'wrzesien': [],
        'pazdziernik': [],
        'listopad': [],
        'grudzie': []
    }

    oferty_data = {
        'nazwa': [],
        'popyt_roczny': [],
        'cena_za_usluge': [],
        'robogodziny': [],
        'wspolczynniki': []
    }

    zasoby_data = {
        'oferta_id': [],
        'nazwa': [],
        'jakosc': [],
        'cena': []
    }

    pracownicy_data = {
        'imie': [],
        'nazwisko': [],
        'wynagrodzenie': []
    }

    oplaty_data = {
        'nazwa': [],
        'oplata': [],
        'miesieczna': []
    }

    kredyty_data = {
        'ilosc': [],
        'oprocentowanie': [],
        'ilosc_rat': []
    }
    wspolczynniki = pd.DataFrame(wspolczynnik_data)
    oferty = pd.DataFrame(oferty_data)
    zasoby = pd.DataFrame(zasoby_data)
    pracownicy = pd.DataFrame(pracownicy_data)
    oplaty = pd.DataFrame(oplaty_data)
    kredyty = pd.DataFrame(kredyty_data)
else:
    connection = sqlite3.connect(fr'{documentspath}\revas.db')
    wspolczynniki = pd.read_sql('SELECT * FROM wspolczynnik', connection)
    oferty = pd.read_sql('SELECT * FROM oferty', connection, index_col='id')
    zasoby = pd.read_sql('SELECT * FROM zasoby', connection)
    pracownicy = pd.read_sql('SELECT * FROM pracownicy', connection)
    oplaty = pd.read_sql('SELECT * FROM oplaty', connection)
    kredyty = pd.read_sql('SELECT * FROM kredyty', connection)
    for index in oferty.index:
        app.options.append(oferty['nazwa'][index])

def add_ofert():
    oferta = {
        'nazwa': app.nazwa.get(),
        'popyt_roczny': int(app.popyt.get()),
        'cena_za_usluge': int(app.cena.get()),
        'robogodziny': float(app.godziny.get()),
        'wspolczynniki': len(oferty.index)
        }
    oferty.loc[len(oferty.index)] = oferta
    app.nazwa.delete("0", "end")
    app.popyt.delete("0", "end")
    app.cena.delete("0", "end")
    app.godziny.delete("0", "end")
    wspolczynniki.loc[len(wspolczynniki.index)] = wspolczynnikidict
    app.optionslist.append(oferta['nazwa'])
    app.oferta['values'] = app.optionslist

def save_zasoby():
    global zasobydict
    try:
        zasobydict = {
            'oferta_id': len(oferty.index),
            'nazwa': app.zasobytoplevel.nazwa.get(),
            'jakosc': int(app.zasobytoplevel.selected_value.get()),
            'cena': float(app.zasobytoplevel.cena.get())
        }
    except ValueError:
        zasobydict = {}

def save():
    global wspolczynnikidict
    try:
        wspolczynnikidict = {
            'styczen': float(app.wspolczynnikitoplevel.styczen.get()),
            'luty': float(app.wspolczynnikitoplevel.luty.get()),
            'marzec': float(app.wspolczynnikitoplevel.marzec.get()),
            'kwiecien': float(app.wspolczynnikitoplevel.kwiecien.get()),
            'maj': float(app.wspolczynnikitoplevel.maj.get()),
            'czerwiec': float(app.wspolczynnikitoplevel.czerwiec.get()),
            'lipiec': float(app.wspolczynnikitoplevel.lipiec.get()),
            'sierpien': float(app.wspolczynnikitoplevel.sierpien.get()),
            'wrzesien': float(app.wspolczynnikitoplevel.wrzesien.get()),
            'pazdziernik': float(app.wspolczynnikitoplevel.pazdziernik.get()),
            'listopad': float(app.wspolczynnikitoplevel.listopad.get()),
            'grudzien': float(app.wspolczynnikitoplevel.grudzien.get())
        }
    except ValueError:
        wspolczynnikidict = {}

def menu(*args, **kwargs):
    oferta = oferty.iloc[app.oferta.current()]
    wspolczynnik = wspolczynniki.iloc[oferta['wspolczynniki']]
    app.nazwaoferty.configure(text=oferta['nazwa'])
    round = app.round.cget("text")
    popyt = oferta['popyt_roczny'] / 12 * wspolczynnik[round.lower()]
    app.sqlpopyt.configure(text=popyt)
    godziny = oferta['robogodziny'] * popyt
    app.sqlgodziny.configure(text=godziny)
    przychod = oferta['cena_za_usluge'] * popyt
    app.sqlprzychod.configure(text=przychod)

def check():
    global wspolczynnikidict
    if(app.wspolczynnikitoplevel is not None and app.wspolczynnikitoplevel.winfo_exists()):
        app.wspolczynnikitoplevel.save.configure(command=save)
    if(len(wspolczynnikidict)>0 and app.nazwa.get() != "" 
       and app.popyt.get() != "" 
       and app.cena.get() != ""
       and app.godziny.get() != ""):
        app.dodajoferte.configure(command=add_ofert)
    app.after(1000, check)

def to_sql():
    wspolczynniki.to_sql(name='wspolczynniki', con=connection, if_exists='append', index=False)
    oferty.to_sql(name='oferty', con=connection, if_exists='append', index=False)
    zasoby.to_sql(name='zasoby', con=connection, if_exists='append', index=False)
    pracownicy.to_sql(name='pracownicy', con=connection, if_exists='append', index=False)
    oplaty.to_sql(name='oplaty', con=connection, if_exists='append', index=False)
    kredyty.to_sql(name='kredyty', con=connection, if_exists='append', index=False)
    connection.close()

global wspolczynnikidict
wspolczynnikidict = {}
app.after(1000, check)
app.variable.trace_add('write', menu)
app.mainloop()
app.variable.trace_remove('write', 'menu')