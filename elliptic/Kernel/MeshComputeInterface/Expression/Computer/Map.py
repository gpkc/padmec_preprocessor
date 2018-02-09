from .Computer import Computer


class Map(Computer):

    def __init__(self, function: str, **fkwargs):
        super().__init__()

        self.function = function
        self.fkwargs = fkwargs

        fkwargs_str = ""
        for k, v in fkwargs.items():
            fkwargs_str = fkwargs_str + '\n' + k + "=" + str(v)
        self.name = "Map " + function + fkwargs_str

    def render(self, template_manager, child, backend_builder) -> str:
        template_file = backend_builder.map()
        template = template_manager.get_template(template_file)

        rendered_template = template.render(function=self.function,
                                            fargs=self.fkwargs.items(),
                                            child=child)

        return rendered_template


class GetScalarField(Map):
    # TODO: FixMe! This is depending on MOAB!
    class TagArg:
        def __init__(self, field_name):
            self.var_name = field_name + "_TAG"

        def __repr__(self):
            return self.var_name

    def __init__(self, field_name):
        super().__init__("get_field", tag_handle=GetScalarField.TagArg(field_name))

        self.field_name = field_name


class PutScalar(Map):

    def __init__(self, value):
        super().__init__("put_scalar", value=value)


class GetCentroid(Map):

    def __init__(self):
        super().__init__("get_centroid")


class NormDist(Map):

    def __init__(self, other):
        super().__init__("norm_dist", other=other.unique_id)


class ScalarProd(Map):

    def __init__(self, other):
        super().__init__("scalar_prod", other=other.unique_id)


class ScalarSum(Map):

    def __init__(self, other):
        super().__init__("scalar_sum", other=other.unique_id)


class ScalarDiv(Map):

    def __init__(self, other):
        super().__init__("scalar_div", other=other.unique_id)
