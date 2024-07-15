from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('alignres', views.seqalign, name='seqalign'),
    path('alignment', views.alignment, name='alignment'),
    path("search", views.search, name='search'),
    path("filter_data", views.search, name='filter_data'),
    path("kegg", views.kegg, name='kegg'),
    path("kegg_page", views.kegg_page, name='kegg_page'),
    path("taxonomytbdata", views.taxonomytbdata, name='taxonomytbdata'),
    path("taxonomytbpres", views.taxonomytbpres, name='taxonomytbpres'),
    path("results/<org>", views.resultsdetails),
    path("genes/<gene>", views.genesdetails),
]