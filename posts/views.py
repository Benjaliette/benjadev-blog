from django.views.generic import ListView, DetailView, CreateView
from posts.models import Post
from posts.forms import PostForm
from django.urls import reverse

# Create your views here.
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return reverse("posts:show", kwargs={'pk': self.object.id})
