from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Projeto")
    domain = models.CharField(max_length=255, blank=True, null=True, verbose_name="Domínio")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['name']

    def __str__(self):
        return self.name

class Service(models.Model):
    SERVICE_TYPES = [
        ('web', 'Web (Django/Frontend)'),
        ('db', 'Database (PostgreSQL/MySQL)'),
        ('cache', 'Cache (Redis/Memcached)'),
        ('proxy', 'Proxy (Nginx/Traefik)'),
        ('other', 'Outro'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='services', verbose_name="Projeto")
    name = models.CharField(max_length=100, verbose_name="Nome do Serviço")
    external_port = models.IntegerField(verbose_name="Porta Externa (Host)")
    internal_port = models.IntegerField(verbose_name="Porta Interna (Container)")
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES, default='web', verbose_name="Tipo de Serviço")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['external_port']

    def __str__(self):
        return f"{self.project.name} - {self.name} ({self.external_port})"
