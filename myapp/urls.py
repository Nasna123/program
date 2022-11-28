from django.urls import path
from.import views

urlpatterns=[
    path('page1/',views.fun1,name='page1'),
    path('amstrong/',views.amstrong,name='amstrong'),
    path('factorial/',views.factorial,name='factorial'),
    path('fibinocci/',views.fibinocci,name='fibinocci'),
    path('hcf/',views.hcf,name='hcf'),
    path('lcm/',views.lcm,name='lcm'),
    path('palindrome/',views.palindrome,name='palindrome'),
    path('perfectno/',views.perfectno,name='perfectno'),
    path('printfactors/',views.printfactors,name='printfactors'),
    path('reversestring/',views.reversestring,name='reversestring'),
    path('sortnumbers/',views.sortnumbers,name='sortrnumbers'),
    path('sumofdigits/',views.sumofdigits,name='sumofdigits'),
    path('sumofprimeno/',views.sumofprimeno,name='sumofprimeno'),


    
]