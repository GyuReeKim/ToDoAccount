from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from .models import Todo
# from IPython import embed

# Create your views here.
@login_required
def index(request):
    # # embed()
    # visit_num = request.session.get('visit_num', 0)
    # # 방문 할 때마다 visit이 1씩 늘어남
    # request.session['visit_num'] = visit_num + 1
    
    # request.session.modified = True

    # context = {
    #     'visit_num': visit_num,
    # }

    # 현재 로그인 한 사람의 정보를 가져와서 사용한다.
    todos = request.user.todo_set.all().order_by('due_date')
    context = {
        'todos': todos,
    }

    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) # 비어있는 column이 있기 때문에, 완전히 저장하지 않고 잠시 기다린다.
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/form.html', context)

@login_required
def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo.user == request.user:
        todo.delete()
    return redirect('todos:index')