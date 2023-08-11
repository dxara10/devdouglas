from django.db import models


class Contato(models.Model):

    id_contato = models.AutoField(primary_key=True)

    Nome = models.TextField(max_length=255)

    Email = models.EmailField(max_length=255)

    Telefone = models.TextField(max_length=255)