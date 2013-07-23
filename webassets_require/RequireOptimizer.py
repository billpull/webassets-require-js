import os
import subprocess
from webassets.exceptions import FilterError

class OptimizationError(Exception):
    pass

class RequireOptimizer(object):
    
    __REQUIRE_RESOURCES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "lib"))

    @staticmethod
    def _resource_path(file):
        """ Return the Path to a Resource """
        return os.path.join(RequireOptimizer.__REQUIRE_RESOURCES_DIR, file)

    @staticmethod
    def run_input_optimizer(source_path, output_path, **kwargs):
        """ Run Optimizer Command and return file """

        if not source_path.endswith(".js"):
            raise FilterError('requireJS: bundle file is not a js-file')

        base_url = kwargs.get('base_url', './')

        # Use the provided name or calculate the name relative to the base_url and minus the ".js"-part
        working_dir = os.getcwd()
        relpath = os.path.relpath(source_path, working_dir)
        name = kwargs.get('name', os.path.relpath(relpath, base_url)[:-3])

        # Any extra args that should be provided to r.js
        extra_arg_string = ""
        extra_args = kwargs.get("extra_args",{})
        for key, value in extra_args.iteritems():
            extra_arg_string += "%s=%s " % (key, value)

        compiler_cmd = "java -classpath %s:%s org.mozilla.javascript.tools.shell.Main %s -o baseUrl=%s name=%s out=%s %s" % (
                                                RequireOptimizer._resource_path("js.jar"),
                                                RequireOptimizer._resource_path("compiler.jar"),
                                                RequireOptimizer._resource_path("r.js"),
                                                base_url,
                                                name,
                                                output_path,
                                                extra_arg_string
        )

        # Run the compiler.
        try:
            os.system(compiler_cmd)

            fo = open(output_path, "r+")

            return fo.read()
        except:
            return ''