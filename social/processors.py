from .models import Link
def context_dict(request):
    ctx = {}
    links = Link.objects.all()
    # for link in links:
    #     ctx[link.key] = link.url
    # Comprension de lista
    ctx = {link.key: link.url for link in Link.objects.all()}
    #ctx['links'] = Link.objects.all()
    return ctx