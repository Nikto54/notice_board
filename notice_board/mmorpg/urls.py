from django.urls import path
from .views import (
    NoticeCreateView,
    NoticeUpdateView,
    NoticeListView,
    NoticeView,
    ResponseCreateView,
    UserNoticeListView
)

app_name = 'mmorpg'

urlpatterns = [
    path('create/', NoticeCreateView.as_view(), name='NoticeCreate'),
    path('<int:pk>/edit/', NoticeUpdateView.as_view(), name='NoticeUpdate'),
    path('all/', NoticeListView.as_view(), name='NoticeList'),
    path('<int:pk>/', NoticeView.as_view(), name='NoticeDetail'),
    path('notice/<int:notice_pk>/response_create/', ResponseCreateView.as_view(), name='ResponseCreate'),
    path('responses/', UserNoticeListView.as_view(), name='UserNoticeList'),
]
