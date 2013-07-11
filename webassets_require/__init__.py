from webassets.filter import Filter
from webassets.filter import register_filter

class RequireJSFilter(Filter):
    name = "requireJS"
    
    def output(self, _in, out, **kwargs):
        #TODO:
        #   - read input file
        #   - run require JS command
        #   - return result from command
        #   - handle options
        #   - handle debug mode
        out.write(_in.read())

register_filter(RequireJSFilter) 