try:
    import mysql.connector
    import webbrowser
    import os
    from colored import fg, bg, attr
    from time import sleep

    # color
    res = attr('reset')
    red = fg(1)
    green = fg(2)
    y = fg(3)
except ModuleNotFoundError:
    print(+'[+] You Need Download Library ')
    x = str(input('[+] Do You Want Download Automatic Library (Yes / No)'))
    if x == 'Yes' or 'yes' or 'y' or 'Y':
        os.system('pip install mysql-connector')
        os.system('pip install colored')
        input('[+] Press Any Keys To Continue')
        os.system('cls')

try:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='url'
    )
    print(db)
except:
    print(red + '[+] Database Connection Error' + res)


def add():
    try:
        print(y + '[+] Add New URL' + res)
        c = db.cursor()
        sql = 'INSERT INTO employee(name, url) values (%s, %s)'
        name = str(input(y + '[+] Enter URL name --> ' + res))
        url = str(input(y + '[+] Enter URL --> ' + res))
        val = (name, url)
        c.execute(sql, val)
        db.commit()
        print(green + '[+] Successfully Add' + res)
        c.close()
        print(green + '[+] Loading...' + res)
        sleep(3)
        os.system('cls')
        inte()
    except:
        print(red + '[+] Some Error Try Again' + res)


def show():
    try:
        c = db.cursor()
        c.execute('SELECT * FROM employee')
        re = c.fetchall()
        print(y + '''

[+] URL DATA''' + res)
        for row in re:
            print(y + '[+] ID -->' + res, row[0])
            print(y + '[+] Name -->' + res, row[1])
            print(y + '[+] URL -->' + res, row[2])
            print(y + '------------------' + res)
        c.close()
        inte()
    except:
        print(red + '[+] Some Error Try Again' + res)


def get():
    try:
        print(y + '[+] Get URL' + res)
        c = db.cursor()
        id = str(input(y + '[+] Enter ID --> ' + res))
        c.execute('SELECT * FROM employee WHERE id = ' + id)
        r = c.fetchall()
        for i in r:
            print(y + '[+] Id -->' + res, i[0])
            print(y + '[+] Name -->' + res, i[1])
            print(y + '[+] URl -->' + res, i[2])
            iff = str(input(y + '[+] Do you want open url in browser (Yes / No)' + res))
            if iff == 'Yes' or 'yes' or 'y':
                webbrowser.open(i[2])
                print(green + '[+] Loading....' + res)
                sleep(3)
                inte()
            elif iff == 'No' or 'no' or 'n':
                c.close()
                print(green + '[+] Loading...' + res)
                sleep(3)
                os.system('cls')
                inte()


    except:
        print(red + '[+] Some error try again' + res)


def edit():
    try:
        print(y + '[+] Edit URL ' + res)
        c = db.cursor()
        id = str(input(y + '[+] Enter ID --> ' + res))
        name = str(input(y + '[+] Change Name --> ' + res))
        url = str(input(y + '[+] Change URL --> ' + res))
        sql1 = 'UPDATE employee SET name = %s WHERE ID = %s'
        sql2 = 'UPDATE employee SET url = %s WHERE ID = %s'
        val1 = (name, id)
        val2 = (url, id)
        c.execute(sql1, val1)
        c.execute(sql2, val2)
        db.commit()
        print(green + '[+] Successfully Edit ' + res)
        c.close()
        print(green + '[+] Loading...' + res)
        sleep(3)
        os.system('cls')
        inte()
    except:
        print(red + '[+] Some Error Try Again' + res)


def delt():
    try:
        print(y + '[+] Delete URL' + res)
        c = db.cursor()
        id = str(input(y + '[+] Enter ID --> ' + res))
        sql = 'DELETE FROM employee WHERE ID = %s'
        val = (id,)
        c.execute(sql, val)
        db.commit()
        print(green + '[+] Successfully Delete' + res)
        c.close()
        print(green + '[+] Loading...' + res)
        sleep(3)
        os.system('cls')
        inte()
    except:
        print(red + '[+] Some Error Try Again' + res)


def inte():
    i = fg(124)
    print(i + '''
    ██╗   ██╗██████╗ ██╗         ██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗
██║   ██║██╔══██╗██║         ██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝
██║   ██║██████╔╝██║         ██║ █╗ ██║███████║██║     ██║     █████╗     ██║   
██║   ██║██╔══██╗██║         ██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║   
╚██████╔╝██║  ██║███████╗    ╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║   
 ╚═════╝ ╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   
                                                                                ''' + res)

    print(i + '''
[+] Programming By Zyiad
[+] SnapChat --> pz_a9
[+] Instagram --> @qq.hk
[+] GitHub --> Zyiad511''' + res)

    print(y + '''
[+] 1 --> Show Data
[+] 2 --> Add URL
[+] 3 --> Get Data
[+] 4 --> Edit Data
[+] 5 --> Delet Data''' + res)
    x = int(input(y + '[+] Choose --> ' + res))
    if x >= 6:
        print(red + '[+] Please Choose From 1 To 5' + res)
        sleep(2)
        os.system('cls')
        inte()

    if x == 1:
        show()
    elif x == 2:
        add()
    elif x == 3:
        get()
    elif x == 4:
        edit()
    elif x == 5:
        delt()
    else:
        print(red + '[+] You Did Choose ' + res)


inte()
