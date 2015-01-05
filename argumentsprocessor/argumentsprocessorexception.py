#!/usr/bin/env python


__author__ = 'James Johnson'

import rollbar

class ArgumentsProcessorException(Exception):
    def __init__(self, msg):
        rollbar.init('4c000b04f99c4fbf930db9ff1e845736', 'production')  # access_token, environment
        rollbar.report_message(msg, 'error')
        rollbar.report_exc_info()
        Exception.__init__(self, msg)


class ArgumentsProcessorExceptionArgumentsAreNone(ArgumentsProcessorException):

    def __init__(self):
        ArgumentsProcessorException.__init__(self, 'Arguments supplied to Arguments Processor may not be None')


class ArgumentsProcessorExceptionArgumentsAreInvalid(ArgumentsProcessorException):
    def __init__(self):
        ArgumentsProcessorException.__init__(self, 'supplied_arguments are not valid in reference to expected_arguments')