from django import forms
from .models import UserPredictDataModel, FeedModel

class UserPredictDataForm(forms.ModelForm):
    class Meta():
        model = UserPredictDataModel
        fields = '__all__'

class FeedForm(forms.ModelForm):
    class Meta():
        model = FeedModel
        fields = '__all__'