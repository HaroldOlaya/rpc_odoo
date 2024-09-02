from xmlrpc import client as xmlrpclib

url = 'http://localhost:8069'
username = '' #aca va el usuario
password = '' # aca la password
db = '' # nombre de la db

common = xmlrpclib.ServerProxy(url+'/xmlrpc/common')
uid = common.login(db, username, password)
#para crear un contacto despues del metodo se coloca clave valor la clave es el nombre del campo
model = 'res.partner'
search = []
method = 'create'
operation = xmlrpclib.ServerProxy(url+'/xmlrpc/object')
#create_contact=operation.execute(db, uid, password, model, method, {'name':'Harold rpc', 'phone':'123456789'})
#print(create_contact)

# para editar un contacto el 44 es el id del contacto los datos a cambiar luego del id podemos colocar [44,45,...]
model = 'res.partner'
method = 'write'
#is_it_write= operation.execute(db, uid, password, model, method, [44], {'name':'Harold write', 'phone':'987654321'})
#print(is_it_write)


# para eliminar un contacto
model = 'res.partner'
method = 'unlink'
#is_it_unlink= operation.execute(db, uid, password, model, method, [44])
#print(is_it_unlink)

#para archivar un contacto
model = 'res.partner'
method= 'write'
is_it_write= operation.execute(db, uid, password, model, method, [45], {'active':False})
print(is_it_write)
