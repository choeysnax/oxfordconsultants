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


def get_services_list():
    for service in services_list:
        yield service['slug']


def services_view(request, slug):
    service = None
    for s in services_list:
        if s['slug'] == slug:
            service = s
            break
    context = {
        'service': service
    }
    return render(request, 'frontend/service.html', context)


def nsia_2023_annual_general_meeting_view(request):
    context = {
        'page': {
            'title': 'NSIA 2023 Annual General Meeting',
            'description': 'Join us for the 46th AGM of NSIA Insurance Company LTD to be held on Tuesday, 6th May 2025 at 0900h GMT via Zoom.',
        },
        'sections': [
            {
                'id': 'overview',
                'title': 'Overview & Agenda',
                'body': '''
                <div class="content">
                    <h3>Notice of Annual General Meeting</h3>
                    <p>Notice is hereby given that the 46th Annual General Meeting of NSIA INSURANCE COMPANY LIMITED (the "Company") will be held on Tuesday, 6th May, 2025 at 0900h GMT by Zoom to transact the following business:</p>

                    <div class="notification is-info is-light">
                        <p><strong>Date:</strong> Tuesday, 6th May 2025</p>
                        <p><strong>Time:</strong> 09:00 AM GMT</p>
                        <p><strong>Venue:</strong> Virtual Meeting via Zoom</p>
                        <p><strong>Link:</strong> <a href="https://us02web.zoom.us/meeting/register/YRkseKZzTUyGqZdGD4SaNQ" target="_blank" class="is-link">
                            <span class="icon"><i class="fas fa-link"></i></span>
                            <span>Click here to register. The Zoom link will be sent to your email after registration</span>
                        </a></p>
                    </div>

                    <h3>Agenda</h3>
                    <ol>
                        <li>To waive the notice period required for this meeting;</li>
                        <li>To receive and consider the Accounts and Reports of the directors and auditors for the year ended 31st December, 2023;</li>
                        <li>To receive the directors' statement on dividend for the year ended 31st December, 2023;</li>
                        <li>To authorize the directors to fix the remuneration of the auditors;</li>
                        <li>To ratify the appointment of Mrs. Monica Amissah as a director of the company, subject to the approval of the National Insurance Commission.</li>
                        <li>To ratify the remuneration of the non-executive directors.</li>
                        <li>To approve the payment of end-of-service benefits to the non-executive directors.</li>
                        <li>To transact any other business appropriate to be dealt with at an Annual General Meeting.</li>
                    </ol>

                    <div class="notification is-warning is-light mt-4">
                        <p><strong>Note:</strong> A member of the company entitled to attend and vote is entitled to appoint a proxy to attend and vote in his/her stead. A proxy need not be a shareholder. A proxy form is available in the registration link that has been provided. It must be completed and submitted online by close of business on 2nd May 2025.</p>
                    </div>

                    <p class="has-text-right">Dated at Accra this 3rd day of April 2025<br>By order of the Board<br><strong>Company Secretary</strong></p>
                </div>
                ''',
            },
            {
                'id': 'registration',
                'title': 'Registration',
                'body': '''
                <div class="content">
                    <h3>Registration Information</h3>
                    <p>All shareholders interested in attending the NSIA 46th Annual General Meeting must complete the registration process.</p>

                    <div class="steps">
                        <div class="step-item">
                            <div class="step-marker">1</div>
                            <div class="step-content">
                                <p>Visit the official Zoom registration portal at <a href="https://us02web.zoom.us/meeting/register/YRkseKZzTUyGqZdGD4SaNQ" target="_blank">https://us02web.zoom.us/meeting/register/YRkseKZzTUyGqZdGD4SaNQ</a></p>
                            </div>
                        </div>
                        <div class="step-item">
                            <div class="step-marker">2</div>
                            <div class="step-content">
                                <p>Complete the registration form with accurate contact information</p>
                            </div>
                        </div>
                        <div class="step-item">
                            <div class="step-marker">3</div>
                            <div class="step-content">
                                <p>Submit your registration and await confirmation email with unique Zoom access credentials</p>
                            </div>
                        </div>
                    </div>

                    <div class="notification is-info is-light mt-4">
                        <p><strong>Note:</strong> Upon successful registration, you will receive access to the audited financial statements and the CV of Mrs. Monica Amissah.</p>
                    </div>
                </div>
                ''',
            },
            {
                'id': 'proxy-form',
                'title': 'Proxy Form',
                'body': '''
                <div class="content">
                    <h3>Proxy Appointment</h3>
                    <p>Shareholders who cannot attend the AGM may appoint a proxy to attend and vote on their behalf. A proxy need not be a shareholder of the Company.</p>

                    <div class="box">
                        <h4>Proxy Submission Guidelines</h4>
                        <ol>
                            <li>Download the proxy form available below</li>
                            <li>Complete all required fields with accurate information</li>
                            <li>Submit the completed form via email to: <a href="mailto:akuaa@oxfordconsultantsgh.com">akuaa@oxfordconsultantsgh.com</a></li>
                            <li>Ensure your submission is received no later than close of business on 2nd May 2025</li>
                        </ol>
                    </div>

                    <p>Upon successful submission, both the shareholder and appointed proxy will receive confirmation emails with relevant details.</p>
                </div>
                ''',
                'file': {
                    'url': '/static/docs/nsia-2023-agm-proxy-form-electronic.docx'
                }
            }
        ]
    }

    # Set the first section to be displayed by default
    context['first_section'] = context['sections'][0]

    return render(request, 'frontend/agm.html', context)


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
    person = PersonToken.objects.get(token=request.GET.get('token').lower())
    if person.is_chairman and ordering == 1:
        return redirect(reverse('frontend:voting_view_results', args=(ordering,)) + f'?token={person.token}')
    context = {
        'question': question,
        'person': person
    }
    return render(request, 'frontend/voting_view.html', context)


def voting_view_answer(request, ordering):
    question = Question.objects.get(ordering=ordering)
    answer = PossibleAnswer.objects.get(id=int(request.GET.get('answer')))
    person = PersonToken.objects.get(token__iexact=str(request.GET.get('token')).strip())

    try:
        Vote.objects.get(question=question, person=person).delete()
    except:
        pass
    Vote.objects.get_or_create(question=question, person=person, answer=answer)
    return redirect(reverse('frontend:voting_view_results', args=(question.ordering,)) + f'?token={person.token}')


def voting_view_launch(request, ordering):
    old_resolution = Question.objects.get(ordering=ordering - 1)
    old_resolution.next_resolution_launched = True
    old_resolution.save()

    question = Question.objects.get(ordering=ordering)
    person = PersonToken.objects.get(token__iexact=str(request.GET.get('token')).strip())

    return redirect(reverse('frontend:voting_view_results', args=(question.ordering,)) + f'?token={person.token}')


def voting_view_results(request, ordering):
    question = Question.objects.get(ordering=ordering)
    token = request.GET.get('token').lower()
    person = PersonToken.objects.get(token=token)
    answers = {

    }
    for possible_answer in question.possible_answers.all():
        if not answers.get(possible_answer.id, None):
            answers[possible_answer.id] = 0
        answers[possible_answer.id] += sum(
            Vote.objects.filter(question=question, answer=possible_answer).values_list('person__weight', flat=True))
    winner = max(answers.items(), key=operator.itemgetter(1))[0]
    a = list(answers.keys())
    a.remove(winner)
    loser = a[0]
    w = PossibleAnswer.objects.get(id=winner)
    l = PossibleAnswer.objects.get(id=loser)
    question.consensus = w
    question.stats = {
        'w': {
            'consensus': w.consensus,
            'number': answers[winner]
        },
        'l': {
            'consensus': l.consensus,
            'number': answers[loser]
        }
    }
    question.save()

    context = {
        'person': person,
        'question': question,
        'next': question.ordering + 1 if Question.objects.filter(ordering=question.ordering + 1).exists() else False,
        'answers': answers,
        'winner': w,
        'winner_votes': answers[winner],
        'loser': l,
        'loser_votes': answers[loser]
    }
    return render(request, 'frontend/voting_view_results.html', context)


def voting_view_summary(request):
    questions = Question.objects.all().order_by('id')
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
