from xmlrpc import client as xmlrpclib

url = 'http://localhost:8069'
username = 'haroldolaya.2499@hotmail.com'
password = 'admin'
db = '20-febrero-2024'

#esto valida la session y retorna el uid
common = xmlrpclib.ServerProxy(url+'/xmlrpc/common')
uid = common.login(db, username, password)
print(uid)

#esto retorna los ids de los res.partner
model = 'res.partner'
search = []
method = 'search'
operation = xmlrpclib.ServerProxy(url+'/xmlrpc/object')
ids = operation.execute(db, uid, password, model, method, search)
print(ids)

# esto retorna los ids que cumplen con el search
model = 'res.partner'
search = [('phone','!=',False)]
method = 'search'
operation = xmlrpclib.ServerProxy(url+'/xmlrpc/object')
ids2 = operation.execute(db, uid, password, model, method, search)
print(ids2)

#esto retorna la informacion de los customer
# model = 'res.partner'
# search = []
# method = 'search'
# operation = xmlrpclib.ServerProxy(url+'/xmlrpc/object')
# ids = operation.execute(db, uid, password, model, method, search)
# method = 'read'
# list_of_partner = operation.execute(db, uid, password, model, method, ids)
# for customer in list_of_partner:
#     print(customer['id'],customer['name'], customer['phone'], customer['email'])

#esto retorna la cantidad de customer
model = 'res.partner'
search = []
method = 'search'
operation = xmlrpclib.ServerProxy(url+'/xmlrpc/object')
ids = operation.execute(db, uid, password, model, method, search)
method = 'search_count'
list_of_partner = operation.execute(db, uid, password, model, method, search)
print(list_of_partner)

# esto retorna los detalles del campo
model = 'res.partner'
method = 'fields_get'
operation = xmlrpclib.ServerProxy(url+'/xmlrpc/object')
fields = operation.execute(db, uid, password, model, method,['name','phone','email'])
print(fields)

#esto retorna la informacion de los customer con el nombre del campo
# model = 'res.partner'
# search = []
# method = 'search'
# operation = xmlrpclib.ServerProxy(url+'/xmlrpc/object')
# ids = operation.execute(db, uid, password, model, method, search)
# method = 'read'
# list_of_partner = operation.execute(db, uid, password, model, method, ids,['id','name','phone','email'])
# for customer in list_of_partner:
#     print(customer)

