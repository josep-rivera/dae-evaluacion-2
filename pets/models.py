from django.db import models


class Owner(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"


class Pet(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueño = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="mascotas")

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
