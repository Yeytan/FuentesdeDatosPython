import sqlite3

conexion = sqlite3.connect('Ejemplo.db')


c = conexion.cursor()

#c. execute ('''CREATE TABLE acciones ( fecha text, operacion text, simbolo text, cantidad real, precio real)''')

#c.execute("INSERT INTO acciones VALUES ('29/nov/2000','venta','INV',100,10)")

#c.execute("INSERT INTO acciones VALUES ('24/nov/2001','compra','INV',444,4)")

#c.execute("INSERT INTO acciones VALUES ('11/sep/1998','rembolso','INV',500,5)")

#c.execute("INSERT INTO acciones VALUES ('24/may/2003','compra','INV',666,6)")

#c.execute("INSERT INTO acciones VALUES ('21/abr/1985','venta','INV',999,9)")

c.execute("INSERT INTO acciones VALUES ('24/nov/2001','compra','INV',444,4)")


conexion.commit()

conexion.close()
