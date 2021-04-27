from django.shortcuts import render
from django.views import View
from main_app.spell_checker.main import Main
# Create your views here.

class MainApp(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'result': '', 'query_sentence': '', 'answer_list': []})

    def post(self, request, *args, **kwargs):
        query_sentence = request.POST['query_sentence']
        result = Main().getResult(query_sentence)
        print(query_sentence)
        return render(request, self.template_name, {'result': 'response', 'query_sentence': query_sentence, 'answer_list': result})