from google_images_search import GoogleImagesSearch


from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Item
from .forms import PositionForm

#------ Insert GOOGLE API ------#
API_KEY = 'Google API Key'
CX = 'Google CX'

# Login Form 
class CustomLoginView(LoginView):
    template_name = 'api/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')

# Register User Form 
class RegisterPage(FormView):
    template_name = 'api/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super(RegisterPage, self).get(*args, **kwargs)

# Main Page Of App -> Generates images  
class ItemList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Item.objects.last() # First Object in Table 
        # context['count'] = Item.objects.count() # Number of Rows in Table Etc Number of Items

        #------ Google API ------#

        # images = []
        # num_images = 9 # Number of Images to Pass *Max 10*
    
        # search = Item.objects.last().name
        # gis = GoogleImagesSearch(API_KEY, CX)

        # _search_params = {
        #     'q': search,
        #     'num': num_images,
        #     'fileType': 'jpg|png',
        #     'safe': 'active', 
        # }
        # gis.search(search_params=_search_params)
        # for image in gis.results():
        #     images.append(image.url)

        # my_list = { i : images[i] for i in range(0, len(images) ) }
        #------ GOOGLE API -------#

        # context['item'] = context['item'].filter(field__lookup=value)[0] # Grab first Object after applying Filter > Used to Grab first (Completed = False) from Model Boolen
        # context['count'] = context['item'].filter().count() # Grab count of Objects with (Completed = false) to populate Progress Bar
        
        #-------- Dummy Data --------#
        my_list = {'one': 'https://imageio.forbes.com/specials-images/imageserve/5d35eacaf1176b0008974b54/2020-Chevrolet-Corvette-Stingray/0x0.jpg?format=jpg&crop=4560,2565,x790,y784,safe&width=960', 'two': 'https://i.ytimg.com/vi/tArC9-RHmU4/maxresdefault.jpg', 'three': 'https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/news/2022/08_22_monterey/cover_m.jpg', 'four': 'https://s7d1.scene7.com/is/image/volkswagen/VW_NGW6_Homepage_Vehicle_Large_2022_09_15?Zml0PWNyb3AlMkMxJndpZD04MDAmaGVpPTgwMCZmbXQ9anBlZyZxbHQ9NzkmYmZjPW9mZiYxMjM4', 'five': 'https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/news/2022/08_22_monterey/cover.jpg', 'six': 'https://car-images.bauersecure.com/wp-images/2672/1752x1168/ferrari_purosangue_30.jpg?mode=max&quality=90&scale=down', 'seven': 'https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/homepage/families-gallery/2022/04_12/family_chooser_tecnica_m.png', 'eight': 'https://www.topgear.com/sites/default/files/2022/07/Aspark_Owl_static_front.jpg', 'nine': 'https://imageio.forbes.com/specials-images/imageserve/5d35eacaf1176b0008974b54/0x0.jpg?format=jpg&crop=4560,2565,x790,y784,safe&width=1200'}
        context['my_list'] = my_list
        #-------- Dummy Data --------#

        context['my_list'] = my_list
        return context

class UpdateItem(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['url']
    template_name = 'api/item_update.html'
    success_url = reverse_lazy('main')

# Deletes Object from Model after Request and sends back to 'main' in urls.py
class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('main')

def UpdateTables(request):
    data = request.GET['image_url']
    return render(request, 'item_update.html', {'url': data})

