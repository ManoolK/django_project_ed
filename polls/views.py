from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# from django.http import HttpResponse, Http404  # two variants to load views and errors
# from django.template import loader
# from django.utils.translation import gettext as _
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.db.models import F
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context, request))


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/poll_detail.html'

    def get_queryset(self):
        """ Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


# def poll_detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404(_("Question does not exist."))
#     return render(request, 'polls/poll_detail.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/poll_results.html'


# def poll_results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/poll_results.html', {'question': question})


def poll_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/poll_detail.html', {'question': question,
                                                          'Error_message': "You didn't select a choice."})
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:poll_results', args=(question.id,)))

