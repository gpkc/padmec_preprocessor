from elliptic.Kernel.MeshComputeInterface.Expression import StatementRoot
from elliptic.Kernel.MeshComputeInterface.Expression.Selector.Dilute import ByEnt
from elliptic.Kernel.TreeBuilder import TreeBuild


class TestTemplateManagerBase:

    def test_template(self, template_manager):
        rendered_template = template_manager.render('test_template', a='x', b='y')

        assert rendered_template == 'x y'


class TestTreeBuilder:

    def test_render_single_node(self, template_manager, simple_backend_builder):
        tree_builder = TreeBuild(template_manager, simple_backend_builder)
        statement_root = StatementRoot()

        built_module = tree_builder.build(statement_root)

        assert built_module.test_fun() == 'x a'

    def test_render_two_node(self, template_manager, simple_backend_builder):
        tree_builder = TreeBuild(template_manager, simple_backend_builder)
        statement_root = StatementRoot()
        statement_root.children = (ByEnt(2),)

        built_module = tree_builder.build(statement_root)

        assert built_module.test_fun() == 'x a2'