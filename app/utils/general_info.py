from aiogram.utils.markdown import hbold, hitalic

from app.misc import i18n

_ = i18n.gettext


def get_general_information():
    INFO = [
        hbold(_("What is this bot for?")),
        _("This bot serves to speed up and simplify communication with project executors."),
        "\n",
        hbold(_("What are we doing?")),
        "\n",
        hitalic(_("Web Development")),
        _("HTML, CSS, JS, PYTHON, PHP"),
        hitalic(_("Design")),
        _("Web Design, Mobile App Design, Identity"),
        hitalic(_("Digital marketing")),
        _("SEO, Contextual Advertising (Google Ads, Yandex Metrica, My Target, SMM (Instagram, Vk, Facebook)"),
        "\n",
        hbold(_("How does it all work?")),
        _(
            "We have a huge number of projects in our assets, and a constantly expanding database of performers."
            "As soon as we open a new project, there is a distribution of proposals to all potentially interested performers."
        ),
        hitalic(_("We")),
        _("We formulate a clear technical task"),
        _("We organize project logistics (time management, project team coordination, working infrastructure - test stands, testing, etc.)"),
        _("We give technical expertise (there are full-time specialists who will help solve any task)"),
        hitalic(_("You")),
        _("Clearly do all the work according to the terms of reference and deadlines and get paid for it."),
        "\n",
        hbold(_("What can we offer for specialists?")),
        "\n",
        hitalic(_("Absolutely free schedule")),
        _("The only restrictions are deadlines and check points"),
        "\n",
        hitalic(_("Relevant experience")),
        _("We work all over the world, keep in touch and work on projects with highly qualified specialists, and share all knowledge and best practices with everyone who wants to join our community"),
        "\n",
        hitalic(_("Flexible payment system")),
        _("Before each project, we will personally agree on the size, terms of payment and the system of fines for non-compliance with the conditions (both for us and for the performers)."),
        "\n",
        hbold(_("Payment")),
        "\n",
        _(
            "Cash rewards are always discussed in person. "
            "All financial nuances are clearly negotiated before any work. "
            "We are still working on a format for contractual relations, and therefore, "
            "so far all relations with performers are built on a non-contractual basis."
        ),
        "\n",
        hbold(_("FAQ")),
        "\n",
        hitalic(_("But what if my skills do not match your occupation?")),
        _("If you think that your skills do not match our profile, then you can still fill out the questionnaire. Any skills will find their application. We will try to find a project for you."),
        "\n",
        hitalic(_("Is it possible to use your services for my projects?")),
        _("If you already have projects, but you don’t have enough resources to execute them, you can also contact us by sending a text message to this bot.")
    ]
    return "\n".join(INFO)
