from locale import PM_STR
import tempfile
from uuid import uuid4
from django.db import models
from django.conf import settings
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contact(BaseModel):
    class Meta:
        verbose_name="Kontakt"
        verbose_name_plural="Kontakty"
    def __str__(self):
        return f"{self.name} ({self.phone_number})"

    name = models.CharField("Imię", max_length=50)
    phone_number = models.CharField("Numer kontaktowy", max_length=20)


class Animal(BaseModel):
    class Meta:
        verbose_name="Zwierzę"
        verbose_name_plural="Zwierzęta"

    class Sex(models.TextChoices):
        MALE = 'male', 'Samiec'
        FEMALE = 'female', 'Samica'

    class Spices(models.TextChoices):
        DOG = 'dog', 'Pies'
        CAT = 'cat', 'Kot'
        OTHER = 'other', 'Inne'

    class Size(models.TextChoices):
        SMALL = 'small', 'Mały zwierzak'
        MEDIUM = 'medium', 'Średni zwierzak'
        LARGE = 'big', 'Duży zwierzak'

    def __str__(self) -> str:
        return f"{self.name}"

    name = models.CharField("Imię", max_length=50)
    spice = models.CharField("Gatunek",choices=Spices.choices, max_length=50)
    description = models.TextField("Opis")
    age = models.IntegerField("Wiek")
    weight = models.FloatField("Waga")
    additional_notes = models.TextField("Dodatkowe uwagi")
    sex = models.CharField("Płeć",choices=Sex.choices, max_length=50)
    breed = models.CharField("Rasa / W typie...", max_length=100)
    size = models.CharField("Rozmiar",choices=Size.choices, max_length=50)
    contacts = models.ManyToManyField(Contact, verbose_name="Numery kontaktowe do adopcji")

    @property
    def form_link(self):
        if self.spice == self.Spices.DOG.value:
            return "https://docs.google.com/forms/d/1sGGmlt3Wqzu-qRTFG4Qc_WAcEAgpA0f-YAjghXE9M2w/viewform?fbclid=IwAR25QoCrvvyCUCH16lh619iFyWXn1qsQWAbH_5wu45db08gBsFe8pH9xNnw&edit_requested=true"
        return "https://docs.google.com/forms/d/1aZ7GuUAQWVyyvKXdQC6E3XYnZcDZb-lAZwv1acYJ0hU/viewform?fbclid=IwAR1g3G59ae7MPObycL8OnTEtfWBDceKvhw2t22RtXvhLVRtplxZt17U0t7g&edit_requested=true"

class Photo(BaseModel):
    class Meta:
        verbose_name="Zdjęcie"
        verbose_name_plural="Zdjęcia"
    image = models.ImageField("Zdjęcie")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="photos")

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return settings.PROD_HOST + self.image.url
        return self.link

    def save(self, *args, **kwargs):
        from PIL import Image
        from io import BytesIO
        from django.core.files.uploadedfile import InMemoryUploadedFile
        from django.core.files.base import ContentFile
        from PIL.ImageOps import exif_transpose
        if self.image and self.image.name.split('.')[-1]!="webp":
            img = Image.open(
                self.image.file
            )
            image = img#.convert('RGB')
            basewidth = 1000
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            image = image.resize((basewidth,hsize), Image.ANTIALIAS)
            f = tempfile.TemporaryFile()

            buffer = BytesIO()
            image = exif_transpose(image)
            image.save(fp=buffer, format='webp')
            image=ContentFile(buffer.getvalue())
            self.image.save(
                f'{self.animal.name}_{self.id}.webp',
                InMemoryUploadedFile(
                    image,  # file
                    None,  # field_name
                    f'{self.animal.name}_{str(uuid4())}.webp',  # file name
                    'image/webp',  # content_type
                    image.tell,  # size
                    None,  # content_type_extra
                ),
            )
        super().save(*args, **kwargs)    
