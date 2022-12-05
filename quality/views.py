import json

from django.shortcuts import render, redirect
from .forms import ProjectForm, ScenarioForm, BlockForm, CommentsForm, ReviewForm
from .models import Projects, Scenario, Block, Comments, Review
from .utils import save_info

def main(request):
    return render(request, 'quality/main.html' )


# ============= 프로젝트 뷰 ===============
def project_list(request):
    data_list = Projects.objects.all().order_by('-created_at')
    form = ProjectForm()
    data = Projects()

    context = {
        'form': form,
        'position': 'project',
        'list': data_list,
    }

    if request.method == "POST":
        saved_data = save_info(request, data)
        saved_data.save()
        return redirect('project_list')

    return render(request, 'quality/project_list.html', context)


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
        return redirect('project_list')

    return render(request, 'quality/project_input.html', context)


# ============= 시나리오 뷰 ===============
def scenario_detail(request, pk):
    project_id = Projects.objects.get(pk=request.session['scenario_data'])
    raw_data = Scenario.objects.filter(relation=project_id)
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
        'comments_list': comments_list,
        'project_id': project_id.pk,
    }

    if request.method == 'POST':
        if request.POST['type'] == 'block':
            saved_data = save_info(request, block)
            saved_data.save()
            data.block_relation.add(saved_data)
            data.save()
        else:
            comment = Comments()

            comment.scenario_relation = Scenario.objects.get(pk=pk)
            comment.writer = request.user
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

    context = {
        'block_item':block_item,
        'form': form,
        'comment_form': comment_form,
        'data': data,
        'list': block_lists,
        'position': 'scenario',
        'raw_data': raw_data,
        'comments_list':comments_list,
        'scenario_id':scenario_id,
        'block_id':block_id,
        'project_id':project_id.pk
    }

    if request.method == 'POST':
        if request.POST['type'] == 'block':
            saved_data = save_info(request, block)
            saved_data.save()
            data.block_relation.add(saved_data)
            data.save()
        else:
            comment = Comments()
            comment.writer = request.user
            comment.block_relation = Block.objects.get(pk=block_id)
            comment.scenario_relation = Scenario.objects.get(pk=scenario_id)
            saved_data = save_info(request, comment)
            saved_data.save()
        return redirect(f'/procedure/scenario/deatil/{scenario_id}/{block_id}/')

    return render(request, 'quality/scenario_detail.html', context)


def scenario_update(request, pk):
    scenario = Scenario.objects.get(pk=pk)
    form = ScenarioForm(instance=scenario)
    context = {
        'data': scenario,
        'form': form,
        'position': 'scenario',
    }
    if request.method == "POST":
        saved_data = save_info(request,scenario)
        saved_data.save()
        return redirect('scenario_detail', pk)

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


def block_update(request, **kwargs):
    scenario_id = kwargs['pk0']
    block_id = kwargs['pk1']
    block_item = Block.objects.get(pk=block_id)
    form = BlockForm(instance=block_item)

    if request.method == 'POST':
        block_item.desc = request.POST['desc']
        block_item.save()
        return redirect(f'/procedure/scenario/deatil/{scenario_id}/{block_id}/')

    context = {
        'form':form,
        'scenario_id':scenario_id,
        'block_id':block_id,
    }

    return render(request, 'quality/blocks.html', context)

# ============= 리뷰 뷰 ===============
def comment_list(request):
    data = Scenario.objects.all().order_by('-created_at')
    return render(request, 'quality/project_list.html', context={'list': data, 'position': 'comment'})


def comment_input(request, **kwargs):
    scenario_id = kwargs['pk0']
    block_id = kwargs['pk1']
    comment_id = kwargs['pk2']
    data = Comments.objects.get(pk=comment_id)
    review_list = Review.objects.filter(comment_relation=data)

    form = ReviewForm()
    context = {
        'data': data,
        'form': form,
        'scenario_id': scenario_id,
        'block_id': block_id,
        'position': 'review',
        'review_list': review_list,
    }

    if request.method == "POST":
        review_data = Review()

        review_data.writer = request.user
        review_data.block_relation_id = block_id
        review_data.scenario_relation_id = scenario_id
        review_data.comment_relation_id = comment_id
        saved_data = save_info(request, review_data)
        saved_data.save()

        return redirect(f'/procedure/comment/input/{scenario_id}/{block_id}/{comment_id}/')
    return render(request, 'quality/review_input.html', context)


def confirm(request, **kwargs):
    pk0 = kwargs['pk0'] #scenario
    pk1 = kwargs['pk1'] #comment
    type_sort = request.get_full_path().split('?')[1].split('=')[1]

    if request.method == 'POST':
        if type_sort == 'block':
            obj = Block.objects.get(pk=pk1)
            obj.delete()
            return redirect(f'/procedure/scenario/deatil/{pk0}/')

        elif type_sort == 'comments':
            obj = Comments.objects.get(pk=pk1)
            obj.delete()
            return redirect(f'/procedure/scenario/deatil/{pk0}/{obj.block_relation.pk}/')

        elif type_sort == 'scenario':
            obj = Scenario.objects.get(pk=pk1)
            obj.delete()
            return redirect('project_detail', pk0)


    context = {
        'pk0': pk0,
        'pk1': pk1,
        'type': type_sort,
    }

    if type_sort == 'comments':
        dummy = Comments.objects.get(pk=pk1)
        pk2 = dummy.block_relation.pk
        context = {
            'pk0': pk0,
            'pk1': pk1,
            'pk2': pk2,
            'type': type_sort,
        }

    return render(request, 'quality/confirm.html', context)