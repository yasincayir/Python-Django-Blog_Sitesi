from django.db import models
# Create your models here.
class Article(models.Model):
    author=models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="YAZAR")
    title=models.CharField(max_length=50,verbose_name="BAŞLIK")
    content=models.TextField(verbose_name="İÇERİK")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="OLUŞTURULMA TARİHİ")
    def __str__(self):
        return self.title
    