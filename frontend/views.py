import operator

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from frontend.forms import ContactForm
from frontend.models import Insight, Testimonial, Upload, UploadForm, Question, Vote, PossibleAnswer, PersonToken

services_list = [
    {
        'description': """
                We are well-placed and have the capability to advise on and facilitate speedy incorporation in Ghana of 
                all forms of corporate entities, such as limited liability and unlimited liability companies, companies 
                limited by guarantee, branch offices of foreign companies, sole proprietorships, and partnerships. 
                We also represent clients in their registration with the Ghana Investment Promotion Centre (GIPC), 
                Ghana Free Zones Board (GFZB), and sector-specific regulatory bodies such as the Minerals Commission, 
                the Petroleum Commission, etc. as necessary.
                """,
        'title': 'Entities Registration',
        'slug': 'entities-registration',
        'icon': '<i class="fas fa-signature fa-2x"></i>',
    },
    {
        'description': """
                    We have expertise in providing excellent company secretarial services and support (in both French and English) to the 
                    management and boards of directors of companies, board committees, and shareholders of small, medium and 
                    large companies, both internationally and locally, in conformity with best practices around the world. 
                    We also have significant experience of maintaining the corporate registered offices and statutory registers of 
                    clients, and of liaising with the Registrar- General’s Department to effect the myriad of changes that 
                    take place in the lifetime of a company.
                """,
        'title': 'Company Secretarial',
        'slug': 'company-secretarial',
        'icon': '<i class="fas fa-pen-nib fa-2x"></i>',
    },
    {
        'description': """
                        We provide seamless business tax advisory services to our clients, from tax planning and financial
                         accounting to tax compliance. We also assist with registration with the relevant tax authorities
                          for companies’ income tax (IT) and value added tax (VAT), monthly calculation and remittance of
                           withholding tax (WHT) and VAT, review and submit IT returns, and conduct tax compliance review
                            of companies’ tax and accounting records, covering VAT, WHT, and employee-related taxes.
                    """,
        'title': 'Tax Advisory & Allied Services',
        'slug': 'tax-advisory-allied-services',
        'icon': '<i class="fas fa-coins fa-2x"></i>',
    },
    {
        'description': """
                    We provide advice on corporate governance, and ensure that our clients follow sound corporate 
                    governance practices to ensure accountability, fairness and transparency in their 
                    relationships with their different stakeholders.
                """,
        'title': 'Corporate Governance',
        'slug': 'corporate-governance',
        'icon': '<i class="fas fa-building fa-2x"></i>',
    },
    {
        'description': """
                    We have expertise in navigating the maze of regulatory and other requirements for doing 
                    business in Ghana in industries such as insurance, telecommunications, and the downstream and 
                    upstream petroleum sectors.
                """,
        'title': 'Compliance',
        'slug': 'compliance',
        'icon': '<i class="fas fa-registered fa-2x"></i>',
    },
    {
        'description': """
                        We have expertise and extensive experience in providing immigration advice and support to 
                        both individuals and companies. From work/ residence permits and dual citizenship applications, 
                        to indefinite leave to remain and right of abode applications, we assist individuals to 
                        regularize their stay in Ghana.
                    """,
        'title': 'Immigration',
        'slug': 'immigration',
        'icon': '<i class="fas fa-plane fa-2x"></i>',
    },
    {
        'description': """
                    For added convenience and speed in commencing business, you can purchase a ready-made company from us.
                    """,
        'title': 'Shelf companies',
        'slug': 'shelf-companies',
        'icon': '<i class="fas fa-archway fa-2x"></i>',
    },
    {
        'description': """
                    We advise on the liquidation of companies that no longer intend to continue in business, 
                    and provide experienced liquidators to handle the process.
                """,
        'title': 'Liquidation',
        'slug': 'liquidation',
        'icon': '<i class="fas fa-coins fa-2x"></i>',
    },
    {
        'description': """
                    From personal to business and official documents, we provide professional oral and written 
                    translation services in French and English.
                """,
        'title': 'Translation',
        'slug': 'translation',
        'icon': '<i class="fas fa-language fa-2x"></i>',
    },
    {
        'description': """
                       We provide nominee directors and shareholders for companies and individuals.
                   """,
        'title': 'Nominee Services',
        'slug': 'nominee-services',
        'icon': '<i class="fas fa-anchor fa-2x"></i>',
    },
    {
        'description': """
                    We provide a suite of human resource services as follows: compensation and benefits administration, 
                    recruitment, job evaluation, performance management, and payroll compliance.
                """,
        'title': 'Human Resources',
        'slug': 'human-resources',
        'icon': '<i class="fas fa-user-circle fa-2x"></i>',
    },
]


def index_view(request):
    context = {
        'banners': [
            {
                'src': '/static/images/banner-image-2.jpg',
                'text': '...seamless corporate solutions',
                'cta_text': 'Learn more',
            }
        ],
        'services': services_list,
        'insights': Insight.objects.filter(is_active=True)
    }
    return render(request, 'frontend/index.html', context)


def about_view(request):
    return render(request, 'frontend/about.html')


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            send_mail(
                f"[ContactPage] {contact_form.cleaned_data.get('subject')}",
                f"Name: {contact_form.cleaned_data.get('name')}\n"
                f"Email: {contact_form.cleaned_data.get('email')}\n"
                f"Phone: {contact_form.cleaned_data.get('phone')}\n\n"
                f"Message: {contact_form.cleaned_data.get('message')}\n",
                'contact-us-page@oxfordconsultantsgh.com',
                ['akuaa@oxfordconsultantsgh.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message has successfully been submitted')
        pass
    else:
        contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }
    return render(request, 'frontend/contact.html', context)


def services_view(request, slug):
    service = None
    for s in services_list:
        if s['slug'] == slug:
            service = s
    context = {
        'service': service
    }
    return render(request, 'frontend/service.html', context)


def redirect_to_english(request):
    return redirect(reverse('frontend:home'))


def testimonials_view(request):
    context = {
        'testimonials': Testimonial.objects.all()
    }
    return render(request, 'frontend/testimonials.html', context)


def voting_index(request):
    context = {}
    return render(request, 'frontend/voting_index.html', context)


def voting_view(request, ordering):
    question = Question.objects.get(ordering=ordering)
    context = {
        'question': question,
        'token': request.GET.get('token')
    }
    return render(request, 'frontend/voting_view.html', context)


def voting_view_answer(request, ordering):
    question = Question.objects.get(ordering=ordering)
    answer = PossibleAnswer.objects.get(id=int(request.GET.get('answer')))
    person = PersonToken.objects.get(token=request.GET.get('token'))

    try:
        Vote.objects.get(question=question, person=person).delete()
    except:
        pass
    Vote.objects.get_or_create(question=question, person=person, answer=answer)
    return redirect(reverse('frontend:voting_view_results', args=(question.ordering,))+f'?token={person.token}')


def voting_view_results(request, ordering):
    question = Question.objects.get(ordering=ordering)
    token = request.GET.get('token')
    answers = {

    }
    for possible_answer in question.possible_answers.all():
        if not answers.get(possible_answer.id, None):
            answers[possible_answer.id] = 0
        answers[possible_answer.id] += sum(Vote.objects.filter(question=question, answer=possible_answer).values_list('person__weight', flat=True))
    winner = max(answers.items(), key=operator.itemgetter(1))[0]
    a = list(answers.keys())
    a.remove(winner)
    context = {
        'token': token,
        'question': question,
        'next': question.ordering + 1,
        'winner':  PossibleAnswer.objects.get(id=winner),
        'answers':  answers,
        'winner_votes': answers[winner],
        'loser_votes': answers[a[0]]
    }
    return render(request, 'frontend/voting_view_results.html', context)



def voting_view_summary(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'frontend/voting_view_summary.html', context)


def upload_form_view(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload: Upload = upload_form.save()
            messages.success(request, f'{upload.file_name} uploaded successfully')
            send_mail(
                subject=f"Upload on Oxford Consultants  [{upload.name}]",
                message=f"File upload: <a href='{upload.file.url}'>{upload.file_name}</a>",
                from_email='uploads@oxfordconsultantsgh.com',
                recipient_list=['akuaa@oxfordconsultantsgh.com'],
                fail_silently=False,
            )
    return redirect(request.META['HTTP_REFERER'])
