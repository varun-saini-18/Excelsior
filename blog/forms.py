from django import forms

from .models import Article
from .models import Poem

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'preview', 'text', 'author')

class PoemForm(forms.ModelForm):

    class Meta:
        model = Poem
        fields = ('title', 'preview', 'text', 'author')