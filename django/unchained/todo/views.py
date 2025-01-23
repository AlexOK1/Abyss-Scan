from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Manga, Favorite


# Home 
def index(request):
    return render(request, 'home.html')



# Manga liste 
def manga_list(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_list.html', {'mangas': mangas})

# Manga detalje
def manga_detail(request, id):
    manga = get_object_or_404(Manga, id=id)
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(user=request.user, manga=manga).exists()
    return render(request, 'manga_detail.html', {'manga': manga, 'is_favorited': is_favorited})

# Favorite en manga 
@login_required
def favorite_manga(request, id):
    manga = get_object_or_404(Manga, id=id)
    Favorite.objects.get_or_create(user=request.user, manga=manga)
    return redirect('manga_detail', id=manga.id)

# fjern favoirte manga 
@login_required
def unfavorite_manga(request, id):
    manga = get_object_or_404(Manga, id=id)
    Favorite.objects.filter(user=request.user, manga=manga).delete()
    return redirect('manga_detail', id=manga.id)

# en liste for brugeren om deres favorit mangaer
@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorite_list.html', {'favorites': favorites})
