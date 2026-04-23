#Exercicio01
# class Pessoa:
#     def __init__(self, name, age):
#         self.nome = name
#         self.idade = age
    
#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade}")
    

# p1 = Pessoa("Harry", 32)
# p2 = Pessoa("William", 42)

# p1.apresentar()
# p2.apresentar()


# #Exercicio02
# class Produto:
#     def __init__(self, name, price):
#         self.nome = name
#         if price < 0:
#             self.preco = 0
#         else:
#             self.preco = price

# prod = Produto("Lápis", -10)
# print(prod.preco)

#Exercicio03
class Contador:
    def __init__(self, value):
        self.valor = value
    
    def incrementar(self):
        self.valor += 1
    
    def resetar(self):
        self.valor = 0

cont = Contador(0)
valor = cont.incrementar()
print(valor)

# #Exercicio04
# class Banco:
#     def __init__(self, saldo):
#         self.__saldo = saldo
    
#     def depositar(self, valor):
#         return self.__saldo + valor
    
#     def sacar(self, valor):
#         if (self.__saldo - valor) >= 0:
#             return self.__saldo - valor
    
#     def mostrar_saldo(self):
#         return self.__saldo
    
# b1 = Banco(100)

# print(b1.sacar(500))
# print(b1.mostrar_saldo())


# #Exercicio05
# class Matematica:
#     def dobro(self, x):
#         return 2 * x
#     def identificador(self):
#         return "Matematica"