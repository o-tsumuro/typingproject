from django.views import generic
from .models import Content

class IndexView(generic.DetailView):
    model = Content
    template_name = "index.html"
    context_object_name = "typing_object"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk", 1)
        return Content.objects.get(pk=pk)
    
class ContentListView(generic.ListView):
    model = Content
    template_name = "content_list.html"
    context_object_name = "content"
    queryset = Content.objects.order_by("pk")