ArgumentsProcessor
==================
[![Build Status](https://travis-ci.org/excellentingenuity/argumentsprocessor.svg?branch=master)](https://travis-ci.org/excellentingenuity/argumentsprocessor)
[![Coverage Status](https://img.shields.io/coveralls/excellentingenuity/argumentsprocessor.svg)](https://coveralls.io/r/excellentingenuity/argumentsprocessor)
[![PyPI version](https://badge.fury.io/py/argumentsprocessor.svg)](http://badge.fury.io/py/argumentsprocessor)
[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=jsam84&url=https://github.com/excellentingenuity/argumentsprocessor&title=argumentsprocessor&language=GH_PROJECT_PROG_LANGUAGE&tags=github&category=software)
![Excellnt InGenuity LLC](data:image/png;base64,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)

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

