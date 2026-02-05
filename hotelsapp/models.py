from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Hotel(models.Model):
    name = models.CharField(verbose_name='Название отеля',max_length=200,unique=True)
    address = models.CharField(verbose_name='Адрес',max_length=250)
    image = models.ImageField(verbose_name='Изображение',upload_to='images/hotels/',blank=True,null=True)
    description = models.TextField(verbose_name='Описание',blank=True)
    rating = models.DecimalField(verbose_name='Рейтинг',max_digits=3,decimal_places=2,validators=[MinValueValidator(0), MaxValueValidator(5)],default=0,blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления',auto_now=True)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
        ordering = ['-rating', 'name']

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_TYPES = [
        ('luxe', 'Люкс'),
        ('comfort', 'Комфорт'),
        ('budget', 'Бюджет')
    ]

    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='rooms',verbose_name='Отель')
    number = models.CharField(verbose_name='Номер комнаты',max_length=10)
    room_type = models.CharField(verbose_name='Тип комнаты',max_length=30,choices=ROOM_TYPES,default='budget')
    capacity = models.PositiveIntegerField(verbose_name='Вместимость',validators=[MinValueValidator(1), MaxValueValidator(10)],default=1)
    image = models.ImageField(verbose_name='Изображение',upload_to='images/rooms/',blank=True,null=True)
    amenities = models.TextField(verbose_name='Удобства',help_text='Wi-Fi, кондиционер, телевизор и т.д.',blank=True)
    description = models.TextField(verbose_name='Описание',blank=True)
    price_per_night = models.DecimalField(verbose_name='Цена за ночь',max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
    is_available = models.BooleanField(verbose_name='Доступна',default=True)
    created_at = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления',auto_now=True)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
        ordering = ['hotel', 'number']
        unique_together = ['hotel', 'number']

    def __str__(self):
        return f'{self.hotel.name} - Комната {self.number} ({self.get_room_type_display()})'


class Booking(models.Model):
    BOOKING_STATUS = [
        ('pending', 'Ожидает'),
        ('confirmed', 'Подтверждено'),
        ('cancelled', 'Отменено'),
        ('completed', 'Завершено')
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bookings',verbose_name='Пользователь')
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='bookings',verbose_name='Комната')
    check_in = models.DateField(verbose_name='Дата заезда')
    check_out = models.DateField(verbose_name='Дата выезда')
    guests = models.PositiveIntegerField(verbose_name='Количество гостей',validators=[MinValueValidator(1)])
    status = models.CharField(verbose_name='Статус',max_length=20,choices=BOOKING_STATUS,default='pending')
    total_price = models.DecimalField(verbose_name='Общая стоимость',max_digits=10,decimal_places=2,blank=True,null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления',auto_now=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} - {self.user.username} - {self.room}'