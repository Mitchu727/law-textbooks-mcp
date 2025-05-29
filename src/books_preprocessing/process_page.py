import re

harder_page_content = """
312
Rozdział VI. Bezpodstawne wzbogacenie
Nb. 697–700
utracił, może żądać jej zwrotu od tego, na kogo ona bezpodstawnie przeszła 
(art. 405 KC). W tym wyraża się istotny sens bezpodstawnego wzbogacenia. 
Służy więc ono nie tylko ochronie majątku przed bezpodstawnym jego uszczu-
pleniem, ale umożliwia zarazem kontrolę poprawności wszelkich przesunięć 
majątkowych.
Bezpodstawne wzbogacenie – za wzorem współczesnych systemów praw-
nych – ukształtowane zostało w polskim prawie cywilnym jako odrębne zdarze-
nie prawne, kreujące stosunek zobowiązaniowy (por. Tytuł V Księgi III KC).
2. Regulacja nienależnego świadczenia
Natomiast wbrew tradycji wywodzącej się jeszcze z  prawa rzymskiego 
ustawodawca polski ujął w ramy jednej instytucji bezpodstawnego wzboga-
cenia także tzw.  nienależne świadczenie, poświęcając mu art.  410–413 KC. 
Zgodnie z  tą koncepcją przypadki wzbogacenia w  następstwie nienależnego 
świadczenia przedstawione zostaną jako szczególne postacie bezpodstawnego 
wzbogacenia.
II. Przesłanki
Zgodnie ze wspomnianymi założeniami instytucji bezpodstawnego wzbo-
gacenia art. 405 KC wskazuje cztery ogólne przesłanki powstania roszczenia 
z tego tytułu. Są nimi:
1) 	wzbogacenie jednego podmiotu;
2) 	zubożenie drugiego podmiotu;
3) 	związek między wzbogaceniem a zubożeniem;
4) 	bezpodstawność wzbogacenia.
1. Wzbogacenie
Polega na uzyskaniu jakiejś korzyści majątkowej w dowolnej postaci. Może 
znaleźć wyraz w nabyciu jakichś praw lub powiększeniu ich zakresu (np. przez 
przetworzenie, połączenie i  pomieszanie – art.  194 KC), na  umocnieniu ist-
niejących praw (np.  na  uzyskaniu przez wierzyciela hipotecznego wyższego 
miejsca w księdze wieczystej), na używaniu cudzych praw lub na korzystaniu 
z cudzych usług uzyskiwanych zazwyczaj odpłatnie, na zwolnieniu z długu lub 
na zniesieniu praw rzeczowych obciążających rzeczy wzbogaconego.
Korzyści te mogą więc polegać nie tylko na powiększeniu aktywów mająt-
ku, lecz także na zmniejszeniu jego pasywów lub na oszczędzeniu wydatków. 
Dominuje pogląd, że także posiadanie w dobrej wierze może być traktowane 
697
698
699
700
PAGE_END
"""

page_content = """
3
Nb. 8–11
II. Źródła prawa zobowiązań
1. Prawo stanowione
Tylko prawo powszechnie obowiązujące może regulować stosunki cywilno-
prawne, a w tym i stosunki zobowiązaniowe. Źródłami powszechnie obowiązu-
jącego prawa Rzeczypospolitej Polskiej są: Konstytucja, ustawy, ratyfikowane 
umowy międzynarodowe oraz rozporządzenia, a także akty prawa miejscowe-
go – na obszarze działania kompetentnych organów (art. 87 Konstytucji RP).
Natomiast inne akty normatywne wydawane przez upoważnione do tego 
orga-ny, a  w  szczególności zarządzenia, mają charakter wewnętrzny, tzn. że 
obowiązują tylko jednostki organizacyjne podległe organom wydającym te akty 
(art. 93 Konstytucji RP). Nie mogą więc mieć waloru źródeł prawa cywilnego.
a) Wśród ustaw największą doniosłość ma Kodeks cywilny z 1964 r., rady-
kalnie zmodyfikowany, zwłaszcza nowelami wydawanymi od 1990  r. Prawu 
zobowiązań jest tam poświęcona Księga III – zresztą najobszerniejsza, obejmu-
jąca ponad połowę wszystkich przepisów KC (art. 353–92116).
Prawo zobowiązań zostało najwcześniej zunifikowane spośród wszystkich działów prawa 
cywilnego. Dokonano tego, wydając w 1933 r. Kodeks zobowiązań oraz rok później Kodeks 
handlowy, przy czym obie kodyfikacje weszły w życie 1.7.1934 r., a przestały obowiązywać 
dopiero 31.12.1964 r., poza pewnymi partiami Kodeksu handlowego, które zachowały moc 
obowiązującą także pod rządem Kodeksu cywilnego (por. art. VI PWKC) – do 1.1.2001 r., 
kiedy to wszedł w życie Kodeks spółek handlowych.
Kodyfikacje te, a zwłaszcza Kodeks zobowiązań, wywarły ogromny wpływ na rozwój 
polskiej nauki prawa cywilnego, a także na treść obowiązującego Kodeksu cywilnego.
Poza regulacją podstawowych instytucji prawa zobowiązań zamieszczoną w Kodeksie 
cywilnym, stosunki prawne tego typu normuje wiele ustaw szczególnych wobec Kodeksu, 
które uzupełniają, a dla pewnych obszarów także modyfikują postanowienia kodeksowe.
Por. zwłaszcza ustawy: Prawo własności przemysłowej, o prawie autorskim i prawach 
pokrewnych, Prawo przewozowe, Kodeks morski, o działalności ubezpieczeniowej i rease-
kuracyjnej, o ochronie praw lokatorów, Prawo zamówień publicznych, Prawo bankowe, Pra-
wo wekslowe, Prawo czekowe, o obrocie instrumentami finansowymi, o ofercie publicznej.
b) Także rozporządzenia są częstym środkiem regulowania stosunków 
zobowiązaniowych.
Jednakże ich rola ulega istotnemu ograniczeniu w świetle Konstytucji RP. 
Rozporządzenia mogą bowiem wydać obecnie jedynie organy wskazane 
w Konstytucji RP, i to na podstawie szczegółowego upoważnienia zawartego 
w ustawie i w celu jej wykonania – przy czym norma upoważniająca do wyda-
nia rozporządzenia powinna nie tylko określać kompetentny organ i  zakres 
8
9
10
11
§ 1. Źródła i miejsce prawa zobowiązań w polskim systemie prawnym
PAGE_END
"""


def parse_odd_page(page_content):
    page_content = re.sub("[0-9]+\nNb\..*\n","", page_content)
    page_content = re.sub("Nb\..*\n(Rozdział.*)","\1", page_content)
    page_content = re.sub("§.*\nPAGE_END", "PAGE_END", page_content)
    paragraph_ids = re.search("([0-9]+\n)*PAGE_END", page_content).group()
    paragraph_ids = paragraph_ids.replace("\nPAGE_END", "").split("\n")
    page_content = re.sub("([0-9]+\n)*PAGE_END", "", page_content)
    return page_content, paragraph_ids

def parse_even_page(page_content):
    page_content = re.sub("[0-9]+\n.*\nNb\..*\n", "", page_content)
    paragraph_ids = re.search("([0-9]+\n)*PAGE_END", page_content).group()
    paragraph_ids = paragraph_ids.replace("\nPAGE_END", "").split("\n")
    page_content = re.sub("([0-9]+\n)*PAGE_END", "", page_content)
    return page_content, paragraph_ids



if __name__ == "__main__":
    # parse_odd_page(page_content)
    parse_even_page(harder_page_content)