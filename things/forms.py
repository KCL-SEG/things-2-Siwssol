from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
"""Forms of the project."""

# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label = "name", max_length=35)
    description = forms.CharField(label = "description", max_length=120)
    quantity = forms.IntegerField(label = "quantity",
                                  validators=[MinValueValidator(0),MaxValueValidator(50)])

    def clean(self):
        super().clean()
        entered_name = self.cleaned_data.get("name")
        entered_desc = self.cleaned_data.get("description")
        entered_quantity = self.cleaned_data.get("quantity")

        if entered_name is not None:
            self.add_error("name can't be empty")

        if len(entered_name) > 35:
            self.add_error("name can't be more than 35 characters")

        if entered_desc is not None and len(entered_desc) > 120:
            self.add_error("description can't be more than 120 characters")

        if entered_quantity < 0 or entered_quantity > 50:
            self.add_error("quantity must be between 0 and 50")

    def save(self):
        super().save()