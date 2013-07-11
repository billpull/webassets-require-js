from webassets.filter import Filter
from webassets.filter import register_filter

class RequireJSFilter(Filter):
    name = "requireJS"
    
    def output(self, _in, out, **kwargs):
        out.write(_in.read())

register_filter(RequireJSFilter) 