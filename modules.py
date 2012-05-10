#!/usr/local/bin/python
import pickle as module_name
import types
#------------------------------------------------------------------------------
def get_docstrings():
    """ get all the docstrings for a module """
    docstrings = {}
    for func_name in module_name.__dict__.keys():
        func = module_name.__dict__[func_name]
        if not isinstance(func, types.FunctionType ):
		continue
        docstrings[ func_name ] = module_name.__dict__[func_name].__doc__
    return docstrings
#------------------------------------------------------------------------------
def get_functions():
    """ get all the functions for a module """
    function_list = []
    for func_name in module_name.__dict__.keys():
        func = module_name.__dict__[func_name]
        if not isinstance(func, types.FunctionType ):
		continue
        function_list.append(func_name)
    return function_list

if __name__ == "__main__":
    print get_docstrings()
    print get_functions()
