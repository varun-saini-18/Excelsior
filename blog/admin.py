from django.contrib import admin
from .models import Article
from .models import Poem
from .models import Miscellaneous

admin.site.register(Article)
admin.site.register(Poem)
admin.site.register(Miscellaneous)