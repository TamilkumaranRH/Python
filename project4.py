from tkinter import *
from tkinter import ttk, font, messagebox
root=Tk()
root.geometry("800x600")
root.config(bg="white")

label_font=font.Font(weight="bold",family="Times New Roman",size=50)
x=Label(root,text="LIVE",font=label_font,bg="white")
x.config(fg="red")
x.place(relx=0.60,rely=0.01)
label_font=font.Font(weight="bold",family="Times New Roman",size=50)
x=Label(root,text="WIRE",font=label_font,bg="white")
x.config(fg="blue")
x.place(relx=0.73,rely=0.01)
s="FOR LIVE CAREERS"
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
l=Label(root,text=s,font=label_font,bg="white")
l.place(relx=0.64,rely=0.12)

label_font=font.Font(weight="bold",family="Times New Roman",size=20)
x=Label(root,text="Customer Data Sheet",font=label_font)
x.config(bg="blue",fg="white")
x.place(relx=0.01,rely=0.02)

""" frame=Frame(root,width=700,height=350,bg="yellow")
frame.pack()
frame.place(relx=0.3,rely=0.3) """
label_font=font.Font(weight="bold",family="Times New Roman",size=15)
x=Label(root,text="Personal Data",font=label_font,bg="white")
x.config(fg="black")
x.place(x=350,y=200)


label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l2=Label(root,text="Name(BLOCK LETTERS):Mr./Mrs./Ms.",font=label_font,bg="white")
l2.place(x=10,y=300)
e1=Entry(root,font=label_font)
e1.place(x=250,y=300)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l3=Label(root,text="Date of Birth:",font=label_font,bg="white")
l3.place(x=10,y=350)
e2=Entry(root,font=label_font)
e2.place(x=250,y=350)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l4=Label(root,text="Qualification:",font=label_font,bg="white")
l4.place(x=10,y=400)
e3=Entry(root,font=label_font)
e3.place(x=250,y=400)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l5=Label(root,text="Premanent Address(BLOCK LETTERS):",font=label_font,bg="white")
l5.place(x=10,y=450)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
text2 = Text(root,height=5, width=25,font=label_font)
text2.place(x=250,y=450)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l6=Label(root,text="Mobile:",font=label_font,bg="white")
l6.place(x=10,y=550)
e4=Entry(root,font=label_font)
e4.place(x=250,y=550)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l7=Label(root,text="E-mail:",font=label_font,bg="white")
l7.place(x=10,y=600)
e5=Entry(root,font=label_font)
e5.place(x=250,y=600)

s="""I here authorize LIVEWIRE and its staff to call/ SMS / Email on my contacts provided 
to discuss further about the courses in future."""
label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l=Label(root,text=s,font=label_font)
l.place(x=10,y=650)

label_font=font.Font(weight="bold",family="Times New Roman",size=15)
x=Label(root,text="To be filled by the Customer Service Executive",font=label_font,bg="white")
x.config(bg="blue",fg="white")
x.place(x=700,y=200)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l=Label(root,text="How did the customer come to know about LIVEWIRE?",font=label_font,bg="white")
l.place(x=600,y=250)
combobox = ttk.Combobox(root, values=["Newspaper Advertisement", "Cinema Theatre Slide/ Cable TV", "Friend or Relative",
                                      "Mailer","Article/Write-up in Newspaper/Magazine","Demo at college","Tele-Call","Handbill",
                                      "LIVEWIRE Staff/Students","LIVEWIRE Website","Banner or Signboard","Others"],font=label_font)
combobox.place(x=1000, y=250)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l=Label(root,text="Present Details of the Customer:",font=label_font,bg="white")
l.place(x=600,y=300)

var=IntVar()
r1=Checkbutton(root,text="Student:",bg="white")
r1.place(x=600,y=320)
l=Label(root,text="Year/Branch:",font=label_font,bg="white")
l.place(x=750,y=320)
e6=Entry(root,font=label_font)
e6.place(x=890,y=320)
l=Label(root,text="College Name:",font=label_font,bg="white")
l.place(x=1050,y=320)
e7=Entry(root,font=label_font)
e7.place(x=1150,y=320)

r2=Checkbutton(root,text="Searching for a job:",bg="white")
r2.place(x=600,y=340)
l=Label(root,text="Degree/Diploma/Plus2:",font=label_font,bg="white")
l.place(x=750,y=340)
e8=Entry(root,font=label_font)
e8.place(x=890,y=340)
l=Label(root,text="Branch:",font=label_font,bg="white")
l.place(x=1050,y=340)
e9=Entry(root,font=label_font)
e9.place(x=1150,y=340)

r3=Checkbutton(root,text="Employed:",bg="white")
r3.place(x=600,y=360)
l=Label(root,text="Designation & Company:",font=label_font,bg="white")
l.place(x=750,y=360)
e10=Entry(root,font=label_font)
e10.place(x=890,y=360)

r4=Checkbutton(root,text="Self-Employed:",bg="white")
r4.place(x=600,y=380)
e11=Entry(root,font=label_font)
e11.place(x=750,y=380)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
l=Label(root,text="Interested in:",font=label_font,bg="white")
l.place(x=600,y=420)

var=IntVar()
r1=Radiobutton(root,text="IT Infrasturucture Management",variable=var,value=1,bg="white")
r1.place(x=700,y=420)
r2=Radiobutton(root,text="Industrial Automation",variable=var,value=2,bg="white")
r2.place(x=700,y=440)
r3=Radiobutton(root,text="Special Programs",variable=var,value=3,bg="white")
r3.place(x=700,y=460)
r4=Radiobutton(root,text="Electronic Design Automation",variable=var,value=4,bg="white")
r4.place(x=900,y=420)
r5=Radiobutton(root,text="Software Development",variable=var,value=5,bg="white")
r5.place(x=900,y=440)
r6=Radiobutton(root,text="Data Science",variable=var,value=6,bg="white")
r6.place(x=900,y=460)

label_font=font.Font(weight="bold",family="Times New Roman",size=25)
x=Label(root,text="Thank You!",font=label_font,bg="white")
x.place(x=900,y=600)

label_font=font.Font(weight="bold",family="Times New Roman",size=12)
b1=Button(root,text="Submit",font=label_font,bg="lime")
b1.place(x=700,y=550)

label_font=font.Font(weight="bold",family="Times New Roman",size=12)
b1=Button(root,text="Fee Details",command=lambda:next(root),font=label_font,bg="brown",fg="white")
b1.place(x=1120,y=650)


#fee details
def next(root):
    root.destroy()
    root=Tk()
    root.title("fee details")
    root.geometry("600x400")
    frame=Frame(root,width=800,height=660,bg="skyblue")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="Fee Details",font=label_font,bg="skyblue")
    x.place(x=350,y=10)

    label_font=font.Font(weight="bold",family="Times New Roman",size=15)
    l1=Label(frame,text="Date:",font=label_font,bg="skyblue")
    l1.place(x=500,y=40)
    e1=Entry(frame,font=label_font)
    e1.place(x=570,y=40)

    l2=Label(frame,text="Admission No:",font=label_font,bg="skyblue")
    l2.place(x=200,y=90)
    e2=Entry(frame,font=label_font)
    e2.place(x=350,y=90)

    l3=Label(frame,text="Name:",font=label_font,bg="skyblue")
    l3.place(x=200,y=150)
    e3=Entry(frame,font=label_font)
    e3.place(x=350,y=150)

    l4=Label(frame,text="Course:",font=label_font,bg="skyblue")
    l4.place(x=200,y=200)
    e4=Entry(frame,font=label_font)
    e4.place(x=350,y=200)

    l5=Label(frame,text="Admission Fee:",font=label_font,bg="skyblue")
    l5.place(x=200,y=250)
    e5=Entry(frame,font=label_font)
    e5.place(x=350,y=250)

    l6=Label(frame,text="Discount:",font=label_font,bg="skyblue")
    l6.place(x=200,y=300)
    e6=Entry(frame,font=label_font)
    e6.place(x=350,y=300)

    l7=Label(frame,text="Net Fee:",font=label_font,bg="skyblue")
    l7.place(x=200,y=350)
    e7=Entry(frame,font=label_font)
    e7.place(x=350,y=350)

    l8=Label(frame,text="DLM:",font=label_font,bg="skyblue")
    l8.place(x=200,y=400)
    e8=Entry(frame,font=label_font)
    e8.place(x=350,y=400)

    l9=Label(frame,text="GST:",font=label_font,bg="skyblue")
    l9.place(x=200,y=450)
    e9=Entry(frame,font=label_font)
    e9.place(x=350,y=450)

    l10=Label(frame,text="Final Amount:",font=label_font,bg="skyblue")
    l10.place(x=200,y=500)
    e10=Entry(frame,font=label_font)
    e10.place(x=350,y=500)

    b2=Button(frame,text="Calculate",command=lambda:cal(root),font=label_font,bg="brown",fg="white")
    b2.place(x=350,y=550)

    b3=Button(frame,text="Submit",font=label_font,bg="green",fg="white")
    b3.place(x=650,y=600)


import pymysql as mysql
def cal(root):
    root=Tk()
    root.title("calculate")

connection = mysql.connect(
    host='localhost',
    user='root',
    password='livewire',
    database='python1',
)
cursor = connection.cursor()
""" cursor.execute("create database python")
cursor.execute("show databases")
cursor.execute("use python") """

cursor.execute("""
    CREATE TABLE IF NOT EXISTS fees (
        student_id INT PRIMARY KEY AUTO_INCREMENT,
        admission_fee DECIMAL(10, 2),
        net_fee DECIMAL(10, 2),
        GST DECIMAL(10, 2),
        DLM DECIMAL(10, 2),
        offer_fee DECIMAL(10, 2),
        discount DECIMAL(10, 2)
    )
""")


cursor.execute("""
    INSERT INTO fees (admission_fee, net_fee, GST, DLM, offer_fee, discount)
    VALUES
    (1000, 5000, 900, 300, 700, 200)""")

connection.commit()

query = """
    SELECT admission_fee,net_fee,GST,DLM,offer_fee,discount,
        (admission_fee + net_fee + GST + DLM + offer_fee - discount) AS final_amount
    FROM fees"""

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(f"Admission Fee: {row[0]}")
    print(f"Net Fee: {row[1]}")
    print(f"GST: {row[2]}")
    print(f"DLM: {row[3]}")
    print(f"Offer Fee: {row[4]}")
    print(f"Discount: {row[5]}")
    print(f"Final Amount: {row[6]}")


cursor.close()
connection.close()


""" #save txt file

import pymysql as mysql

def save(root):
    root=Tk()
    root.title("txt file")
    try:
        connection = mysql.connect(
            host='localhost',   
            user='root',    
            password='livewire',
            database='details'
        )

        if connection.connect():
            print("Connected to MySQL database")

           
            cursor = connection.cursor()

            
            query = "SELECT * FROM fee details;"  

            cursor.execute(query)

            rows = cursor.fetchall()

            file_path = 'fee details.txt'

            with open(file_path, 'w') as file:
                # Write the column headers
                column_headers = [i[0] for i in cursor.description]
                file.write('\t'.join(column_headers) + '\n')

                # Write each row of data
                for row in rows:
                    row_data = '\t'.join(map(str, row))
                    file.write(row_data + '\n')

            print(f"Fee details have been saved to {file_path}")

    except mysql.Error as err:
        print(f"Error: {err}")
    finally:
        
        if connection.connect():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Call the function to save fee details to a text file """

root.mainloop()