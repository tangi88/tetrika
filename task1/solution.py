import inspect


def strict(func):
    def wrapper(a, b, *args, **kwargs):
        params_func = locals()
        signature_func = inspect.signature(func)

        for parameter in signature_func.parameters.items():
            name_parameter, type_parameter = parameter

            if type_parameter.annotation is type_parameter.empty:
                continue

            if (type_parameter.kind == type_parameter.POSITIONAL_OR_KEYWORD) or \
                (type_parameter.kind == type_parameter.KEYWORD_ONLY and type_parameter.default is type_parameter.empty):

                if not type(params_func[name_parameter]) is type_parameter.annotation:
                    raise TypeError

            elif type_parameter.kind == type_parameter.VAR_POSITIONAL:
                if any(not type(p) is type_parameter.annotation for p in params_func[name_parameter]):
                    raise TypeError

        res = func(a, b, *args, **kwargs)

        if not type(res) is signature_func.return_annotation:
            raise TypeError

        return res

    return wrapper

