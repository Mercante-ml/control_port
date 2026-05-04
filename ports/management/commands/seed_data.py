from django.core.management.base import BaseCommand
from ports.models import Project, Service

class Command(BaseCommand):
    help = 'Seeds the database with initial port data'

    def handle(self, *args, **kwargs):
        # DS Prime
        ds_prime, _ = Project.objects.get_or_create(
            name='DS Prime',
            domain='dsprime.org',
            description='Projeto Principal'
        )
        Service.objects.get_or_create(project=ds_prime, name='Django (Web)', external_port=8000, internal_port=8000, service_type='web')
        Service.objects.get_or_create(project=ds_prime, name='PostgreSQL', external_port=5432, internal_port=5432, service_type='db')

        # NBA
        nba, _ = Project.objects.get_or_create(
            name='NBA',
            domain='nba.dsprime.org',
            description='Portal de Playoffs NBA'
        )
        Service.objects.get_or_create(project=nba, name='Django (Web)', external_port=8001, internal_port=8000, service_type='web')
        Service.objects.get_or_create(project=nba, name='PostgreSQL', external_port=5433, internal_port=5432, service_type='db')
        Service.objects.get_or_create(project=nba, name='Redis', external_port=6380, internal_port=6379, service_type='cache')

        # Kanban
        kanban, _ = Project.objects.get_or_create(
            name='Kanban',
            domain='kanban.dsprime.org',
            description='Gerenciamento de Tarefas'
        )
        Service.objects.get_or_create(project=kanban, name='Django (Web)', external_port=8002, internal_port=8000, service_type='web')
        Service.objects.get_or_create(project=kanban, name='PostgreSQL (DB)', external_port=5434, internal_port=5432, service_type='db')

        # Port Control (Self)
        port_control, _ = Project.objects.get_or_create(
            name='Port Control',
            domain='port.dsprime.org',
            description='Sistema de Controle de Portas'
        )
        Service.objects.get_or_create(project=port_control, name='Django (Web)', external_port=8003, internal_port=8000, service_type='web')
        Service.objects.get_or_create(project=port_control, name='PostgreSQL', external_port=5435, internal_port=5432, service_type='db')

        self.stdout.write(self.style.SUCCESS('Successfully seeded initial port data'))
