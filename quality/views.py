import json

from django.shortcuts import render, redirect
from .forms import ProjectForm, ScenarioForm, BlockForm, CommentsForm
from .models import Projects, Scenario, Block, Comments, Review
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

    request.session['scenario_data'] = data.pk

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
    dt = Projects.objects.get(pk=request.session['scenario_data'])
    raw_data = Scenario.objects.filter(relation=dt)
    data = raw_data.get(pk=pk)
    block = Block()
    block_lists = data.block_relation.all()
    form = BlockForm()
    comment_form = CommentsForm()
    comments_list = Comments.objects.filter(scenario_relation=pk)

    context = {
        'form': form,
        'comment_form': comment_form,
        'data': data,
        'list': block_lists,
        'position': 'scenario',
        'raw_data': raw_data,
        'comments_list':comments_list,
    }

    if request.method == 'POST':
        key_counter = request.POST.keys()
        print(request.POST)
        if len(key_counter) == 2:
            saved_data = save_info(request, block)
            saved_data.save()
            data.block_relation.add(saved_data)
            data.save()
        else:
            comment = Comments()
            comment.scenario_relation = Scenario.objects.get(pk=pk)
            saved_data = save_info(request, comment)
            saved_data.save()
        return redirect('scenario_detail', pk)

    return render(request, 'quality/scenario_detail.html', context)


def scenario_detail_block(request, **kwargs):
    scenario_id = kwargs['pk0']
    block_id = kwargs['pk1']
    project_id = Projects.objects.get(pk=request.session['scenario_data'])
    raw_data = Scenario.objects.filter(relation=project_id)
    block_item = Block.objects.get(pk=block_id)
    data = raw_data.get(pk=scenario_id)
    block = Block()
    block_lists = data.block_relation.all()
    form = BlockForm()
    comment_form = CommentsForm()

    comments_list = Comments.objects.filter(block_relation=block_id)

    print(block_item.desc)
    context = {
        'block_item':block_item,
        'form': form,
        'comment_form': comment_form,
        'data': data,
        'list': block_lists,
        'position': 'scenario',
        'raw_data': raw_data,
        'comments_list':comments_list,
    }

    if request.method == 'POST':
        key_counter = request.POST.keys()
        print(request.POST)
        if len(key_counter) == 2:
            saved_data = save_info(request, block)
            saved_data.save()
            data.block_relation.add(saved_data)
            data.save()
        else:
            comment = Comments()
            comment.block_relation = Block.objects.get(pk=block_id)
            comment.scenario_relation = Scenario.objects.get(pk=scenario_id)
            saved_data = save_info(request, comment)
            saved_data.save()
        return redirect(f'/procedure/scenario/deatil/{scenario_id}/{block_id}/')

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


def block_update(request, pk):
    context ={}
    return render(request, 'quality/blocks.html', context)

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


