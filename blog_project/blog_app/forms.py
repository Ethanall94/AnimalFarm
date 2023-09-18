from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextField
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput
            (attrs={
                'placeholder':' 제목',
                'style': 'width: 99%; height: 30px; border: solid 1px #CAC8C5; border-radius:3px;'}),
                label= '',required=True)
    
    content = forms.CharField(widget=SummernoteWidget(),
                            label= '',required=False)
    
    topic_choices = [
        ('일상', '일상'),
        ('요리', '요리'),
        ('여행', '여행'),
        ('영화', '영화'),
        ('IT / 전자기기', 'IT/전자기기'),]

    topic = forms.ChoiceField(
        choices = topic_choices,
        widget = forms.RadioSelect,
        label = 'TOPIC',
        required = False)
    
    temporary = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'topic', 'content_poster']