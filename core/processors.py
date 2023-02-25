from .models import About, Category, Link, Post

#about
def ctx_dic_about(request):
    ctx_about = {}
    ctx_about['abouts'] = About.objects.latest('created')
    return ctx_about

#categorias
def ctx_dic_category(request):
    ctx_category = {}
    ctx_category['categories'] = Category.objects.filter(active=True)
    return ctx_category

#archivos

#Redes sociales
def ctx_dic_link(request):
    links_ctx = {}
    links_ctx['links'] = Link.objects.all()
    """ for link in links:
        if link.url:
            links_ctx[link.key]= {'url':link.url, 'icon':link.icon, 'name':link.name} """
    
    return links_ctx

def ctx_dic_history(request):
    ctx_history = {}
    ctx_history['dates'] = Post.objects.dates('created', 'month', order='DESC').distinct()
    return ctx_history