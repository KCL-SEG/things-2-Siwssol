from django import forms
"""Forms of the project."""

# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label = "name")
    description = forms.CharField(label = "description")
    quantity = forms.IntegerField(label = "quantity")

    def clean(self):
        super().clean()
        entered_name = self.cleaned_data.get("name")
        entered_desc = self.cleaned_data.get("description")
        entered_quantity = self.cleaned_data.get("quantity")

        if len(entered_name) > 35:
            self.add_error("name can't be more than 35 characters")

        if len(entered_desc) > 120:
            self.add_error("description can't be more than 120 characters")

        if entered_quantity < 0 or entered_quantity > 50:
            self.add_error("quantity must be between 0 and 50")

    def save(self):
        super().save()