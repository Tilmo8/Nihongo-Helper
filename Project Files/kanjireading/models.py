from django.db import models

# Create your models here.
class Kanji(models.Model):
    # Choices
    N5 = 'N5'
    N4 = 'N4'
    N3 = 'N3'
    N2 = 'N2'
    N1 = 'N1'
    JLPT_LEVELS = [
        (N5, 'N5'),
        (N4, 'N4'),
        (N3, 'N3'),
        (N2, 'N2'),
        (N1, 'N1')
    ]

    # Database Fields
    kanji = models.CharField(
        null = False,
        blank = False,
        max_length = 1
    )

    jlpt_level = models.CharField(
        null = False,
        blank = False,
        choices = JLPT_LEVELS,
        max_length = 2  
    )

    onyomi = models.CharField(blank = True, max_length=255)
    kunyomi = models.CharField(blank = True, max_length=255)

    subtitle = models.CharField(blank = False, max_length=255) # 玉 = jewel
    meanings = models.CharField(blank = False, max_length=255) # 玉 = jewel; ball

    # Meta Class
    class Meta:
        verbose_name = 'kanji'
        verbose_name_plural = 'kanji'

    # ToString Method
    def __str__ (self):
        return self.kanji

class Reading(models.Model):
    KUNYOMI = 'KU';
    ONYOMI = 'ON';

    YOMI_TYPES = [
        (KUNYOMI, 'Kun')
    ]

    # Database Fields
    kanji = models.ForeignKey(Kanji, on_delete=models.CASCADE)
    yomi_type = models.CharField(max_length=2, choices=YOMI_TYPES, blank=False)

    reading = models.CharField(max_length=255, blank=False)

    # ToString Method
    def __str__(self):
        return "" + self.kanji + " (" + self.yomi_type + "): " + self.reading