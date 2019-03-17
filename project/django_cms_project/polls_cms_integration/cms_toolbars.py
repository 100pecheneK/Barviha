from cms.utils.urlutils import admin_reverse
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from polls.models import Poll


class PollToolbar(CMSToolbar):


    def populate(self):

        menu = self.toolbar.get_or_create_menu('polls_cms_integration-polls', 'Polls')

        menu.add_sideframe_item(
            name='Новая Запись',
            url=admin_reverse('polls_poll_changelist'),
        )

        menu.add_modal_item(
            name=('Add a new poll'),
            url=admin_reverse('polls_poll_add'),
        )

        buttonlist = self.toolbar.add_button_list()

        buttonlist.add_sideframe_button(
            name='Poll list',
            url=admin_reverse('polls_poll_changelist'),
        )




toolbar_pool.register(PollToolbar)  # register the toolbar