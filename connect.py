import pymysql


def connect(user):
    db = pymysql.connect(host=user['host'], user=user['username'], password=user['pass'], database="sklep_db")
    return db


def get_shops(user):
    rows = []
    shop = {}
    db = connect(user)
    db.begin()
    sql = "SELECT oddzialy.id_oddzialu, oddzialy.nazwa, adresy.ulica, adresy.nr_domu, adresy.kod_pocztowy, adresy.miejscowosc FROM `oddzialy`, adresy WHERE oddzialy.id_adresu=adresy.id_adresu"
    cursor = db.cursor()
    cursor.execute(sql)
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        else:
            shop['id'] = str(row[0])
            shop['text'] = row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4] + ' ' + row[5]
            rows.append(dict(shop))
    db.close()
    return rows


def get_products(user, pos, selection, query):
    product = {}
    products = []
    db = connect(user)
    db.begin()
    if pos is not None:
        if selection == 'nazwa':
            sql = "SELECT DISTINCT towary.id_towaru, nazwa, cena FROM towary, stany WHERE nazwa LIKE '%{}%' AND stany.id_towaru=towary.id_towaru AND stany.id_oddzialu={} ORDER BY towary.id_towaru".format(
                query, pos)
        elif selection == 'ID':
            sql = "SELECT DISTINCT towary.id_towaru, nazwa, cena FROM towary, stany WHERE towary.id_towaru={} AND stany.id_towaru=towary.id_towaru AND stany.id_oddzialu={} ORDER BY towary.id_towaru".format(
                query, pos)
        elif selection == 'opis':
            sql = "SELECT DISTINCT towary.id_towaru, nazwa, cena FROM towary, stany WHERE towary.opis LIKE '%{}%' AND stany.id_towaru=towary.id_towaru AND stany.id_oddzialu={} ORDER BY towary.id_towaru".format(
                query, pos)
        elif selection == 'ALL':
            sql = "SELECT DISTINCT towary.id_towaru, nazwa, cena FROM towary, stany WHERE stany.id_towaru=towary.id_towaru AND stany.id_oddzialu={} ORDER BY towary.id_towaru".format(
                pos)
    else:
        if selection == 'nazwa':
            sql = "SELECT id_towaru, nazwa, cena FROM towary WHERE nazwa LIKE '%{}%'".format(query)
        elif selection == 'ID':
            sql = "SELECT id_towaru, nazwa, cena FROM towary WHERE id_towaru={}".format(query)
        elif selection == 'opis':
            sql = "SELECT id_towaru, nazwa, cena FROM towary WHERE opis LIKE '%{}%'".format(query)
        else:
            sql = "SELECT id_towaru, nazwa, cena FROM towary"
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            else:
                product['id'] = row[0]
                product['name'] = row[1]
                product['price'] = row[2]
                products.append(dict(product))
    except:
        products = []
    db.close()
    return products


def get_info(id, user):
    sql = "SELECT * FROM towary WHERE id_towaru={}".format(id)
    db = connect(user)
    db.begin()
    cursor = db.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    db.close()
    return row


def get_quantity(pos, prod, user):
    sql = 'SELECT SUM(stany.ilosc) FROM stany WHERE stany.id_oddzialu={} AND stany.id_towaru={}'.format(pos, prod)
    db = connect(user)
    db.begin()
    cursor = db.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    db.close()
    if row[0] is None:
        return '0'
    return str(row[0])
