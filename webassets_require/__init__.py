from webassets.filter import Filter
from webassets.filter import register_filter
from RequireOptimizer import RequireOptimizer

class RequireJSFilter(Filter):
    name = "requireJS"
    
    def output(self, _in, out, **kwargs):
    	output_path = kwargs.get('output_path')

    	RequireOptimizer.configure_optimizer(output_path, _in.read())

        out.write(RequireOptimizer.run_optimizer())

register_filter(RequireJSFilter) 