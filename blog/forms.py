from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','email','message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4,'placeholder': 'Xabaringizni kiriting'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email kiriting'}),
        }
    def validate(self):
        if not self.cleaned_data['name']  or self.cleaned_data['email'] or self.cleaned_data['message']:
            raise forms.ValidationError('Barcha Fieldlarni toldirish talab etiladi!')

        return self.cleaned_data
