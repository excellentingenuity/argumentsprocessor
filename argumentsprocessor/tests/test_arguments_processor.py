#!/usr/bin/env python

from nose.tools import *

from argumentsprocessor.argumentsprocessor import ArgumentsProcessor
from argumentsprocessor.argumentsprocessorexception import *
from argumentsprocessor import rollbar_cfg as rollbar_cfg

rollbar_cfg.environment = 'development'

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
expected_arguments_not_required = {
            'mode': {
                'arguments': (
                    'encrypt',
                    'decrypt'
                ),
                'required': False,
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

def test_supplied_arguments_are_none():
    assert_raises(ArgumentsProcessorExceptionArgumentsAreNone, ArgumentsProcessor, expected_arguments, None)

def test_matching_expected_and_supplied_keys_exception():
    bad_arguments = {'day':'monday', 'data':'hello'}
    assert_raises(
        ArgumentsProcessorExceptionArgumentsAreInvalid,
        ArgumentsProcessor,
        expected_arguments,
        bad_arguments
    )

def test_matching_expected_and_supplied_keys_true():
    temp_processor = ArgumentsProcessor(expected_arguments, supplied_arguments)
    temp_arguments = temp_processor.return_arguments
    assert temp_arguments == supplied_arguments
    assert temp_arguments == expected_return

def test_matching_expected_and_supplied_keys_not_required_true():
    temp_processor = ArgumentsProcessor(expected_arguments_not_required, supplied_arguments)
    temp_arguments = temp_processor.return_arguments
    assert temp_arguments == supplied_arguments
    assert temp_arguments == expected_return

def test_extra_arguments_not_included():
    extra_arguments = {
        'mode':'encrypt',
        'data':'data',
        'year': '2015'
    }
    temp_processor = ArgumentsProcessor(expected_arguments, extra_arguments)
    temp_arguments = temp_processor.return_arguments
    assert temp_arguments == supplied_arguments
    assert temp_arguments == expected_return

def test_rollbar_cfg_token():
    assert rollbar_cfg.token == '4c000b04f99c4fbf930db9ff1e845736'


def test_rollbar_cfg_env():
    assert rollbar_cfg.environment == 'development'