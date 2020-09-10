from django.db import models
# Create your models here.

class Usuario(models.Model):
    matricula = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)
    nome = models.CharField(max_length=64)

class Setor(models.Model):
    nome = models.CharField(max_length=30)

class Acessa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    permissao = models.CharField(max_length=15, choices=[
          ('adm','Administrador'),
          ('cord','Cordenador'),
          ('bols','Bolsista'),
          ('vist','Visitante'),

      ])

class Animal(models.Model):
    codigo = models.IntegerField(primary_key=True)
    peso = models.DecimalField(max_digits=5 , decimal_places=2)
    nome = models.CharField(max_length=30)
    raca = models.CharField(max_length=30, default='Bovino')
    data_registro = models.DateField(blank = True, null = True)
    sexo = models.CharField(max_length=10 , choices=[
          ('F','Feminino'),
          ('M','Masculino')
      ])

# class Macho(Animal):
#     inicRepr = models.DateField(blank = True, null = True)
#     fimRepr = models.DateField(blank = True, null = True)
    
#     def reproducao(self, data):
#         self.inicRepr = data
    
#     def fim_reproducao(self, data):
#         self.fimRepr = data
   
# class Femea(Animal):
#     inicLact = models.DateField(blank = True, null = True)
#     fimLact = models.DateField(blank = True, null = True)

#     def lactacao(self, data):
#         self.inicLact = data
    
#     def fim_lactacao(self, data):
#         self.fimLact = data

class Produc_leite(models.Model):
    
    data = models.DateField()
    quantidade = models.DecimalField(max_digits=5 , decimal_places=2)
    femea = models.ForeignKey(Animal, on_delete=models.CASCADE)

class Saida_Leite(models.Model):
    
    data = models.DateField()
    quantidade = models.IntegerField()
    destino = models.CharField(max_length=30)
    responsavel = models.CharField(max_length=30)

class Cobertura(models.Model):
    inicio = models.DateField(blank = True, null = True)
    macho = models.ForeignKey(Animal, related_name='macho' , on_delete=models.DO_NOTHING)
    femea = models.ForeignKey(Animal, related_name='femea' , on_delete=models.DO_NOTHING)
    inicio2 = models.DateField(blank = True, null = True)

class Gravidez(models.Model):
    inicio = models.DateField(blank = True, null = True)
    fim = models.DateField(blank = True, null = True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    inicio2 = models.DateField(blank = True, null = True)

class Nascimento(models.Model):
    data = models.DateField()
    pai = models.ForeignKey(Animal, related_name='pai' ,on_delete=models.DO_NOTHING)
    matriz = models.ForeignKey(Animal, related_name='matriz' , on_delete=models.DO_NOTHING)
    filhote = models.ForeignKey(Animal, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5 , decimal_places=2)
    obito = models.BooleanField()

# class Gasto(models.Model):
    
#     valor = models.DecimalField(max_digits=7 , decimal_places=5)
#     data = models.DateField()

class Material(models.Model):
    
    tipo = models.CharField(max_length=30, choices=[
        ('med','Medicamento'),
        ('equip','Equipamento Veterinário'),
        ('limp','Material de Limpeza')
        ])
    nome = models.CharField(max_length=30, primary_key=True)
    quantidade = models.IntegerField()
    # quant_un = models.DecimalField(max_digits=5 , decimal_places=2)
    # un_medida = models.CharField(max_length=3, choices=[
    #     ('l','l'),
    #     ('ml','ml'),
    #     ('g','g'),
    #     ('mg','mg')
    #     ])
    validade = models.DateField()

# class Aquisicao(models.Model):
    
#     gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
#     material = models.ForeignKey(Material, on_delete=models.CASCADE)
 
class Secacao(models.Model):
    
    data = models.DateField()
    matriz = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    leite = models.CharField(max_length=30, choices=[
        ('n','NÃO MAIS'),
        ('p','POUCO LEITE'),
        ('m','MUITO LEITE')
        ])

