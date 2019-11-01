from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Persona
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    personas = Persona.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'personas': personas})
def post_detail(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'blog/post_detail.html', {'persona': persona})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.published_date = timezone.now()
            persona.save()
            return redirect('post_detail', pk=persona.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.published_date = timezone.now()
            persona.save()
            return redirect('post_detail', pk=persona.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def publish(self):
    self.published_date = timezone.now()
    self.save()
def post_publish(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
def post_remove(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    post.delete()
    return redirect('post_list')

