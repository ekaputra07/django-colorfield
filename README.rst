Django Colorfield
=================

This module fills the need of having a 'colorfield' that's usable in both
django models and forms.

Makes use of http://jscolor.com/.

Usage example
=============

1. Install django-colorfield into your Django Project / Python Path.

2. Add "colorfield" into your INSTALLED_APPS in settings.py.

3. If you need to use the widget directly follow below sample code:

::

    from django import forms
    from colorfield.fields import ColorWidget

    class SomeForm(forms.Form):
        color = forms.CharField(widget=ColorWidget)

4. If you want to use form field that django-colorfield that already provided, follow below sample:

::

    from django import forms
    from colorfield.fields import ColorFormField

    class SomeForm(forms.Form):
        color = ColorFormField()

5. If you want to use Colorfield in model, use as sample below:

::

    from django.db import models
    from colorfield.fields import ColorField

    class SomeModel(models.Model):
        color = ColorField()

That's it.. Now we have color picker in our Django admin panel.
    


