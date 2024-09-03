from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import MenuGenre, Menu, Log
from django.views.generic.edit import CreateView 
from django.urls import reverse
from urllib.parse import urlencode
from linebot import LineBotApi
from linebot.models import TextSendMessage
# Create your views here.

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
group_id = settings.GROUP_ID


def send_line_message(message_text):
    try:
        line_bot_api.push_message(group_id, TextSendMessage(text=message_text))
    except Exception as e:
        print(f"Error sending message: {e}")


class HomeView(ListView):
    model = MenuGenre 
    template_name = "index.html"
    context_object_name = "menu_genres"
    
class OrderView(ListView):
    model = Menu 
    template_name = "order.html"
    context_object_name = "menu_list"
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Menu.objects.filter(genre__id=pk)
        return queryset
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["genre"] = MenuGenre.objects.get(id=pk)
        
        if message := self.request.GET.get("message"):
            context['message'] = message
        
        return context
    
        
class OrderConfirmView(DetailView):
    model = Menu
    template_name = "confirm.html"
    context_object_name = "menu" 
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        menu = Menu.objects.get(id=pk)
        log = Log.objects.create(
            menu=menu
        )
        log.save()
        query_params = urlencode({"message": f"まいど!{menu.name}を注文しました!"})
        base_url = reverse('order', kwargs={'pk': menu.genre.id,
            })
        send_line_message(menu.name)
        redirect_url = f"{base_url}?{query_params}"
        return HttpResponseRedirect(redirect_url)
    
        
    
class OrderLogView(ListView):
    template_name = "log.html"
    model = Log
    context_object_name = "log_list"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logs = Log.objects.all()
        sum = 0
        for log in logs:
            sum += log.menu.price
        
        context["sum"] = sum
        
        return context
    
class Checkout(TemplateView):
    template_name = "checkout.html"
    
    def post(self, request, *args, **kwargs):
        send_line_message("お会計入りました!")
        return HttpResponseRedirect(reverse('thanks'))
    
class Thanks(TemplateView):
    template_name = "thanks.html"