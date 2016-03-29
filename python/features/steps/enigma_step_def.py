from behave import *
from nose.tools import eq_

from enigma import Enigma


@given('an enigma')
def step_impl(context):
    context.enigma = Enigma()


@given(u'an enigma that uses the reflector')
def step_impl(context):
    if not hasattr(context, 'enigma'):
        context.enigma = Enigma()

@given(u'an enigma that uses the reflector and leftmost rotor')
def step_impl(context):
    if not hasattr(context, 'enigma'):
        context.enigma = Enigma()

@given(u'an enigma that uses the reflector, and left and center rotors')
def step_impl(context):
    if not hasattr(context, 'enigma'):
        context.enigma = Enigma()

@given(u'a reflector "{reflector}"')
def step_impl(context, reflector):
    if not hasattr(context, 'enigma'):
        context.enigma = Enigma()
    context.enigma.reflector = reflector

@given(u'a reflector "{reflector}";')
def step_impl(context, reflector):
    if not hasattr(context, 'enigma'):
        context.enigma = Enigma()
    context.enigma.reflector = reflector

@given(u'center rotor "{centerRotor}";')
def step_impl(context, centerRotor):
    print('*****************centerRotor:'+centerRotor)
    if not hasattr(context, 'enigma'):
        context.enigma = Enigma()
    context.enigma.centerRotor = centerRotor

@given(u'leftmost rotor "{leftRotor}";')
def step_impl(context, leftRotor):
    if not hasattr(context, 'enigma'):
        context.enigma = Enigma()
    context.enigma.leftRotor = leftRotor


# Apparently behave can't recognize "" as text of zero length
@when('an operator encrypts ""')
def step_impl(context):
    context.result = context.enigma.encrypt(message='')


@then('the result is ""')
def step_impl(context):
    eq_('', context.result)


@when('an operator encrypts "{text}"')
def step_impl(context, text):
    context.result = context.enigma.encrypt(text)


@then('the result is "{text}"')
def step_impl(context, text):
    eq_(text, context.result)
