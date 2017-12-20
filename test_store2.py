# encoding=utf8
import shopify
import requests
import json
import pprint
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')

API_KEY = '5a08a70ed4abd9a0f46a349d0cd08625'
PASSWORD = 'f725a802b54e8fc016ffc68af6a4a701'
SHOP_NAME = 'nerdempire00'
page = range(1, 2)


#product_ids = get_all_resources(shopify.Product, fields="id")

# order = requests.get( "https://nerdempire00.myshopify.com/admin/orders/count.json",
#                              auth=(API_KEY,PASSWORD))

product = requests.get( "https://nerdempire00.myshopify.com/admin/products/count.json",
                             auth=(API_KEY,PASSWORD))
'''
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

c = 0

for c in page:
    product_list = requests.get("https://nerdempire00.myshopify.com/admin/products.json?limit=250&page=" + str(c),
                                auth=(API_KEY, PASSWORD))
    print c
    for p in product_list.json()['products']:
        if(p != ''):
            desc = str(p['title'])
            print desc, ' descrizione'
            code = '2000'
            c += 1
            try:
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = """INSERT INTO nerdempyre (descr1) VALUES (%s);"""
                    cursor.execute(sql, desc)
                    
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                    connection.commit()
            except:
                print 'error'
'''
# print order.json()['count'], 'ordini'
#print product.json()['count'], 'prodotti'



