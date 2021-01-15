from django.db import models


class Category_m(models.Model):

    Category = models.CharField(max_length=50, blank=False, unique=True,
                                verbose_name='Category',
                                help_text='Vehicle Category?'
                                )
    Image = models.ImageField(blank=True,
                              verbose_name='Image',
                              help_text='Category Image?'
                              )
    ACTIVE = (
        (True, 'Yes'),
        (False, 'No'),
    )
    Active = models.BooleanField(default=False, choices=ACTIVE,  # unique=True,
                                 verbose_name='Enable/Disable',
                                 help_text='Enable/Disable Inventory'
                                 )

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
