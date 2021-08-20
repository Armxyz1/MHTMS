bseat=['B7','H8','E4']
def seat(x,y):
    #defines a seat in a row
    a="||"
    if x+str(y) in bseat:
        a="#"
    return a
def row(r):
    #defines a row in a cinema hall
    row=[r]
    for i in range(1,10):
        row+=[seat(r,i)]
    return row
def hall():
    #defines the cinema hall
    text=""
    text+="_"*48+"\n"+"SCREEN THIS WAY"+"\n"+"_"*48+"\n"*2
    sp=" "
    text+="*"
    text+=sp*6
    for i in range(1,10):
        text+=str(i)
        if i==2:
            text+=sp*10
        elif i==7:
            text+=sp*9
        else:
            text+=sp*5
    text+="\n"
    s="ABCDEFGH"
    for j in range(8):
        for k in range(10):
            text+=row(s[j])[k]
            if k==2 or k==7:
                text+=sp*9
            else:
                text+=sp*5
        text+="\n"
    text+="||:- Empty seat"+"\n"
    text+="#:- Occupied seat"
    return text

#_MAIN_
import PySimpleGUI as pgs
x=hall()
pgs.theme('Material2')
lt=[[pgs.Text("Enter seat name:-",font="Cambria")],[pgs.Text(x,font="Cambria")],[pgs.InputText()],[pgs.Button("CONFIRM", font="Cambria")]]
win=pgs.Window("HALL VIEW",lt)
while True:
    event,values=win.read()
    if event=="CONFIRM" or pgs.WIN_CLOSED:
        break
win.close()
lst=values[0].split()
bseat.extend(lst)
x=hall()
lt=[[pgs.Text(x,font="Cambria")],[pgs.Button("OK",font="Cambria")]]
win=pgs.Window("HALL VIEW",lt)
while True:
    event,values=win.read()
    if event=="OK" or pgs.WIN_CLOSED:
        break
win.close()
dispwinlayt=[[pgs.Text('BOOKED!',font="Cambria")],[pgs.Button("OK")]]
dispwin=pgs.Window("Booked",dispwinlayt)
evdisp,valdisp=dispwin.read()
if evdisp=="OK" or evdisp==pgs.WIN_CLOSED:
    dispwin.close()
