from anytree import NodeMixin
from typing import Dict, Any, Type


class EllipticNode(NodeMixin):

    last_id: int = 0

    def __init__(self) -> None:
        super().__init__()

        self.name: str

        self.unique_id = EllipticNode.last_id
        EllipticNode.last_id += 1

    def _name_func(self) -> str:
        return str(self.unique_id) + '\n' + self.name

    def _shape(self) -> str:
        return "shape=box"

    def export_tree(self, filename: str) -> None:
        from anytree.exporter import DotExporter

        exporter = DotExporter(self.root,
                               nodenamefunc=lambda node: node._name_func(),
                               nodeattrfunc=lambda node: node._shape())

        exporter.to_picture(filename)

    def render(self, template_manager, child: str, backend_builder) -> str:
        return child
        #raise NotImplementedError


class ExpressionBase(EllipticNode):

    def __init__(self) -> None:
        super().__init__()

    def __call__(self,
                 expr_type: Type['ExpressionBase'],
                 **kwargs) -> 'ExpressionBase':
        expr = expr_type(**kwargs)

        self.children += (expr,)

        return expr


class StatementRoot(EllipticNode):

    def _shape(self) -> str:
        return "shape=doubleoctagon"

    def __init__(self) -> None:
        super(StatementRoot, self).__init__()
        self.name = "stmt_root"

    def __call__(self,
                 expr_type: Type[ExpressionBase],
                 **kwargs) -> 'ExpressionBase':
        expr = expr_type(**kwargs)

        self.children += (expr,)

        return expr

    def render(self, template_manager, child, backend_builder) -> str:
        template_file = backend_builder.base()
        template = template_manager.get_template(template_file)

        rendered_template = template.render(child=child)

        return rendered_template
