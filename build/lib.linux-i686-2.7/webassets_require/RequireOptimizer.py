import os
import subprocess

class OptimizationError(Exception):

    pass

class RequireOptimizer(object):
    
    __REQUIRE_RESOURCES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "lib"))
    __OUTPUT_FILE_PATH = ''
    __INPUT_FILE_MODULE = ''
    __TMP_INPUT_FILE_NAME = 'main.js'

    @staticmethod
    def _resource_path(file):
        """ Return the Path to a Resource """
        return os.path.join(RequireOptimizer.__REQUIRE_RESOURCES_DIR, file)
    

    @staticmethod
    def _create_tmp_input_file(path, contents):
        file_path = "%s/%s" % (path, RequireOptimizer.__TMP_INPUT_FILE_NAME)

        file = open(file_path, 'w')

        file.write("define(function(require) {\n")
        file.write(contents)
        file.write("});")

        file.close()

        RequireOptimizer.__INPUT_FILE_MODULE = "/assets/%s" % RequireOptimizer.__TMP_INPUT_FILE_NAME[:-3]


    @staticmethod
    def configure_optimizer(output_path, input_contents):
        input_path = os.path.abspath(os.path.join(os.path.dirname(output_path), '..'))

        RequireOptimizer._create_tmp_input_file(input_path, input_contents)

        RequireOptimizer.__OUTPUT_FILE_PATH = output_path

    
    @staticmethod
    def run_optimizer(*args, **kwargs):
        """ Run Optimizer Command and return file """

        compiler_cmd = "java -classpath %s:%s org.mozilla.javascript.tools.shell.Main %s -o name=%s out=%s baseUrl=." % (
                                                    RequireOptimizer._resource_path("js.jar"),
                                                    RequireOptimizer._resource_path("compiler.jar"),
                                                    RequireOptimizer._resource_path("r.js"),
                                                    RequireOptimizer.__INPUT_FILE_MODULE,
                                                    RequireOptimizer.__OUTPUT_FILE_PATH
                                                )

        # Run the compiler.
        try:
            os.system(compiler_cmd)

            fo = open(RequireOptimizer.__OUTPUT_FILE_PATH, "r+")

            return fo.read()
        except:
            return ''
