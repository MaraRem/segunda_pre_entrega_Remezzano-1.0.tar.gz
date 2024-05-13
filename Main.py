from segunda_pre_entrega_Remezzano.Clientes import Cliente

Cliente1 = Cliente("Pedro","Pascal",331236547,"Santiago de Chile")
Cliente2 = Cliente("Roberto","Gomez Bolaños",556547898, "Mexico DF")
Cliente3 = Cliente("Cersei","Lannister",12365478,"Desembarco del Rey")
Cliente4 = Cliente("Popeye","Elmarino",987654587,"El Mar")
Cliente5 = Cliente("Lisa", "Simpson", 654889987, "Avenida Siempre Viva")


print(Cliente1)
print(Cliente2.compra("Notebook"))
print(Cliente4.paga())
print(Cliente5.consulta("Pelopincho"))