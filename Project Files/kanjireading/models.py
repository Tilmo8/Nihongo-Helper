from django.db import models

# Create your models here.
class Reading(models.Model):

    """ Database Fields """
    pronounciation = models.CharField(max_length=255, blank=False)

    """ ToString Method """
    def __str__(self):
        return self.pronounciation

    """ Other Methods """
    def get_kanji_list(self, kanji_only=True):
        kanji_listing = []

        for reading in self.kanji_list.all():
            if kanji_only:
                item = reading.kanji.kanji
            else:
                item = ( reading.kanji.kanji, reading.yomi_type )

            kanji_listing.append(item)

        return kanji_listing


class Kanji(models.Model):
    """ Choices """
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

    """ Database Fields """
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

    # For all possible readings (ONYOMI and KUNYOMI combined)
    readings = models.ManyToManyField('Reading', related_name='kanji', through='KanjiReading', through_fields=('kanji', 'reading'))

    subtitle = models.CharField(blank = False, max_length=255) # 玉 = jewel
    meanings = models.CharField(blank = False, max_length=255) # 玉 = jewel; ball

    """ Meta Class """
    class Meta:
        verbose_name = 'kanji'
        verbose_name_plural = 'kanji'

    """ ToString Method """
    def __str__ (self):
        return self.kanji

class KanjiReading(models.Model):
    KUNYOMI = 'KU';
    ONYOMI = 'ON';

    YOMI_TYPES = [
        (KUNYOMI, 'Kunyomi'),
        (ONYOMI, 'Onyomi')
    ]

    kanji = models.ForeignKey('Kanji', related_name='kanji_readings', on_delete=models.SET_NULL, null=True)
    reading = models.ForeignKey('Reading', related_name='kanji_list', on_delete=models.SET_NULL, null=True, blank=True)
    yomi_type = models.CharField(max_length=2, choices=YOMI_TYPES, blank=False)


    """ Meta Class """
    class Meta:
        verbose_name = "KanjiReading"
        verbose_name_plural = "KanjiReadings"

    """ ToString Method """
    def __str__(self):
        return "(" + self.yomi_type + "): " + self.reading.pronounciation  