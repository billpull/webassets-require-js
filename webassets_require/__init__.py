from webassets.filter import Filter
from webassets.filter import register_filter
from RequireOptimizer import RequireOptimizer
import tempfile
import shutil


class RequireJSFilter(Filter):
    name = "requireJS"

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def unique(self):
        return [self.args].extend([(k, v) for (k, v) in self.kwargs.items()])

    def setup(self):
        pass

    def input(self, _in, out, **kwargs):
        tmp_folder = tempfile.mkdtemp(prefix='webassets_require_')
        tmp_output_path = '{tmp_folder}/optimized_file.js'.format(tmp_folder=tmp_folder)
        
        source_path = kwargs.get('source_path')
        out.write(RequireOptimizer.run_input_optimizer(source_path,
                                                       tmp_output_path,
                                                       **self.kwargs))
        
        shutil.rmtree(tmp_folder)

register_filter(RequireJSFilter)
