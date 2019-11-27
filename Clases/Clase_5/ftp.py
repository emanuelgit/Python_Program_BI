# -*- coding: utf-8 -*-


import paramiko

'''FUNCIONES FTP'''

def download_data_sftp(host, username, password, origin, destination, port):
	'''
	Descarga un archivo desde un SFTP en una ubicacion dada, hay que usar paramiko, si no funciona tal vez bajar el whl. Ejemplo: 
	host = "sftp.riskamerica.com"
	username = "AGF_X"
	pw = "clave"
	origin = './out/Composicion_Indice.csv'
	dst = 'C://Users/Desktop/Compo1006.csv'
	port = 22
	downloadDataSFTP(host, username, pw, origin, dst, port)
	'''
	sftp = None
	sftp_open = False
	transport = paramiko.Transport((host, port))
	transport.connect(username=username, password=password)
	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp_open = True
	sftp.get(origin, destination)
	if sftp_open:
		sftp.close()
		sftp_open = False
	transport.close()


'''FUNCIONES SSH'''

def connect_ssh(host, username, password, port):
    '''
    Se conecta a un servidor via ssh y devuelve un objeto cliente.
    '''
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
    return client
