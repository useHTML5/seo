# coding: utf-8
from __future__ import unicode_literals
from cms.extensions.toolbar import ExtensionToolbar
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, PAGE_MENU_IDENTIFIER
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse


@toolbar_pool.register
class SiteAppToolbar(ExtensionToolbar):
    def populate(self):
        self.seo_menu = self.toolbar.get_or_create_menu('seo_menu', 'SEO настройки')
        self.menu_favicon()
        self.menu_files()
        self.menu_counters()
        self.menu_meta()

    def menu_favicon(self):
        admin_url = admin_reverse('favicon_favicon_changelist')
        self.seo_menu.add_sideframe_item(u"Favicon", url=admin_url)

    def menu_files(self):
        admin_url = admin_reverse('files_confirmfile_changelist')
        self.seo_menu.add_sideframe_item(u"Файлы подтверждения", url=admin_url)

    def menu_meta(self):
        admin_url = admin_reverse('meta_meta_changelist')
        self.seo_menu.add_sideframe_item(u"Мета теги", url=admin_url)

    def menu_counters(self):
        admin_url = admin_reverse('counters_counter_changelist')
        self.seo_menu.add_sideframe_item(u"Счетчики", url=admin_url)
