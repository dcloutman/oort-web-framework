import re
import bleach
from .. initialize import flask_app

@flask_app.template_filter()
def hpassage(value):
    """HTML Passage
    Single line strings. Permits essential text styling markup only.

    Only allows <strong> and <em> tags.
    """
    return bleach.clean(value, ['strong', 'em'])

@flask_app.template_filter()
def hsdoc( value):
    """HTML Simple Document
    Simple documents, like comments or brief articles. Use when keeping a close reign on your formatting.

    Only allows <strong>, <em>, <br>, <p>, <h2>, and <h3> tags.
    """
    return bleach.clean(value, ['strong', 'em', 'br', 'p', 'h2', 'h3', 'ul', 'ol', 'li'])

@flask_app.template_filter()
def hidoc(value):
    """HTML Intermediate Document
    Moderately complex documents, like pages or blog posts. Use when keeping a close reign on your formatting.

    Only allows <strong>, <em>, <br>, <p>, and <h1>-<h6> tags.
    """
    return bleach.clean(value, ['header', 'strong', 'em', 'br', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'aside', 'section', 'blockquote', 'pre', 'code'])
