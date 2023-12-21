import os
import sqlite3
import pandas as pd
from gui import *

app = Application()
miesiace = [
    'styczen',
    'luty',
    'marzec',
    'kwiecien',
    'maj',
    'czerwiec',
    'lipiec',
    'sierpien',
    'wrzesien',
    'pazdziernik',
    'listopad',
    'grudzien'
]
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
            cena float NOT_NULL,
            sprzedaz integer NOT NULL,
            jednostka integer NOT NULL
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
            miesieczna float NOT NULL,
            miesiac string NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE kredyty(
            ilosc float NOT NULL,
            oprocentowanie float NOT NULL,
            ilosc_rat int NOT NULL,
            miesiac string NOT NULL
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
        'cena': [],
        'sprzedaz': [],
        'jednostka': []
    }

    pracownicy_data = {
        'imie': [],
        'nazwisko': [],
        'wynagrodzenie': []
    }

    oplaty_data = {
        'nazwa': [],
        'oplata': [],
        'miesieczna': [],
        'miesiac': []
    }

    kredyty_data = {
        'ilosc': [],
        'oprocentowanie': [],
        'ilosc_rat': [],
        'miesiac': []
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

def add_kredyt():
    kredyt = {
        'ilosc': app.ilosc.get(),
        'oprocentowanie': app.oprocentowanie.get(),
        'ilosc_rat': app.iloscrat.get(),
        'miesiac': app.round.cget("text")
    }   
    kredyty.loc[len(kredyty.index)] = kredyt
    app.ilosc.delete("0", "end")
    app.ilosc.insert(0,1)
    app.oprocentowanie.delete("0", "end")
    app.oprocentowanie.insert(0,1)
    app.iloscrat.delete("0", "end")
    app.iloscrat.insert(0,1)
    print(kredyty)

def add():
    if(int(app.zasobytoplevel.selected_value.get())==1):
        jakosc = "⭐"
    elif(int(app.zasobytoplevel.selected_value.get())==2):
        jakosc = "⭐⭐"
    elif(int(app.zasobytoplevel.selected_value.get())==3):
        jakosc = "⭐⭐⭐"
    app.zasobytoplevel.zasobylist.append(f'Nazwa: {app.zasobytoplevel.nazwa.get()} | Jakość: {jakosc}')
    app.zasobytoplevel.zasoby['values'] = app.zasobytoplevel.zasobylist
    zasob = {
        'oferta_id': len(oferty.index),
        'nazwa': app.zasobytoplevel.nazwa.get(),
        'jakosc': int(app.zasobytoplevel.selected_value.get()),
        'cena': float(app.zasobytoplevel.cena.get()),
        'sprzedaz': int(app.zasobytoplevel.wielkosc.get()),
        'jednostka': int(app.zasobytoplevel.potrzeba.get())
    }
    zasoby.loc[len(zasoby.index)] = zasob
    app.zasobytoplevel.nazwa.delete("0", "end")
    app.zasobytoplevel.cena.delete("0", "end")
    app.zasobytoplevel.cena.insert(0,1)
    app.zasobytoplevel.wielkosc.delete("0", "end")
    app.zasobytoplevel.wielkosc.insert(0,1)
    app.zasobytoplevel.potrzeba.delete("0", "end")
    app.zasobytoplevel.potrzeba.insert(0,1)

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

def add_pracownicy():
    pracownik = {
        'imie': app.imie.get(),
        'nazwisko': app.nazwisko.get(),
        'wynagrodzenie': int(app.wynagrodzenie.get())
    }
    pracownicy.loc[len(pracownicy.index)] = pracownik
    app.imie.delete("0", "end")
    app.nazwisko.delete("0", "end")
    app.wynagrodzenie.delete("0", "end")
    app.wynagrodzenie.insert(0,1)

def add_oplaty():
    oplata = {
        'nazwa': app.nazwaoplaty.get(),
        'oplata': float(app.oplata.get()),
        'miesieczna': float(app.oplatamiesieczna.get()),
        'miesiac': app.round.cget("text")
    }
    oplaty.loc[len(oplaty.index)] = oplata
    app.nazwaoplaty.delete("0", "end")
    app.oplata.delete("0", "end")
    app.oplata.insert(0,1)
    app.oplatamiesieczna.delete("0", "end")
    app.oplatamiesieczna.insert(0,1)

def menu(*args):
    global calyprzychod, calydochod
    oferta = oferty.iloc[app.oferta.current()]
    wspolczynnik = wspolczynniki.iloc[oferta['wspolczynniki']]
    app.nazwaoferty.configure(text=oferta['nazwa'])
    round = app.round.cget("text")
    popyt = oferta['popyt_roczny'] / 12 * wspolczynnik[round.lower()]
    app.sqlpopyt.configure(text=popyt)
    godziny = oferta['robogodziny'] * popyt
    app.sqlgodziny.configure(text=godziny)
    przychod = oferta['cena_za_usluge'] * popyt
    calyprzychod += przychod
    app.sqlprzychod.configure(text=przychod)
    cenazazasoby = 0
    for index, row in zasoby.iterrows():
        if(row['oferta_id'] == len(oferty.index)):
            cena = popyt * row['jednostka'] / row['sprzedaz'] * row['cena']
            cenazazasoby += cena
    dochod = przychod - cenazazasoby
    calydochod += dochod
    app.sqldochod.configure(text=dochod)

def menu_zasoby(*args):
    pass

def check():
    global wspolczynnikidict
    if(app.wspolczynnikitoplevel is not None and app.wspolczynnikitoplevel.winfo_exists()):
        app.wspolczynnikitoplevel.save.configure(command=save)
    if(len(wspolczynnikidict)>0 
       and len(zasoby)>0
       and app.nazwa.get() != "" 
       and app.popyt.get() != "" 
       and app.cena.get() != ""
       and app.godziny.get() != ""):
        app.dodajoferte.configure(command=add_ofert)
    else: app.dodajoferte.configure(command=None)
    if(app.zasobytoplevel is not None and app.zasobytoplevel.winfo_exists()):
        if(app.zasobytoplevel.nazwa.get() != ""):
            app.zasobytoplevel.add.configure(command=add)
        else: app.zasobytoplevel.add.configure(command=None)
    app.addkredyt.configure(command=add_kredyt)
    if(app.imie.get() != "" and app.nazwisko.get() != ""):
        app.dodajpracownika.configure(command=add_pracownicy)
    else: app.dodajpracownika.configure(command=None)
    if(app.nazwaoplaty.get() != ""):
        app.dodajoplate.configure(command=add_oplaty)
    else: app.dodajoplate.configure(command=None)
    zasobylabel = []
    for index, row in zasoby.iterrows():
        zasobylabel.append(row['nazwa'])
    app.zasoby.configure(text=zasobylabel if(len(zasobylabel)>0) else "[]")
    app.przychodcaly.configure(text=calyprzychod)
    app.dochodcaly.configure(text=calydochod)
    calykoszt = 0
    round = app.round.cget("text")
    if(len(oferty.index)>0):
        for index, row in zasoby.iterrows():
            if(row['oferta_id'] < len(oferty.index)):
                oferta = oferty.iloc[row['oferta_id']]
                wspolczynnik = wspolczynniki.iloc[oferta['wspolczynniki']]
                popyt = oferta['popyt_roczny'] / 12 * wspolczynnik[round.lower()]
                cena = popyt * row['jednostka'] / row['sprzedaz'] * row['cena']
                calykoszt +=  cena
            else: break
    app.koszt.configure(text=calykoszt)
    if(len(kredyty.index)>1):
        app.kredytyid.configure(state='normal')
        app.kredytyid.delete("0", "end")
        app.kredytyid.insert("0", len(kredyty))
        app.kredytyid.configure(state='disabled')
    calykredyt = 0
    for index, row in kredyty.iterrows():
        if(row['miesiac'] != round):
            rata = row['ilosc']*(1+row['oprocentowanie'])/row['ilosc_rat']
            howmany = miesiace.index(round) - miesiace.index(row['miesiac'])
            value = row['ilosc'] - rata*howmany
            print(value, row['ilosc'], rata*howmany)
            if(value != 0):
                value = 0
                kredyty.drop(index)
            calykredyt += value
        else:
            calykredyt += row['ilosc']
    app.kredyt.configure(text=calykredyt)
    calewynagrodzenie = 0
    for index, row in pracownicy.iterrows():
        calewynagrodzenie += row['wynagrodzenie']
    app.oplatawynagrodzenie.configure(text=calewynagrodzenie)
    caleoplatymiesieczne = 0
    caleoplatydodatkowe = 0
    for index, row in oplaty.iterrows():
        caleoplatymiesieczne += row['miesieczna']
        if(row['miesiac'] == round):
            caleoplatydodatkowe += row['oplata']
    app.oplatymiesieczne.configure(text=caleoplatymiesieczne)
    app.oplatadodatkowa.configure(text=caleoplatydodatkowe)
    app.after(1000, check)

def to_sql():
    if(len(oferty.index)>=1):
        oferty.to_sql(name='oferty', con=connection, if_exists='replace', index=False)
        wspolczynniki.to_sql(name='wspolczynniki', con=connection, if_exists='append', index=False)
        zasoby.to_sql(name='zasoby', con=connection, if_exists='replace', index=False)
        pracownicy.to_sql(name='pracownicy', con=connection, if_exists='replace', index=False)
        oplaty.to_sql(name='oplaty', con=connection, if_exists='replace', index=False)
        kredyty.to_sql(name='kredyty', con=connection, if_exists='replace', index=False)
        connection.close()

global wspolczynnikidict
global calyprzychod, calydochod, calykoszt, calykredyt, calewynagrodzenie, caleoplatymiesieczne, caleoplatydodatkowe
calyprzychod = 0
calydochod = 0
calykoszt = 0
calykredyt = 0
calewynagrodzenie = 0
caleoplatymiesieczne = 0
caleoplatydodatkowe = 0
wspolczynnikidict = {}
app.after(1000, check)
app.variable.trace_add('write', menu)
app.mainloop()
app.variable.trace_remove('write', 'menu')