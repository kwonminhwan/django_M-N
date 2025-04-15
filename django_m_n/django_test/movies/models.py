# movies/models.py

from django.db import models
from django.conf import settings


class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    # related_name=> 역참조할 떄 사용할 이름 , M:N관계 모델 생성 MOVIE클래스에서 선언(movie 입장에서 참조)
    # ForeignKey 또는 ManyToManyField 중 한 곳에 related_name을 추가로 작성하여 서로를 구분분
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_movies') 
    title = models.CharField(max_length=20)
    description = models.TextField()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
