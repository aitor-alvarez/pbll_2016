from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site
from django.contrib.auth import login, logout
from lessons.views import HomeView, ModuleView, LessonView, LoginForbiddenView, ModuleCreateView, ModuleUpdateView, ModuleDeleteView, LessonCreateView, LessonUpdateView, LessonDeleteView, LessonSectionUpdateView, PbllPageUpdateView, PbllPageView, LessonQuizQuestionCreateView, LessonQuizQuestionUpdateView, LessonQuizQuestionDetailView, LessonQuizQuestionListView, LessonQuizQuestionDeleteView
from quiz.views import QuizTake
from discussions.views import DiscussionListView, DiscussionView, PostCreateView, PostDeleteView, PostUpdateView
from core.views import HonorCodeFormView, ParticipantListView, ParticipantUpdateView, ParticipantCreateView, ParticipantDeleteView

urlpatterns = [

   # url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls')),

	url(r'^$', HomeView.as_view(), name='home'),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/filebrowser/', site.urls),
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/login/$', login, name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^quiz/', include('quiz.urls')),

    url(r'^module/add/$', ModuleCreateView.as_view(), name='module_create' ),
    url(r'^module/(?P<slug>[-\w]+)/$', ModuleView.as_view(), name='module' ),
    url(r'^module/edit/(?P<slug>[-\w]+)/$', ModuleUpdateView.as_view(), name='module_edit' ),
    url(r'^module/delete/(?P<pk>[-\w]+)/$', ModuleDeleteView.as_view(), name='module_delete' ),

    url(r'^lesson/module/(?P<module_id>[-\w]+)/add/$', LessonCreateView.as_view(), name='lesson_create' ),
    url(r'^lesson/(?P<pk>[-\w]+)/$', LessonView.as_view(), name='lesson' ),
    url(r'^lesson/edit/(?P<pk>[-\w]+)/$', LessonUpdateView.as_view(), name='lesson_edit' ),
    url(r'^lesson/(?P<pk>[-\w]+)/section/(?P<section>[-\w]+)/$', LessonView.as_view(), name='lesson_section' ),
    url(r'^lesson/section/edit/(?P<pk>[-\w]+)/$', LessonSectionUpdateView.as_view(), name='lesson_section_edit' ),
    url(r'^lesson/delete/(?P<pk>[-\w]+)/$', LessonDeleteView.as_view(), name='lesson_delete' ),

    url(r'^lesson/quiz/(?P<quiz_id>[-\w]+)/question/(?P<pk>[-\w]+)/$', LessonQuizQuestionDetailView.as_view(), name='question_preview' ),
    url(r'^lesson/quiz/(?P<quiz_id>[-\w]+)/add/question/$', LessonQuizQuestionCreateView.as_view(), name='question_create' ),
    url(r'^lesson/quiz/(?P<quiz_id>[-\w]+)/edit/question/(?P<pk>[-\w]+)/$', LessonQuizQuestionUpdateView.as_view(), name='question_edit' ),
    url(r'^lesson/quiz/(?P<quiz_id>[-\w]+)/delete/question/(?P<pk>[-\w]+)/$', LessonQuizQuestionDeleteView.as_view(), name='question_delete' ),
    url(r'^lesson/quiz/(?P<pk>[-\w]+)/list/questions/$', LessonQuizQuestionListView.as_view(), name='question_list' ),
    url(r'^lesson/quiz/(?P<quiz_id>[-\w]+)/quiz/take/', QuizTake.as_view(), name='lesson_quiz'),

    url(r'^discussions/(?P<pk>[-\w]+)/$', DiscussionView.as_view(), name='discussion_select' ),
    url(r'^discussions/$', DiscussionListView.as_view(), name='discussion' ),
    url(r'^discussions/post/add/$', PostCreateView.as_view(), name='create_post'),
    url(r'^discussions/post/delete/$', PostDeleteView.as_view(), name='delete_post'),
    url(r'^discussions/post/(?P<pk>[-\w]+)/edit/$', PostUpdateView.as_view(), name='edit_post'),


    url(r'^pbllpage/(?P<slug>[-\w]+)/$', PbllPageView.as_view(), name='pbllpage' ),
    url(r'^pbllpage/edit/(?P<slug>[-\w]+)/$', PbllPageUpdateView.as_view(), name='pbllpage_edit' ),


    url(r'^participants/$', ParticipantListView.as_view(), name='participants'),
    url(r'^participants/add/$', ParticipantCreateView.as_view(), name='add_participant'),
    url(r'^participants/edit/(?P<pk>[-\w]+)/$', ParticipantUpdateView.as_view(), name='edit_participant'),
    url(r'^participants/delete/(?P<pk>[-\w]+)/$', ParticipantDeleteView.as_view(), name='delete_participant'),

    url(r'^inactive-user/$', HonorCodeFormView.as_view(), name='honor_agreement'),
    url(r'^login-forbidden/$', LoginForbiddenView.as_view(), name='login_forbidden'),
]