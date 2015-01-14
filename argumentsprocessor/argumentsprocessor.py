#!/usr/bin/env python

"""
    ArgumentsProcessor Module

    Processes arguments according to a supplied dictionary containing expected arguments
    and rules.

    @includes:
        ArgumentsProcessor
        ArgumentsProcessorExceptions

    @requires:
        'expected_arguments' = {   -- categories are synonymous to the arguments you pass
            'category_a' : { -- this is will be whatever you name your argument, see the example below
                'arguments: (
                    'hello',
                    'bye'
                ),
                'required' : True || False,
                'returns' : 'string' -- default is string but you may pass the string name of any
                   python variable type or pass in a custom object
            },
            'category_b' : {
                arguments: (
                    'data'
                ),
                'required' : True || False,
                'returns': 'string' -- default is string but you may pass the string name of any
                   python variable type or pass in a custom object
            }
        }

    @return:
        arguments = {
            'category_a':return_value, -- either the default string, any python type, or custom object passed in
            'category_b':return_value, -- either the default string, any python type, or custom object passed in
         }


    @example:

    import ArgumentsProcessor

    class classy:

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

        def __init__(self, mode, data):
            supplied_arguments = {
                'mode':mode,
                'data':data
            }
            arguments = ArgumentsProcessor(self.expected_arguments, supplied_arguments)
            print('mode is' arguments['mode']


    @copyright: James Johnson 2014
    @license: MIT, see license file
"""

from argumentsprocessor.argumentsprocessorexception import *

class ArgumentsProcessor(object):
    """
    ArgumentsProcessor
    @description: Receives a dictionary of dictionaries containing supplied_arguments and
        processes them against the supplied expected_arguments, returning a dictionary of the
        processed arguments.

    @requires: expected_arguments, supplied_arguments
    @return: (default)string, python builtin type, or supplied object -- supplied object must be able to process the data
        passed to in on init
    @raise: ArgumentsProcessorException
    """

    __author__ = 'James Johnson'
    __version__ = '1.1.5'

    supplied_arguments = {}
    expected_arguments = {}
    rules = {}
    return_arguments = {}

    def __init__(self, expected_arguments, supplied_arguments):
        self.return_arguments = self.process(expected_arguments, supplied_arguments)

    def process(self, expected_arguments, supplied_arguments):
        self.check_arguments(expected_arguments, supplied_arguments)
        if self.validate_supplied_arguments() is not True:
            raise ArgumentsProcessorExceptionArgumentsAreInvalid()
        else:
            self.process_arguments()
            return self.return_arguments

    def check_arguments(self, expected_arguments, supplied_arguments):
        self.check_expected_arguments(expected_arguments)
        self.check_supplied_arguments(supplied_arguments)

    def check_expected_arguments(self, expected_arguments):
        if expected_arguments is None:
            raise ArgumentsProcessorExceptionArgumentsAreNone()
        else:
            self.expected_arguments = expected_arguments

    def check_supplied_arguments(self, supplied_arguments):
        if supplied_arguments is None:
            raise ArgumentsProcessorExceptionArgumentsAreNone()
        else:
            self.supplied_arguments = supplied_arguments

    def validate_supplied_arguments(self):
     #TODO: break into 3 functions, needs to handle not required items but will not add items not expected
        for (expected_argument_key, expected_argument_value) in self.expected_arguments.items():
            if expected_argument_key in self.supplied_arguments:
                # TODO: add check if value is valid
            elif self.is_required(expected_argument_value):
                raise ArgumentsProcessorExceptionArgumentsAreInvalid()
                return False
            else:

    def is_required(self, expected_argument_value):
        return expected_argument_value['required']

    def validate_supplied_argumentsx(self):
        for (expected_argument_key, expected_argument_value) in self.expected_arguments.items():
            for (supplied_argument_key, supplied_argument_value) in self.supplied_arguments.items():
                if supplied_argument_key != expected_argument_key:
                    return False
                else:
                    if self.validate_by_rules(expected_argument_value, supplied_argument_value):
                        return True

    def validate_by_rules(self, expected_argument_value, supplied_argument_value):
        if self.is_required(expected_argument_value):
            if self.check_supplied_argument_value_is_not_none_or_empty(supplied_argument_value):
                return True
            else:
                return False
        else:
            return False

    def check_supplied_argument_value_is_not_none_or_empty(self, supplied_argument_value):
        if supplied_argument_value is None:
            return False
        if supplied_argument_value == '':
            return False
        return True

    def process_arguments(self):
        for expected_argument_key in self.expected_arguments:
            self.return_arguments[expected_argument_key] = self.supplied_arguments[expected_argument_key]
