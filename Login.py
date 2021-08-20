import PySimpleGUI as pgs
import mysql.connector
mycon=mysql.connector.connect(host='localhost', user='root', passwd='boss', database='MHTMS')
mycs=mycon.cursor()
pgs.theme('Material2')
sess_id=sess_pass=None
def signin():
            global sess_id, sess_pass
            sgin=[[pgs.Text("Enter username",font="Cambria")],[pgs.InputText()],
             [pgs.Text("Enter password",font="Cambria")],[pgs.InputText()],[pgs.Button("SignIn",font="Cambria")]]
            sginwin=pgs.Window("SignIn",sgin)
            evesgin,idpas_in=sginwin.read()
            if evesgin=="SignIn":
                quer="select * from customers"
                mycs.execute(quer)
                data=mycs.fetchall()
                cuslist=[]
                for x in data:
                    cuslist.append(x[1])
                if idpas_in[0] in cuslist:
                    sess_id=idpas_in[0]
                    sess_pass=idpas_in[1]
                    sginwin.close()
                    dispwinlayt=[[pgs.Text('Succesfully signed in',font="Cambria")],[pgs.Button("OK")]]
                    dispwin=pgs.Window("SIGNED IN",dispwinlayt)
                    evdisp,valdisp=dispwin.read()
                    if evdisp=="OK" or evdisp==pgs.WIN_CLOSED:
                        dispwin.close()
                else:
                    print("Invalid Login")
def signup():
            sgup=[[pgs.Text("Enter Full Name",font="Cambria")],[pgs.InputText()],
            [pgs.Text("Enter username",font="Cambria")],[pgs.InputText()],
            [pgs.Text("Enter DOB(YYYY-MM-DD)",font="Cambria")],[pgs.InputText()],
            [pgs.Text("Enter password",font="Cambria")],[pgs.InputText()],[pgs.Button("SignUp",font="Cambria")]]
            sgupwin=pgs.Window("SignUp",sgup)
            evesgup,idpas_up=sgupwin.read()
            if evesgup=="SignUp":
                quer="select * from customers"
                mycs.execute(quer)
                data=mycs.fetchall()
                cuslist=[]
                for x in data:
                    cuslist.append(x[1])
                if idpas_up[1] in cuslist:
                    print("Username already taken, choose another")
                else:                    
                    quer="create table if not exists "+idpas_up[1]+" (mov_bkd varchar(20), no_seats int(2), date date, timing time);"
                    mycs.execute(quer)
                    quer="insert into customers values ('{}','{}','{}','{}')".format(idpas_up[0],idpas_up[1],idpas_up[3],idpas_up[2])
                    mycs.execute(quer)
                    mycon.commit()
                    sgupwin.close()
                    dispwinlayt=[[pgs.Text('ACCOUNT CREATED, Please sign in',font="Cambria")],[pgs.Button("OK")]]
                    dispwin=pgs.Window("Account created",dispwinlayt)
                    evdisp,valdisp=dispwin.read()
                    if evdisp=="OK" or evdisp==pgs.WIN_CLOSED:
                        dispwin.close()
                    mainpg()
def mainpg():
    loglayout=[[pgs.Text("------------------------WELCOME!----------------------------",font="Cambria")],
               [pgs.Button("SignIn",font="Cambria")],[pgs.Button("SignUp",font="Cambria")]]
    logwin=pgs.Window("WELCOME",loglayout)
    while True:
        event,logvalues=logwin.read()
        logwin.close()
        if event=="SignUp":
            signup()
        elif event=="SignIn":
            signin()
        elif event==pgs.WIN_CLOSED:
            break
mainpg()
print(sess_id,sess_pass)

