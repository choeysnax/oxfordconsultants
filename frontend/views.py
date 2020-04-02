from django.shortcuts import render


# Create your views here.
def index_view(request):
    context = {
        'banners': [
            {
                'src': '/static/images/banner-image-2.jpg',
                'text': 'Seamless corporate solutions',
                'cta_text': 'Learn more',
            }
        ],
        'services': [
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
                'icon': '<i class="fas fa-coins fa-2x"></i>',
            },
            {
                'description': """
                    We provide advice on corporate governance, and ensure that our clients follow sound corporate 
                    governance practices to ensure accountability, fairness and transparency in their 
                    relationships with their different stakeholders.
                """,
                'title': 'Corporate Governance',
                'icon': '<i class="fas fa-building fa-2x"></i>',
            },
            {
                'description': """
                    We have expertise in navigating the maze of regulatory and other requirements for doing 
                    business in Ghana in industries such as insurance, telecommunications, and the downstream and 
                    upstream petroleum sectors.
                """,
                'title': 'Compliance',
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
                'icon': '<i class="fas fa-plane fa-2x"></i>',
            },
            {
                'description': """
                    For added convenience and speed in commencing business, you can purchase a ready-made company from us.
                    """,
                'title': 'Shelf companies',
                'icon': '<i class="fas fa-archway fa-2x"></i>',
            },

            {
                'description': """
                    We advise on the liquidation of companies that no longer intend to continue in business, 
                    and provide experienced liquidators to handle the process.
                """,
                'title': 'Liquidation',
                'icon': '<i class="fas fa-tint fa-2x"></i>',
            },

            {
                'description': """
                    From personal to business and official documents, we provide professional oral and written 
                    translation services in French and English.
                """,
                'title': 'Translation',
                'icon': '<i class="fas fa-language fa-2x"></i>',
            },
            {
                'description': """
                       We provide nominee directors and shareholders for companies and individuals.
                   """,
                'title': 'Nominee Services',
                'icon': '<i class="fas fa-anchor fa-2x"></i>',
            },
            {
                'description': """
                    We provide a suite of human resource services as follows: compensation and benefits administration, 
                    recruitment, job evaluation, performance management, and payroll compliance.
                """,
                'title': 'Human Resources',
                'icon': '<i class="fas fa-user-circle fa-2x"></i>',
            },
        ]
    }
    return render(request, 'frontend/index.html', context)


def about_view(request):
    return render(request, 'frontend/about.html')


def contact_view(request):
    return render(request, 'frontend/contact.html')


def services_view(request, slug=None):
    if slug:
        return render(request, 'frontend/service.html')
    else:
        return render(request, 'frontend/services.html')
