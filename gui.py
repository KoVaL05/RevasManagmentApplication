import tkinter as tk
import tkinter.ttk as ttk

class Zasoby(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x130")
        self.title("Zasoby")
        self.resizable(False, False)
        self.variable = tk.StringVar()
        self.zasobylist = []
        self.zasoby = ttk.Combobox(self, textvariable=self.variable, width=20)
        self.zasoby['values'] = self.zasobylist
        self.zasoby['state'] = 'readonly'
        self.zasoby.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
        self.nazwalabel = ttk.Label(self, text="Nazwa")
        self.nazwalabel.grid(row=1, column=0, padx=10, pady=5)
        self.nazwa = ttk.Entry(self)
        self.nazwa.grid(row=2, column=0, padx=10, pady=5)
        self.jakosclabel = ttk.Label(self, text="Jakość")
        self.jakosclabel.grid(row=1, column=1, padx=10, pady=5)
        self.selected_value = tk.IntVar()
        self.selected_value.set(1)
        self.jakosc = ttk.Scale(self, from_=1, to=3, orient='horizontal', command=self.change_scale, variable=self.selected_value)
        self.jakosc.grid(row=2, column=1, padx=10, pady=5)
        self.cenalabel = ttk.Label(self, text="Cena za jednostke")
        self.cenalabel.grid(row=1, column=2, padx=10, pady=5)
        self.cena = ttk.Spinbox(self, from_=0, to=999999, width=10)
        self.cena.grid(row=2, column=2, padx=10, pady=5)
        self.save = ttk.Button(self, text="Zapisz",width=40)
        self.save.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
    
    def change_scale(self, value):
        if(float(value)>1):
            self.selected_value.set(1)
        if(float(value)>2):
            self.selected_value.set(3)
        if(float(value)<3):
            self.selected_value.set(2)
        if(float(value)<2):
            self.selected_value.set(1)

class WspolczynnikiLevel(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("200x410")
        self.title("Współczynniki")
        self.resizable(False, False)
        self.styczenlabel = ttk.Label(self, text="Styczeń:")
        self.styczenlabel.grid(row=0, column=0, padx=20, pady=5)
        self.styczen = ttk.Entry(self, width=10)
        self.styczen.grid(row=0, column=1, padx=(0, 20), pady=5)
        self.lutylabel = ttk.Label(self, text="Luty:")
        self.lutylabel.grid(row=1, column=0, padx=20, pady=5)
        self.luty = ttk.Entry(self, width=10)
        self.luty.grid(row=1, column=1, padx=(0, 20), pady=5)
        self.marzeclabel = ttk.Label(self, text="Marzec:")
        self.marzeclabel.grid(row=2, column=0, padx=20, pady=5)
        self.marzec = ttk.Entry(self, width=10)
        self.marzec.grid(row=2, column=1, padx=(0, 20), pady=5)
        self.kwiecienlabel = ttk.Label(self, text="Kwiecień:")
        self.kwiecienlabel.grid(row=3, column=0, padx=20, pady=5)
        self.kwiecien = ttk.Entry(self, width=10)
        self.kwiecien.grid(row=3, column=1, padx=(0, 20), pady=5)
        self.majlabel = ttk.Label(self, text="Maj:")
        self.majlabel.grid(row=4, column=0, padx=20, pady=5)
        self.maj = ttk.Entry(self, width=10)
        self.maj.grid(row=4, column=1, padx=(0, 20), pady=5)
        self.czerwieclabel = ttk.Label(self, text="Czerwiec:")
        self.czerwieclabel.grid(row=5, column=0, padx=20, pady=5)
        self.czerwiec = ttk.Entry(self, width=10)
        self.czerwiec.grid(row=5, column=1, padx=(0, 20), pady=5)
        self.lipieclabel = ttk.Label(self, text="Lipiec:")
        self.lipieclabel.grid(row=6, column=0, padx=20, pady=5)
        self.lipiec = ttk.Entry(self, width=10)
        self.lipiec.grid(row=6, column=1, padx=(0, 20), pady=5)
        self.sierpienlabel = ttk.Label(self, text="Sierpień:")
        self.sierpienlabel.grid(row=7, column=0, padx=20, pady=5)
        self.sierpien = ttk.Entry(self, width=10)
        self.sierpien.grid(row=7, column=1, padx=(0, 20), pady=5)
        self.wrzesienlabel = ttk.Label(self, text="Wrzesień:")
        self.wrzesienlabel.grid(row=8, column=0, padx=20, pady=5)
        self.wrzesien = ttk.Entry(self, width=10)
        self.wrzesien.grid(row=8, column=1, padx=(0, 20), pady=5)
        self.pazdzierniklabel = ttk.Label(self, text="Październik:")
        self.pazdzierniklabel.grid(row=9, column=0, padx=20, pady=5)
        self.pazdziernik = ttk.Entry(self, width=10)
        self.pazdziernik.grid(row=9, column=1, padx=(0, 20), pady=5)
        self.listopadlabel = ttk.Label(self, text="Listopad:")
        self.listopadlabel.grid(row=10, column=0, padx=20, pady=5)
        self.listopad = ttk.Entry(self, width=10)
        self.listopad.grid(row=10, column=1, padx=(0, 20), pady=5)
        self.grudzienlabel = ttk.Label(self, text="Grudzień:")
        self.grudzienlabel.grid(row=11, column=0, padx=20, pady=5)
        self.grudzien = ttk.Entry(self, width=10)
        self.grudzien.grid(row=11, column=1, padx=(0, 20), pady=5)
        self.save = ttk.Button(self, text="Zapisz", width=20)
        self.save.grid(row=12, column=0, columnspan=2, padx=20, pady=5)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x325")
        self.title("RevasManager")
        self.frameconfig = ttk.LabelFrame(self, text="Konfiguruj", width=725, height=50)
        self.frameconfig.grid(row=0, column=0, padx=(10, 2), pady=10)
        self.roundframe = ttk.LabelFrame(self, text="Runda", width=140, height=95)
        self.roundframe.grid(row=0, column=1, padx=(5, 10))
        self.round = ttk.Label(self.roundframe, text="Maj")
        self.round.place(relx=0.5, rely=0.5, anchor='center')
        self.options = ttk.Notebook(self.frameconfig, width=725, height=50)
        self.oferty = ttk.Frame(self.options)
        self.pracownicy = ttk.Frame(self.options)
        self.oplaty = ttk.Frame(self.options)
        self.options.add(self.oferty, text="Oferty")
        self.options.add(self.pracownicy, text="Pracownicy")
        self.options.add(self.oplaty, text="Opłaty")
        self.options.pack(expand=1, fill='both')
        #Oferty
        self.nazwalabel = ttk.Label(self.oferty, text="Nazwa")
        self.nazwalabel.grid(row=0, column=0, padx=10)
        self.nazwa = ttk.Entry(self.oferty)
        self.nazwa.grid(row=1, column=0, padx=10, pady=5)
        self.poptylabel = ttk.Label(self.oferty, text="Popyt roczny")
        self.poptylabel.grid(row=0, column=1, padx=10)
        self.popyt = ttk.Entry(self.oferty, width=10)
        self.popyt.grid(row=1, column=1, padx=10, pady=5)
        self.cenalabel = ttk.Label(self.oferty, text="Cena za usługę")
        self.cenalabel.grid(row=0, column=2, padx=10)
        self.cena = ttk.Entry(self.oferty, width=10)
        self.cena.grid(row=1, column=2, padx=10, pady=5)
        self.godzinylabel = ttk.Label(self.oferty, text="Godziny")
        self.godzinylabel.grid(row=0, column=3, padx=10)
        self.godziny = ttk.Entry(self.oferty, width=10)
        self.godziny.grid(row=1, column=3, padx=10, pady=5)
        self.wspolczynniklabel = ttk.Label(self.oferty, text="Współczynniki")
        self.wspolczynniklabel.grid(row=0, column=4, padx=10)
        self.wspolczynnik = ttk.Button(self.oferty, text="Otwórz Menu", command=self.open_wspolczynniki)
        self.wspolczynnik.grid(row=1, column=4, padx=10, pady=5)
        self.dodajzasobylabel = ttk.Label(self.oferty, text="Zasoby")
        self.dodajzasobylabel.grid(row=0, column=5, padx=10)
        self.dodajzasoby = ttk.Button(self.oferty, text="Otwórz Menu")
        self.dodajzasoby.grid(row=1, column=5, padx=10, pady=5)
        self.dodajoferte = ttk.Button(self.oferty, text="Dodaj oferte")
        self.dodajoferte.grid(row=0, rowspan=2, column=6, padx=10, pady=10)
        #Pracownicy
        self.imielable = ttk.Label(self.pracownicy, text="Imie")
        self.imielable.grid(row=0, column=0, padx=15)
        self.imie = ttk.Entry(self.pracownicy)
        self.imie.grid(row=1, column=0, padx=15, pady=5)
        self.nazwiskolabel = ttk.Label(self.pracownicy, text="Nazwisko")
        self.nazwiskolabel.grid(row=0, column=1, padx=15)
        self.nazwisko = ttk.Entry(self.pracownicy)
        self.nazwisko.grid(row=1, column=1, padx=15, pady=5)
        self.wynagrodzenielabel = ttk.Label(self.pracownicy, text="Wynagrodzenie")
        self.wynagrodzenielabel.grid(row=0, column=2, padx=15)
        self.wynagrodzenie = ttk.Entry(self.pracownicy, width=15)
        self.wynagrodzenie.grid(row=1, column=2, padx=15, pady=5)
        self.dodajpracownika = ttk.Button(self.pracownicy, text="Dodaj pracownika", width=20)
        self.dodajpracownika.grid(row=0, rowspan=2, column=3, padx=15, pady=10)
        #Oplaty
        self.nazwaoplatylabel = ttk.Label(self.oplaty, text="Nazwa")
        self.nazwaoplatylabel.grid(row=0, column=0, padx=15)
        self.nazwaoplaty = ttk.Entry(self.oplaty)
        self.nazwaoplaty.grid(row=1, column=0, padx=15, pady=5)
        self.oplatalabel = ttk.Label(self.oplaty, text="Opłata jednorazowa")
        self.oplatalabel.grid(row=0, column=1, padx=15)
        self.oplata = ttk.Entry(self.oplaty)
        self.oplata.grid(row=1, column=1, padx=15, pady=5)
        self.oplatamiesiecznalabel = ttk.Label(self.oplaty, text="Opłata miesięczna")
        self.oplatamiesiecznalabel.grid(row=0, column=2, padx=15)
        self.oplatamiesieczna = ttk.Entry(self.oplaty, width=15)
        self.oplatamiesieczna.grid(row=1, column=2, padx=15, pady=5)
        self.dodajoplate = ttk.Button(self.oplaty, text="Dodaj opłate", width=20)
        self.dodajoplate.grid(row=0, rowspan=2, column=3, padx=15, pady=10)
        #------------------------------------------------------------------
        self.revas = ttk.LabelFrame(self, text="Revas", width=880, height=200)
        self.revas.grid(row=1, column=0, columnspan=2, padx=10)
        self.revas.grid_propagate(False)
        self.revasoferta = ttk.LabelFrame(self.revas, text="Oferty", width=300, height=180)
        self.revasoferta.grid(row=0, rowspan=3, column=0, padx=5)
        self.revasoferta.grid_propagate(False)
        self.variable = tk.StringVar()
        self.optionslist = []
        self.oferta = ttk.Combobox(self.revasoferta, textvariable=self.variable, width=10)
        self.oferta['values'] = self.optionslist
        self.oferta['state'] = 'readonly'
        self.oferta.grid(row=0, column=0, padx=10, pady=10)
        self.nazwaoferty = ttk.Label(self.revasoferta, text="Nazwa", width=30, anchor="center")
        self.nazwaoferty.grid(row=0, column=1, padx=(0,10))
        self.iloscpopyt = ttk.Label(self.revasoferta, text="Popyt:")
        self.iloscpopyt.grid(row=1, column=0, padx=(0,10), pady=5)
        self.sqlpopyt = ttk.Label(self.revasoferta, text="SQLPopyt", width=30, anchor="center")
        self.sqlpopyt.grid(row=1, column=1, padx=(0,10), pady=5)
        self.iloscgodzin = ttk.Label(self.revasoferta, text="Godziny:")
        self.iloscgodzin.grid(row=2, column=0, padx=(0,10), pady=5)
        self.sqlgodziny = ttk.Label(self.revasoferta, text="SQLGodziny", width=30, anchor="center")
        self.sqlgodziny.grid(row=2, column=1, padx=(0,10), pady=5)
        self.przychod = ttk.Label(self.revasoferta, text="Przychód:")
        self.przychod.grid(row=3, column=0, padx=(0,10), pady=5)
        self.sqlprzychod = ttk.Label(self.revasoferta, text="SQLPrzychod", width=30, anchor="center")
        self.sqlprzychod.grid(row=3, column=1, padx=(0,10), pady=5)
        self.dochod = ttk.Label(self.revasoferta, text="Dochód:")
        self.dochod.grid(row=4, column=0, padx=(0,10), pady=5)
        self.sqldochod = ttk.Label(self.revasoferta, text="SQLDochod", width=30, anchor="center")
        self.sqldochod.grid(row=4, column=1, padx=(0,10), pady=5)
        #--------------------------------------------------------
        self.oplatymiesiecznelabel = ttk.Label(self.revas, text="Opłaty miesięczne:")
        self.oplatymiesiecznelabel.grid(row=0, column=1, padx=(30, 10), pady=5)
        self.oplatymiesieczne = ttk.Label(self.revas, text="999999")
        self.oplatymiesieczne.grid(row=0, column=2, padx=10, pady=5)
        self.oplatadodatkowalabel = ttk.Label(self.revas, text="Opłata w tym miesiącu:")
        self.oplatadodatkowalabel.grid(row=1, column=1, padx=(30, 10), pady=5)
        self.oplatadodatkowa = ttk.Label(self.revas, text="999999")
        self.oplatadodatkowa.grid(row=1, column=2, padx=10, pady=5)
        self.oplatawynagrodzenielabel = ttk.Label(self.revas, text="Opłata za pracowników:")
        self.oplatawynagrodzenielabel.grid(row=2, column=1, padx=(30, 10), pady=5)
        self.oplatawynagrodzenie = ttk.Label(self.revas, text="999999")
        self.oplatawynagrodzenie.grid(row=2, column=2, padx=10, pady=5)
        self.zasobylabel = ttk.Label(self.revas, text="Zasoby:")
        self.zasobylabel.grid(row=0, column=3, padx=10, pady=5)
        self.zasoby = ttk.Label(self.revas, text="[]")
        self.zasoby.grid(row=0, column=4, columnspan=3, padx=10, pady=5)
        self.kosztzasobow = ttk.Label(self.revas, text="Koszt:")
        self.kosztzasobow.grid(row=1, column=3, padx=10, pady=5)
        self.koszt = ttk.Label(self.revas, text="999999")
        self.koszt.grid(row=1, column=4, padx=10, pady=5)
        self.przychodcalylabel = ttk.Label(self.revas, text="Przychód:")
        self.przychodcalylabel.grid(row=2, column=3, padx=10, pady=5)
        self.przychodcaly = ttk.Label(self.revas, text="999999")
        self.przychodcaly.grid(row=2, column=4, padx=10, pady=5)
        self.kredytlabel = ttk.Label(self.revas, text="Pozostały kredyt:")
        self.kredytlabel.grid(row=1, column=5, padx=10, pady=5)
        self.kredyt = ttk.Label(self.revas, text="999999")
        self.kredyt.grid(row=1, column=6, padx=10, pady=5)
        self.dochodcalylabel = ttk.Label(self.revas, text="Dochód:")
        self.dochodcalylabel.grid(row=2, column=5, padx=10, pady=5)
        self.dochodcaly = ttk.Label(self.revas, text="999999")
        self.dochodcaly.grid(row=2, column=6, padx=10, pady=5)
        self.wspolczynnikitoplevel = None
        self.zasobytoplevel = None
        self.open_zasoby()

    def open_wspolczynniki(self):
        if(self.wspolczynnikitoplevel is None or not self.wspolczynnikitoplevel.winfo_exists()):
            self.wspolczynnikitoplevel = WspolczynnikiLevel()
            self.wspolczynnikitoplevel.attributes('-topmost', 'true')
        else:
            self.wspolczynnikitoplevel.focus()

    def open_zasoby(self):
        if(self.zasobytoplevel is None or not self.zasobytoplevel.winfo_exists()):
            self.zasobytoplevel = Zasoby()
            self.zasobytoplevel.attributes('-topmost', 'true')
        else:
            self.zasobytoplevel.focus()
