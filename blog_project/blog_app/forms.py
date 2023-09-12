from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextField
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.Textarea, label='')
    title = forms.CharField(widget=forms.TextInput
                            (attrs={
                                'placeholder':' 제목',
                                'style': 'width: 99%; height: 30px; border: solid 1px #CAC8C5; border-radius:3px;'
                                }),
                            label= '',required=True)
    content = forms.CharField(widget=SummernoteWidget(),
                            label= '',required=True)
    field_order = [
        'title', 'content'
    ]


    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "content": SummernoteWidget(),
        }

    def clean(self):
        clean_data = super().clean()

        title = clean_data.get('title','')
        content = clean_data.get('content', '')

        if title == '':
            self.add_error('title', '글 제목을 입력하세요')
        elif content == '':
            self.add_error('content', '글 내용을 입력하세요')

        