from django.contrib import admin
from .models import Weather

admin.site.register(Weather)

# {% for el in weather %}
#     <dic class="alert alert-warning mt-2">
#         <h3><u>{{ el.title }}</u></h3>
#         <p>
#     </dic>