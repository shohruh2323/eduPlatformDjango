from django.db import models

# Create your models here.

# Таблица для категорий
class Category(models.Model):
    # Создаем столбцы
    category_name = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

# Таблицы для продуктов
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_price = models.FloatField()
    course_period = models.FloatField()
    course_description = models.TextField()
    course_photo = models.ImageField(upload_to='media', null=True, blank=True)
    course_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name

# кОРЗИНА
class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Course, on_delete=models.CASCADE)

#Таблица для личного кабинета
class Cabinet(models.Model):
    user_id = models.IntegerField()
    user_courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True)

# Таблицв акций
class Sale(models.Model):
    sale_name = models.CharField(max_length=75, null=True, blank=True)
    courses = models.ManyToManyField(Course)
    sale_start_date = models.DateTimeField()
    sale_end_date = models.DateTimeField()

    def __str__(self):
        return self.sale_name


class Programs(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    tema_uroka = models.CharField(max_length=150)
    opisaniye_temi = models.TextField()

    def __str__(self):
        return self.tema_uroka

class CourseLevel(models.Model):
    course = models.ManyToManyField(Course)

    chices = (('junior', 'Начинающий'), ('middle', 'Продолжающий'), ('pro', 'Продвинутый'))
    choice = models.CharField(max_length=15, choices=chices)

    def __str__(self):
        return self.choice


