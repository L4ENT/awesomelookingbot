from app.misc import i18n
from aiogram.utils.markdown import hbold

_ = i18n.gettext

INFO = [
    hbold(_('What we do?')),
    (
        'Web - HTML, CSS, JS, PYTHON, PHP'
        '\nDesign - Web Design, Mobile Design, Identity'
        '\nMarketing - SEO, Context (Google Ads, Yandex Metrica, My Target, SMM (Instagram, Vk, Facebook)'
        '\nIf you do not see here what you are good at - we are open to any offers - we will burst into any area if the game is worth the paraffin spent.'
        '\nIf you have your own projects, but do not have enough resources to implement them, then contact us. We will definitely respond - with what we can we will help.'
    ),
    hbold(_('What do we give?')),
    (
        'Free schedule (only deadlines and checkpoints limit).'
        '\n\nTop experience. We work all over the world, keep in touch and work on projects with top experts, and share all knowledge and best practices with everyone who wants to join the community.'
        '\n\nFlexible payment system. Before each project, we personally agree on the size, terms of payment and the system of fines for non-compliance with the conditions (for both parties).'
    ),
    hbold(_('Payment')),
    (
        'Remuneration is discussed with each person personally before each project. All financial nuances are clearly agreed upon prior to any work.'
        '\nWe are not concluding an agreement yet. Not because we are a radical marginal community, but because, so far, there is no such possibility due to the complexity of implementation in terms of jurisprudence and taxation.'
        '\nBUT our policy - a contract is always good. We will gradually come to official contracts - this is a fact.'
    ),
    hbold(_('Minimum Entry Threshold')),
    (
        'Know Git at the level of clone, brunch, commit and push. The rest is personal nuances.'
    ),
    hbold(_('Who is this job for?')),
    (
        'While we cannot provide everyone with permanent projects and a stable monthly salary, we offer to consider all this as an excellent temporary part-time job, an opportunity to pump your skills and replenish your portfolio with cool projects.'
    )
]


def get_general_information():
    return '\n\n'.join(INFO)