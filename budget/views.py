from django.shortcuts import render, get_object_or_404
from .models import Project 

# Create your views here.
def project_list(request):
    return render(request, 'budget/project-list.html')

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    expense_list = project.expenses.all()
    budget_left = 0
    total_transactions = 0
    for exp in expense_list:
        total_transactions += exp.amount
    budget_left = project.budget - total_transactions
    return render(request, 'budget/project-detail.html', {
        'project':project,'expense_list':expense_list,
        'total_transactions':total_transactions,
        'budget_left':budget_left
        })