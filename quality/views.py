from django.shortcuts import render
from .forms import ProjectForm, ScenarioForm, BlockForm, CommentsForm
from .models import Projects, Scenario, Block, Comments


def project_input(request):
    form = ProjectForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        print(request.user)
        print(request.POST)
        print(request.FILES)

    return render(request, 'quality/project_input.html', context)


def scenario_input(request):
    form = ScenarioForm()
    context = {
        'form': form,
    }
    return render(request, 'quality/project_input.html', context)


def block_input(request):
    form = BlockForm()
    context = {
        'form': form,
    }
    return render(request, 'quality/project_input.html', context)


def comment_input(request):
    form = CommentsForm()
    context = {
        'form': form,
    }
    return render(request, 'quality/project_input.html', context)


