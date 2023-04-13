from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField('Текст запису')
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публікації')
    img = models.ImageField('Зображення', upload_to='image')

    def __str__(self): #красивое отображение заголовок+текст+автор списком
        return self.title
    

    class Meta:                     #исп.для определения разл вещей наследоваться      другими классами(бд, разрешение, од\множ число)
      verbose_name = 'Запис' #исп для определения удобочитаемого единств имени модели, заменяет стандарт согл об именах джанго
      verbose_name_plural = 'Записи'

class Comments(models.Model):
   email=models.EmailField()
   name=models.CharField('Нікнейм', max_length=50)
   text_comments=models.TextField('Текст коментарія', max_length=1000)
   post=models.ForeignKey(Post, verbose_name='Публікації', on_delete=models.CASCADE)
   def __str__(self):
        return f'{self.name}, {self.post}'
    
   class Meta:
      verbose_name = 'Коментарій'
      verbose_name_plural ='Коментарії'