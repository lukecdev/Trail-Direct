from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """
    Form for product details
    """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

class ReviewForm(forms.ModelForm):
    """
    Form for product reviews
    """
    class Meta:
        model = Review
        fields = ("text", "rating")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        product_review = self.initial.get("product_reviews", False)
