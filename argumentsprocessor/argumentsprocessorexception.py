#!/usr/bin/env python


__author__ = 'James Johnson'


class ArgumentsProcessorException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class ArgumentsProcessorExceptionArgumentsAreNone(ArgumentsProcessorException):

    def __init__(self):
        ArgumentsProcessorException.__init__(self, 'Arguments supplied to Arguments Processor may not be None')


class ArgumentsProcessorExceptionArgumentsAreInvalid(ArgumentsProcessorException):
    def __init__(self):
        ArgumentsProcessorException.__init__(self, 'supplied_arguments are not valid in reference to expected_arguments')