# from nome_arquivo_sem_extensao import NomeClasse1, NomeClasse2, NomeClasse3
from forma_geometrica_aula import FormaGeometrica, Quadrado, Circulo
if __name__ == '__main__':
    # obj_forma = FormaGeometrica()  # TypeError:
    # print(obj_forma)
    # Can't instantiate abstract class FormaGeometrica with abstract methods
    # print("Quantidade:", FormaGeometrica.get_qtd_figura())
    obj_quad = Quadrado(3)          # Objeto da subclasse concreta Quadrado
    # print("Quantidade:", FormaGeometrica.get_qtd_figura())
    print('- Quadrado:\nLado:', obj_quad.get_lado())
    print('Área:', obj_quad.area())
    print('Perímetro:', obj_quad.perimetro())
    obj_quad.set_lado(4)            # Altera o valor do lado
    print('Lado:', obj_quad.get_lado())
    print('Área:', obj_quad.area())
    print('Perímetro:', obj_quad.perimetro())
    obj_circ = Circulo(3)           # Objeto da subclasse concreta Circulo
    # print("Quantidade:", FormaGeometrica.get_qtd_figura())
    print('- Círculo:\nRaio:', obj_circ.get_raio())
    print('Área:', obj_circ.area())
    print('Perímetro:', obj_circ.perimetro())
    obj_circ.set_raio(2)
    print('Raio:', obj_circ.get_raio())
    print(f"Área: {obj_circ.area():.3f}")   # Com três casas decimais
    print('Perímetro:', obj_circ.perimetro())
    print("- Testando os métodos mensagem")
    obj_quad.mensagem()                     # Use um objeto da subclasse
    obj_circ.mensagem()
    FormaGeometrica.mensagem(obj_quad)
    FormaGeometrica.mensagem(obj_circ)
    obj_quad.mensagem2()    # <quadrado.Quadrado object at 0x000001D990E8DFD0>
    obj_circ.mensagem2()
    obj_quad.mensagem3()    # Nome da classe: Quadrado
    obj_circ.mensagem3()

