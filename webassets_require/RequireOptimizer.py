import os
import subprocess

class OptimizationError(Exception):

    pass

class RequireOptimizer(object):
    
    __REQUIRE_RESOURCES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "resources"))
    
    @staticmethod
    def _resource_path(file):
        """ Return the Path to a Resource """
        return os.path.join(RequireOptimizer.__REQUIRE_RESOURCES_DIR, file)
    
    @staticmethod
    def _load_environment():
        """ Load Rhino Environment """
        # Start of the command to run the compiler in Java.
        return [
            "java",
            "-classpath",
            ":".join((
                RequireOptimizer._resource_path("js.jar"),
                RequireOptimizer._resource_path("compiler.jar"),
            )),
            "org.mozilla.javascript.tools.shell.Main"
        ]
    
    @staticmethod
    def run_optimizer(*args, **kwargs):
        """ Run Optimizer Command and return file """
        compiler = RequireOptimizer._load_environment()
        
        compiler.extend([RequireOptimizer._resource_path("r.js"), "-o"])
        compiler.extend(args)

        compiler.extend(
            "{0}={1}".format(
                key, value
            )
            for key, value
            in kwargs.items()
        )
        # Run the compiler in a subprocess.
        if subprocess.call(compiler) != 0:
            raise OptimizationError("Error while running r.js optimizer.")