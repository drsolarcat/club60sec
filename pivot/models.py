from __future__ import unicode_literals

from django.db.models import Model, CharField, URLField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.blocks import StructBlock, ListBlock, CharBlock, TextBlock, URLBlock, RichTextBlock, DateBlock, PageChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
# from wagtail.wagtailsnippets.models import register_snippet

# headers

class BottomTextHeaderBlock(StructBlock):
    header = CharBlock()
    subheader = CharBlock()
    background = ImageChooserBlock()
    class Meta:
        template = 'pivot/headers/bottom_text_header.html'

class CenteredHeroBlock(StructBlock):
    header = CharBlock()
    subheader = CharBlock()
    text = TextBlock()
    background = ImageChooserBlock()
    class Meta:
        template = 'pivot/headers/centered_hero.html'

class CenteredPageHeaderBlock(StructBlock):
    header = CharBlock()
    subheader = CharBlock()
    text = TextBlock()
    background = ImageChooserBlock()
    class Meta:
        template = 'pivot/headers/centered_page_header.html'

class ComingSoonBannerBlock(StructBlock):
    header = CharBlock()
    note = CharBlock()
    background = ImageChooserBlock()
    class Meta:
        template = 'pivot/headers/coming_soon_banner.html'

class HeaderWithImageBlock(StructBlock):
    header = CharBlock()
    background = ImageChooserBlock()
    image = ImageChooserBlock()
    class Meta:
        template = 'pivot/headers/header_with_image.html'

class PageHeaderBlock(StructBlock):
    header = CharBlock()
    subheader = CharBlock()
    text = TextBlock()
    background = ImageChooserBlock()
    class Meta:
        template = 'pivot/headers/page_header.html'

class HeaderWithProblemsBlock(StructBlock):
    background = ImageChooserBlock()
    image = ImageChooserBlock()
    problems = ListBlock(
        StructBlock(
            [
                ('question', TextBlock()),
                ('answer', TextBlock()),
            ]
        )
    )
    class Meta:
        template = 'pivot/headers/header_with_problems.html'

# sections

# class SectionBlock(StructBlock):
#     anchor = CharBlock()

class CenteredTextBlock(StructBlock):
    header = CharBlock()
    subheader = CharBlock()
    text = TextBlock()
    class Meta:
        template = 'pivot/sections/centered_text.html'

class FullwidthMapBlock(StructBlock):
    google_map_url = URLBlock()
    class Meta:
        template = 'pivot/sections/fullwidth_map.html'

class GoogleFormBlock(StructBlock):
    google_form_url = URLBlock()
    class Meta:
        template = 'pivot/sections/google_form.html'

class InlineImageRightBlock(StructBlock):
    header = CharBlock()
    subheader = CharBlock()
    text = TextBlock()
    image = ImageChooserBlock()
    class Meta:
        template = 'pivot/sections/inline_image_right.html'

# class ProjectsContainedBlock(StructBlock):
#     pass

class StatCountersBlock(StructBlock):
    header = CharBlock()
    background = ImageChooserBlock()
    counters = ListBlock(
        StructBlock(
            [
                ('title', CharBlock()),
                ('number', CharBlock())
            ],
            template='pivot/sections/_stat_counter.html'
        ),
    )
    class Meta:
        template = 'pivot/sections/stat_counters.html'

class TextColumnsBlock(StructBlock):
    header = CharBlock()
    columns = ListBlock(
        StructBlock(
            [
                ('title', CharBlock()),
                ('text', RichTextBlock())
            ],
            template='pivot/sections/_text_column.html'
        )
    )
    class Meta:
        template = 'pivot/sections/text_columns.html'

class TextFeaturesBlock(StructBlock):
    columns = ListBlock(
        StructBlock(
            [
                ('title', CharBlock()),
                ('text', RichTextBlock())
            ],
            template='pivot/sections/_text_feature.html'
        )
    )
    class Meta:
        template = 'pivot/sections/text_features.html'

class TextOnImageBlock(StructBlock):
    header = CharBlock()
    text = TextBlock()
    background = ImageChooserBlock()
    image = ImageChooserBlock()
    class Meta:
        template = 'pivot/sections/text_on_image.html'

# pages

class PivotPage(Page):
    THEMES = (
        ('theme', 'Original'),
        ('theme-aquatica', 'Aquatica'),
        ('theme-aspirin', 'Aspirin'),
        ('theme-blues', 'Blues'),
        ('theme-buddha', 'Buddha'),
        ('theme-campfire', 'Campfire'),
        ('theme-cobalt', 'Cobalt'),
        ('theme-dusk', 'Dusk'),
        ('theme-eco', 'Eco'),
        ('theme-matte', 'Matte'),
        ('theme-mustang', 'Mustang'),
        ('theme-rocklobster', 'Rocklobster'),
        ('theme-sunset', 'Sunset'),
        ('theme-tronic', 'Tronic'),
        ('theme-zest', 'Zest')
    )
    
    theme = CharField(
        max_length=30,
        choices=THEMES,
        default='theme'
    )

    header = StreamField([
        ('bottom_text_header', BottomTextHeaderBlock()),
        ('centered_hero', CenteredHeroBlock()),
        ('centered_page_header', CenteredPageHeaderBlock()),
        ('coming_soon_banner', ComingSoonBannerBlock()),
        ('header_with_image', HeaderWithImageBlock()),
        ('header_with_problems', HeaderWithProblemsBlock()),
        ('page_header', PageHeaderBlock()),
    ], null=True, blank=True)

    body = StreamField([
        ('centered_text', CenteredTextBlock()),
        ('fullwidth_map', FullwidthMapBlock()),
        ('google_form', GoogleFormBlock()),
        ('inline_image_right', InlineImageRightBlock()),
        ('stat_counters', StatCountersBlock()),
        ('text_columns', TextColumnsBlock()),
        ('text_features', TextFeaturesBlock()),
        ('text_on_image', TextOnImageBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels+[
        StreamFieldPanel('header'),
        StreamFieldPanel('body')
    ]

    settings_panels = Page.settings_panels+[
        MultiFieldPanel(
            [
                FieldPanel('theme')
            ],
            heading='Design'
        )
    ]

# settings

@register_setting(icon='wagtail')
class SocialMediaSettings(BaseSetting):
    facebook = URLField(blank=True)
    instagram = URLField(blank=True)
    twitter = URLField(blank=True)
    class Meta:
        verbose_name = 'Social accounts'
