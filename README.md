ArgumentsProcessor
==================
[![Build Status](https://travis-ci.org/excellentingenuity/argumentsprocessor.svg?branch=master)](https://travis-ci.org/excellentingenuity/argumentsprocessor)
[![Coverage Status](https://img.shields.io/coveralls/excellentingenuity/argumentsprocessor.svg)](https://coveralls.io/r/excellentingenuity/argumentsprocessor)
[![PyPI version](https://badge.fury.io/py/argumentsprocessor.svg)](http://badge.fury.io/py/argumentsprocessor)
[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=jsam84&url=https://github.com/excellentingenuity/argumentsprocessor&title=argumentsprocessor&language=GH_PROJECT_PROG_LANGUAGE&tags=github&category=software)

A Python module that process a dictionary of arguments against a supplied dictionary of expected arguments.

**Install**

`pip install argumentsprocessor`


**Documentation**

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


    @copyright: James Johnson, Excellent InGenuity LLC, 2014
    @license: BSD New, see license file

