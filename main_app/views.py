from django.shortcuts import render
from django.views import View
# Create your views here.

class MainApp(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'result' : '', 'query': ''})

    def post(self, request, *args, **kwargs):
        query_word = request.POST['query_word']
        return render(request, self.template_name, {'result': 'correct', 'query': query_word})