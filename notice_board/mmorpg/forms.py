from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Notice, Response, Category

class NoticeForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', required=True)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент', required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Не выбрана', required=True)

    class Meta:
        model = Notice
        fields = ['title', 'content', 'category']

class ResponseForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', required=True)
    text = forms.CharField(label='Текст', required=True)
    reponse=forms.ModelChoiceField(queryset=Notice.objects.all(),label='Объявление')

    class Meta:
        model = Response
        fields = ['title', 'text']
