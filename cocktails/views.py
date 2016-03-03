from django.shortcuts import HttpResponse
from django.views.generic import View

class IngredientView(View):

    def get(self, request):

        return HttpResponse('It worked')