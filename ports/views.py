from django.shortcuts import render
from .models import Project

def dashboard(request):
    projects = Project.objects.prefetch_related('services').filter(is_active=True)
    
    # Calculate some stats for the dashboard
    total_projects = projects.count()
    total_services = sum(project.services.count() for project in projects)
    
    context = {
        'projects': projects,
        'total_projects': total_projects,
        'total_services': total_services,
    }
    return render(request, 'ports/dashboard.html', context)
