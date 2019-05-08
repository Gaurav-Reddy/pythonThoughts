

#for x in myresult:
#    print(x)


def get_table(r):
    import mysql.connector

    mydb=mysql.connector.connect(
            host=r,
            user="root",
            passwd="",
            database="test"
            )

    newcursor=mydb.cursor()
    newcursor.execute("Select `author`,`title`,`content`,`date_posted` from blog_stuff")

    myresult=newcursor.fetchall()
    r=[]
    #print(myresult)
    for x in myresult:
        r.append({"author":x[0],"title":x[1],"content":x[2],"date_posted":x[3]})
    return(r)
ty=get_table("localhost")
print(ty)
