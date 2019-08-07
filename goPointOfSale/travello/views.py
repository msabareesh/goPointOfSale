from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination("Kochi","Kochi kandavanu Achi venda",False, 500, "destination_1.jpg")
    dest2 = Destination("Thrissur", "Poorangalude pooram", True, 450, "destination_2.jpg")
    dest3 = Destination("Palakkad", "Kottayudem Malambuzhayudem Naadu", False, 600, "destination_3.jpg")
    destList = [dest1, dest2, dest3]
    return render(request, 'index.html', {'destList':destList})