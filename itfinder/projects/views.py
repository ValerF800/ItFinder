from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Tag, Review
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects


# def projects(request):
#     projects = Project.objects.all()
#     return render(request, 'projects/projects.html', {'projects':projects})
# def project(request, pk):
#     project = Project.objects.get(id=pk)
#     return render(request, 'projects/single-project.html', {'project' : project})



def projects(request):
	projects, search_query = searchProjects(request)
	custom_range, projects = paginateProjects(request, projects, 10)

	context = {'projects': projects, }
	return render(request, 'projects/projects.html', context)


def project(request, project_slug):
	project = Project.objects.get(slug=project_slug)
	tags = project.tags.all()
	form = ReviewForm()
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		review = form.save(commit=False)
		review.project = project
		review.owner = request.user.profile
		review.save()
		project.getVoteCount

		messages.success(request, 'Ваш отзыв был добавлен!')
		return redirect('project', project_slug=project.slug)
	return render(request, 'projects/single-project.html', {'project': project, 'form': form})

@login_required(login_url="login")
def createProject(request):
	profile = request.user.profile
	form = ProjectForm()

	if request.method == 'POST':
		newtags = request.POST.get('newtags').replace(',',  " ").split()
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			project = form.save(commit=False)
			project.owner = profile
			project.save()

			for tag in newtags:
				tag, created = Tag.objects.get_or_create(name=tag)
				project.tags.add(tag)
			return redirect('account')
	context = {'form': form}
	return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, slug):
	profile = request.user.profile
	# project = Project.objects.get(slug=slug)
	project = profile.project_set.get(slug=slug)
	form = ProjectForm(instance=project)

	if request.method == 'POST':
		newtags = request.POST.get('newtags').replace(',',  " ").split()

		form = ProjectForm(request.POST, request.FILES, instance=project)
		if form.is_valid():
			project = form.save()
			for tag in newtags:
				tag, created = Tag.objects.get_or_create(name=tag)
				project.tags.add(tag)

			return redirect('account')

	context = {'form': form, 'project': project}
	return render(request, "projects/project_form.html", context)


def deleteProject(request, slug):
	project = Project.objects.get(slug=slug)
	if request.method == 'POST':
		project.delete()
		return redirect('projects')
	context = {'object': project}
	return render(request, 'projects/delete.html', context)

def projects_by_tag(request, tag_slug):
	tag = get_object_or_404(Tag, slug=tag_slug)
	projects = Project.objects.filter(tags__in=[tag])
	context = {
        "projects": projects	}

	return render(request, "projects/projects.html", context)