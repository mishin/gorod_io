# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import capfirst

from gorod.utils.word_processor import WordProcessor

from ckeditor.fields import RichTextField


class City(models.Model):
    """
        City class
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_gent = models.CharField(max_length=255, null=True, blank=True)
    short_title = models.CharField(max_length=255, null=True)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    region = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_city'
        verbose_name_plural = 'cities'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title_gent:
            self._set_title_gent()
        super(City, self).save(*args, **kwargs)

    def _set_title_gent(self):
        wordproc = WordProcessor()
        self.title_gent = capfirst(wordproc.inflect(self.title, 'gent'))


# OLD
class CityInfo(models.Model):
    """
        City info hub
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    #text = RichTextField(max_length=25000, help_text="Some questions preface", null=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_cityinfo'
        verbose_name = 'city hub'
        verbose_name_plural = 'city hub'


# OLD
class CityInfoQuestion(models.Model):
    """
        One city question-answer pair
    """
    cityinfo = models.ForeignKey(CityInfo, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = RichTextField(max_length=25000)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'gorod'
        #unique_together = ('cityinfo', 'question(20)')
        db_table = 'gorod_cityinfoquestion'

    def get_absolute_url(self):
        return reverse('gorod:city-info-question', kwargs={
            'city_name': self.cityinfo.city.name,
            'question_id': self.id
        })


class CityWelcome(models.Model):
    """
        City Welcome page for new users
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE, unique=True)
    text = RichTextField(max_length=25000)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_citywelcome'

    def get_absolute_url(self):
        """
            Http Link to this page
        """
        return reverse('gorod:welcome', kwargs={
            'city_name': self.city.name,
        })


