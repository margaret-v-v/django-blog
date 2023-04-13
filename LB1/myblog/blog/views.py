from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic.base import View #род класс, на базе которого будут создаваться представления
from .models import Post
from .form import CommentsForm

class PostView(View):
    '''Вивод записів'''
    def get(self,request):
        posts = Post.objects.all()  #ссылка на всю инфу из таблы, постлист - имя, по которому обращаемся к данным, которые взяли
        return render(request, 'blog/blog.html', {'post_list':posts})  # render объединяет шаблон и данные из модели+возвращает объект


class PostDetail(View):
    '''Окрема сторінка записів'''
    def get(self, request, pk): #pk = id post number
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post':post})

class AddComments(View):
    '''Додавання коментарів'''
    def post(self, request,pk):
        form = CommentsForm(request.POST)#все данные от пользователя
        if form.is_valid():#валидно ли?
            form = form.save(commit=False)#сохр в бд если хорошо, ф. приостановляет сохр для редакт данных и доб новых
            form.post_id = pk
            form.save()#сохр все данные в бд
        return redirect(f'/{pk}')