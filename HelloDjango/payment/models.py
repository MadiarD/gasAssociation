import os
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.core.files import File
from datetime import datetime
from io import BytesIO
from django.db import models
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

class Receipt(models.Model):
    id_p = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_receipt', null=True)
    date = models.DateTimeField()
    amount = models.FloatField()
    description = models.TextField()
    status = models.CharField(max_length=50)
    file = models.FileField(upload_to='receipt/', null=True, blank=True)
    gas_volume = models.FloatField(null=True, blank=True) 
    rate = models.FloatField(null=True)       

    def __str__(self):
        return str(self.date)

    def create_receipt_pdf(self):
        # Создание PDF в памяти
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Регистрация встроенного шрифта DejaVu Sans
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Путь к шрифту на системе Linux, проверьте путь для вашей системы
        pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))

        # Использование зарегистрированного шрифта
        c.setFont("DejaVuSans", 16)

        # Заголовок
        c.drawString(200, height - 50, "Газ төлемінің түбіртегі")

        # Дата
        c.setFont("DejaVuSans", 12)
        date_str = self.date.strftime("%Y-%m-%d %H:%M:%S")
        c.drawString(50, height - 100, f"Күні: {date_str}")

        # Данные о квитанции
        y_position = height - 150
        user_info = f"Алушы: {self.user.username if self.user else 'Белгісіз'}"
        c.drawString(50, y_position, user_info)
        y_position -= 20

        c.drawString(50, y_position, f"Сома: {self.amount} тг")
        y_position -= 20

        c.drawString(50, y_position, f"Төлем мақсаты: {self.description}")
        y_position -= 20

        c.drawString(50, y_position, f"Статус: {self.status}")
        y_position -= 20

        c.drawString(50, y_position, f"Газ көлемі: {self.gas_volume} м³")
        y_position -= 20

        c.drawString(50, y_position, f"Тариф: {self.rate} тг/м³")
        y_position -= 20

        total = self.gas_volume * self.rate
        c.drawString(50, y_position, f"Жалпы сома: {total} тг")
        y_position -= 20

        # Сохранение PDF в памяти
        c.save()

        # Сохранение PDF файла в файловое поле
        buffer.seek(0)
        filename = f"receipt_{self.id_p}.pdf"
        self.file.save(filename, File(buffer), save=False)
        buffer.close()

        # Сохранение изменений в объекте
        self.save()