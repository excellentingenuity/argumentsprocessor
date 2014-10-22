#!/usr/bin/env python

from nose.tools import *

from argumentsprocessor.argumentsprocessor import ArgumentsProcessor
from argumentsprocessor.argumentsprocessorexception import *

expected_arguments = {
            'mode': {
                'arguments': (
                    'encrypt',
                    'decrypt'
                ),
                'required': True,
                'return': 'string'
            },
            'data': {
                'arguments': (
                    'data'
                ),
                'required': True,
                'return': 'string'
            }
        }
supplied_arguments = {'mode':'encrypt', 'data':'data'}

expected_return = {
    'mode':'encrypt',
    'data':'data'
}

def test_init_object_with_None():
    assert_raises(TypeError, ArgumentsProcessor)
    assert_raises(ArgumentsProcessorExceptionArgumentsAreNone, ArgumentsProcessor, None, None)

def test_init_object():
    temp_processor = ArgumentsProcessor(expected_arguments, supplied_arguments)
    assert isinstance(temp_processor, ArgumentsProcessor)

def test_arguments_processor():
    temp_processor = ArgumentsProcessor(expected_arguments, supplied_arguments)
    assert temp_processor.return_arguments == expected_return

def test_arguments_are_invalid():
    assert_raises(ArgumentsProcessorExceptionArgumentsAreInvalid, ArgumentsProcessor, expected_arguments, {'mode':'encrypt', 'data':''})