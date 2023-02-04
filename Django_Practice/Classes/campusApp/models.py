from django.db import models


# This creates model of University Campus.
class UniversityCampus(models.Model):
    campus_name = models.CharField(
        max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # This creats the model manager
    object = models.Manager()

    # This displays the object output values in the form of a string.

    def __str__(self):
        # This returns the input value of the campus name and state
        # field as a tuple to display in the browser instead of the default titles.
        display_campus = '{0.campus_name}: {0.state}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"
