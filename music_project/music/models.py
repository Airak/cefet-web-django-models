from django.db import models

# Create your models here.

class Musico(models.Model):
	gen = (
	    (0, 'Feminino'),
	    (1, 'Masculino'),
    )
	nome = models.TextField()
	sexo = models.IntegerField(choices=gen, default=1)
	data_nascimento = models.DateField()

	def __str__(self):
		return self.nome

class EstiloMusical(models.Model):
	nome = models.TextField()

	def __str__(self):
		return self.nome

class Banda(models.Model):
	nome = models.TextField()
	estilo_musical = models.ForeignKey('EstiloMusical', related_name='banda', on_delete=models.PROTECT)
	musico = models.ManyToManyField('Musico', related_name='banda')

	def __str__(self):
		return self.nome