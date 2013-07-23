from webassets.filter import Filter
from webassets.filter import register_filter
from RequireOptimizer import RequireOptimizer


class RequireJSFilter(Filter):
    name = "requireJS"

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def unique(self):
        return self.args, self.kwargs

    def setup(self):
        pass

    def input(self, _in, out, **kwargs):
        source_path = kwargs.get('source_path')
        output_path = kwargs.get('output_path')
        out.write(RequireOptimizer.run_input_optimizer(source_path,
                                                       output_path,
                                                       **self.kwargs))

register_filter(RequireJSFilter)
