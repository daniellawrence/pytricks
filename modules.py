#!/usr/local/bin/python
import pickle as module_name
import types
#------------------------------------------------------------------------------
def get_docstrings():
    """ get all the docstrings for a module """
    docstrings = {}
    # loop over everything inside the module_name 
    for func_name in module_name.__dict__.keys():
        # grab an instance of the item
        func = module_name.__dict__[func_name]
        # check if the instance is a function
        if not isinstance(func, types.FunctionType ):
		continue
        # if it is then pull out the __doc__ and add it othe dict
        docstrings[ func_name ] = module_name.__dict__[func_name].__doc__
    return docstrings
#------------------------------------------------------------------------------
def get_functions():
    """ get all the functions for a module """
    function_list = []
    # loop over everything inside the module_name 
    for func_name in module_name.__dict__.keys():
        # grab an instance of the item
        func = module_name.__dict__[func_name]
        # check if the instance is a function
        if not isinstance(func, types.FunctionType ):
		continue
        # if it is then append it to our list
        function_list.append(func_name)
    return function_list

if __name__ == "__main__":
    print get_docstrings()
    print get_functions()
