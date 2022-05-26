import json

from django.shortcuts import render, redirect
from .forms import ProjectForm, ScenarioForm, BlockForm, CommentsForm
from .models import Projects, Scenario, Block, Comments
from .utils import save_info

def main(request):
    return render(request, 'quality/main.html' )


# ============= 프로젝트 뷰 ===============
def project_list(request):
    data = Projects.objects.all().order_by('-created_at')
    return render(request, 'quality/project_list.html', context={'list': data, 'position': 'project'})


def project_detail(request, pk):
    data = Projects.objects.get(pk=pk)
    scenario = Scenario.objects.filter(relation=data)
    form = ScenarioForm()
    context = {
        'data': data,
        'form': form,
        'list': scenario,
        'position': 'project',
    }
    target_data = Scenario()
    if request.method == "POST":
        saved_data = save_info(request, target_data)
        saved_data.relation = data
        saved_data.save()
    return render(request, 'quality/project_detail.html', context)


def project_input(request):
    form = ProjectForm()
    data = Projects()

    context = {
        'form': form,
        'position': 'project',
    }

    if request.method == "POST":

        saved_data = save_info(request, data)
        saved_data.save()
        # request.session['last_position'] = 'project'
        return redirect('project_list')

    return render(request, 'quality/project_input.html', context)


# ============= 시나리오 뷰 ===============
def scenario_detail(request, pk):
    data = Scenario.objects.get(pk=pk)
    block = Block()
    block_lists = data.block_relation.all().order_by('order')

    comment_form = CommentsForm()
    comments = Comments()

    form = BlockForm()
    context = {
        'form': form,
        'data': data,
        'list': block_lists,
        'position': 'scenario'
    }
    if request.method == 'POST':
        if len(block_lists) == 0:
            block_order = 1
        else:
            block_order = len(block_lists) + 1

        saved_data = save_info(request, block)
        saved_data.order = block_order
        saved_data.save()

        data.block_relation.add(saved_data)
        data.save()

        context = {
            'form': form,
            'data': data,
            'list': block_lists,
            'position': 'scenario'
        }

        return redirect('scenario_detail', pk)

    return render(request, 'quality/scenario_detail.html', context)


def scenario_input(request):
    form = ScenarioForm()
    context = {
        'form': form,
        'position': 'scenario',
    }
    return render(request, 'quality/project_input.html', context)


# ============= 블럭 뷰 ===============
def block_list(request):
    data = Scenario.objects.all().order_by('-created_at')
    return render(request, 'quality/project_list.html', context={'list': data, 'position': 'block'})


def block_input(request):
    form = BlockForm()
    context = {
        'form': form,
        'position': 'block',
    }
    return render(request, 'quality/project_input.html', context)


# ============= 코멘트 뷰 ===============
def comment_list(request):
    data = Scenario.objects.all().order_by('-created_at')
    return render(request, 'quality/project_list.html', context={'list': data, 'position': 'comment'})


def comment_input(request):
    form = CommentsForm()
    context = {
        'form': form,
        'position': 'comment',
    }
    return render(request, 'quality/project_input.html', context)


