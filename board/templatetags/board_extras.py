from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter(needs_autoescape=True)
def doublearrowquotes(text, autoescape=None):  # la re matcha cose come >>1234
    return applyFunctionToMatches(text, r'(>>\d+)', lambda x: '<a href="/' + x + '" >' + x + '</a>', autoescape)


# #todo fixme e quant'altro. NON FUNZIONA
@register.filter(needs_autoescape=True) # da cambiare re in [<p>/<br>/^][simbolo di > in html][stringa]
def singlearrowquotes(text, autoescape=None):  # la re matcha cose tipo "[inizio o \s]>testo quotato[interrotto da \n]"
    return applyFunctionToMatches(text, r'[\s\A](>[^>][^\n$]*)', lambda x: '<p style="color:green;">' + x + '</p>', autoescape)


#prende il testo da modificare, una re, una funzione e autoescape
#applica la funzione a tutte le occorrenze della re SENZA FARE L'ESCAPE
#ed escapizza il resto.
#Ritorna una stringa sicura
def applyFunctionToMatches(text, exp, function, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    result = ''
    for t in re.split(exp, text):
        if t in re.findall(exp, text):
            result += function(t)
        else:
            result += esc(t)

    return mark_safe(result)