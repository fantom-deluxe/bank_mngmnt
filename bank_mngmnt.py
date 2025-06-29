
#Bank Management Sytem
import mysql.connector as msql
connect = msql.connect(host='localhost',user='root',password='mysql') #change password if needed
c = connect.cursor()
c.execute('create database if not exists bank')
c.execute('use bank')
c.execute('create table if not exists cus(acno int(12) primary key,name varchar(30),address varchar(20),mobile BIGINT(12),balance BIGINT(7))')
c.execute('create table if not exists banktrans(acno int(12),ttype varchar(2),amt int(7))')
#already exists some account in database
c.execute('delete from cus')
c.execute("insert into cus values('1266552','Customer1','Kolkata',8448798761,10000)")
c.execute("insert into cus values('1267583','Customer2','Delhi',9856921420,25500)")
connect.commit()

#GUI
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Bank Management System")
Label(window,text="Bank Management System",font='Bahnschrift 30  bold',fg="light blue",bg="blue",justify="center").grid(row=0,columnspan=5)
Label(window,text="Account No. :",bg='white',fg='black',font='none 10') .grid(row=2,column=0, padx=40, pady=5)
Label(window,text="Account Holder's Name :",bg='white',fg='black',font='none 10') .grid(row=3,column=0, padx=40, pady=5)
Label(window,text="Address :",bg='white',fg='black',font='none 10') .grid(row=4,column=0, padx=40, pady=5)
Label(window,text="Mobile No. :",bg='white',fg='black',font='none 10') .grid(row=5,column=0, padx=40, pady=5)
Label(window,text="Amount(Only to Withdraw/Deposit) :",bg='white',fg='black',font='none 10') .grid(row=6,column=0, padx=40, pady=5)


#entry box
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
e1=Entry(window,textvariable=v1).grid(row=2,column=1)
e2=Entry(window,textvariable=v2).grid(row=3,column=1)
e3=Entry(window,textvariable=v3).grid(row=4,column=1)
e4=Entry(window,textvariable=v4).grid(row=5,column=1)
e5=Entry(window,textvariable=v5).grid(row=6,column=1)


def clear():
    v1.set('')
    v2.set('')
    v3.set('')
    v4.set('')
    v5.set('')


#create account
def add():
    balance=0
    c.execute("insert into cus values(%s,%s,%s,%s,%s)",(v1.get(),v2.get(),v3.get(),v4.get(),balance))
    connect.commit()
    print("Account Created Succesfully")
    print('')
    print('................................................................')
    messagebox.showinfo("Success", "Account Created Successfully")


#delete account
def remove():
    c.execute("delete from cus where (acno=%s and name=%s)",(v1.get(),v2.get()))
    connect.commit()
    print('Account Removed successfully!')
    print('')
    print('................................................................')
    messagebox.showinfo("Success", "Account Deleted Successfully")


#display Acc. details
def display():
    c.execute("select * from cus where (acno=%s and name=%s)",(v1.get(),v2.get()))
    data=c.fetchone()
    print('Account is available')
    print('Account Number:',data[0])
    print("Account Holder's Name:",data[1])
    print('Address:',data[2])
    print('Mobile Number',data[3])
    print('Account Balance:',data[4])
    print('')
    print('................................................................')


#Withdraw or Deposit Money
      
def deposit():
    ttype="d"
    c.execute("insert into banktrans values(%s,%s,%s)",(v1.get(),ttype,v5.get()))
    c.execute("update cus set balance=balance+ %s where acno= %s",(v5.get(),v1.get()))
    connect.commit()
    print('Money Deposited')
    print('................................................................')
    messagebox.showinfo("Success", "Money Deposited Successfully")


def withdraw():
    ttype="w"
    c.execute("insert into banktrans values(%s,%s,%s)",(v1.get(),ttype,int(v5.get())))
    c.execute("update cus set balance=balance- %s where acno= %s",(int(v5.get()),v1.get()))
    connect.commit()
    print('Money Withdrawed')
    print('................................................................')
    messagebox.showinfo("Success", "Money Withdrawed Successfully")


def exit():
    window.destroy()

import csv 

def trans():
    c.execute("select * from banktrans")
    data=c.fetchall()
    op=open('Transactions.csv','w',newline='')
    wobj=csv.writer(op)
    wobj.writerow(['AccountNo.','TransactionType','Amount'])
    wobj.writerows(data)
    
    

#buttons
Button(window,text='Create Account',command=add,width=20).grid(row=7,column=0,padx=20, pady=10)
Button(window,text='Delete Account',command=remove,width=20).grid(row=7,column=1,padx=20, pady=10)
Button(window,text='Show Details',command=display,width=20).grid(row=7,column=2,padx=20, pady=10)
Button(window,text='Deposit',command=deposit,width=20).grid(row=8,column=0,padx=20, pady=10)
Button(window,text='Withdraw',command=withdraw,width=20).grid(row=8,column=1,padx=20, pady=10)
Button(window,text='Clear',command=clear,width=20).grid(row=8,column=2,padx=20, pady=10)
Button(window,text='Close',command=exit,width=20).grid(row=9,column=2,padx=20, pady=10)
Button(window,text='Generate CSV',command=trans,width=20).grid(row=9,column=0,padx=20, pady=10)

window.mainloop()    

