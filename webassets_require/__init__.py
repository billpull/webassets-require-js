from webassets.filter import Filter
from webassets.filter import register_filter
from RequireOptimizer import RequireOptimizer

class RequireJSFilter(Filter):
    name = "requireJS"
    
    def output(self, _in, out, **kwargs):
        raise Exception(_in.read())
        out.write(RequireOptimizer.run_optimizer(_in.read()))

register_filter(RequireJSFilter) 