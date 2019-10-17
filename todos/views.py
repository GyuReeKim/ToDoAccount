from django.shortcuts import render
# from IPython import embed

# Create your views here.
def index(request):
    # # embed()
    # visit_num = request.session.get('visit_num', 0)
    # # 방문 할 때마다 visit이 1씩 늘어남
    # request.session['visit_num'] = visit_num + 1
    
    # request.session.modified = True

    # context = {
    #     'visit_num': visit_num,
    # }

    return render(request, 'todos/index.html')