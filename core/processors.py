from .models import About, Category, Link, Post

def context_dictionary(request):
    ctx_dic = {}
    ctx_dic['abouts'] = About.objects.latest('created')
    ctx_dic['categories'] = Category.objects.filter(active=True) 
    ctx_dic['dates'] = Post.objects.dates('created', 'month', order='DESC').distinct()
    ctx_dic['links'] = Link.objects.all()
    return ctx_dic