from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from .models import Project, Service

@login_required
def dashboard(request):
    projects = Project.objects.prefetch_related(
        Prefetch('services', queryset=Service.objects.order_by('external_port'))
    ).filter(is_active=True)
    
    # Calculate some stats for the dashboard
    total_projects = projects.count()
    total_services = sum(project.services.count() for project in projects)
    
    context = {
        'projects': projects,
        'total_projects': total_projects,
        'total_services': total_services,
    }
    return render(request, 'ports/dashboard.html', context)
