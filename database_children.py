import sqlite3
conn=sqlite3.connect("komal_sainani99.db")
cur=conn.cursor()
sql="create table if not exists student(Roll int,Name char(20),Grade char(10))"
cur.execute(sql)
while True:
    choice=int(input("1-view 2-insert 3-delete 4-update 5-search 6-exit"))  
    if(choice==1):
        select_command=("select *from student")
        cur.execute(select_command)
        results=cur.fetchall()
        print("Roll_no Name Grade")
        for r in results:
            print(str(r[0])+"\t"+r[1]+"\t"+r[2]+"\t")
    elif(choice==2):
        roll=int(input("Enter the roll no to be inserted"))
        sname=input("Enter the name to be inserted")
        grade=input("Enter the grade")
        insert_command="insert into student(Roll,Name,Grade)\
                        values('%d','%s','%s')"%(roll,sname,grade)
        cur.execute(insert_command)
        conn.commit()
    elif(choice==3):
        roll=int(input("Enter the roll no to be deleted"))
       
        try:
            cur.execute("DELETE FROM student WHERE roll=%d"%roll)
            conn.commit()
        except:
            print("Error in delete")
    elif(choice==4):
            roll=int(input("Enter roll no to be updated"))
            newgrade=input("Enter the newgrade")
            update_command="UPDATE student SET grade='%s' WHERE roll='%d'"%(newgrade,roll)
            try:
                cur.execute(update_command)
                conn.commit()
            except:
                print("Error is update")
    elif choice==5:
            roll=int(input("Enter the roll no to be searched"))
            search_command="select *from student where roll='%d'"%roll
            cur.execute(search_command)
            r=cur.fetchone()
            if r==None:
                print("Data not found")
            else:
                print(r[0],r[1],r[2],sep='\t')                
    else:
        print("Done")
        break
conn.close()
        
