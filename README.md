webassets-require-js
====================

A webassets filter for require js optimizer.
This fork adds support for:
- File with dependencies. Gives r.js access to the original source file, so that it can follow and include dependencies.
- No more hardcoded output. Instead the output path from the webassets bundle-definition is used.
- Specifying base_url explicitly. If no base_url is set, "./" is used instead.
- Specifying name parameter to r.js explicitly. If no name option is provided, the filter will now figure out the name based on the source path and the current working dir.
- Passing additional arguments to r.js from the webassets bundle-definition. These arguments will be passed directly to r.js.

Example usage:
from webassets_require import RequireJSFilter

start_page_js = Bundle('js/pages/start_page.js',
                       filters=RequireJSFilter(base_url='app/assets/js/',
                                               extra_args={"mainConfigFile": "app/assets/js/config.js",
                                                           "exclude": "common",
                                                           "findNestedDependencies": "true",
                                                           "optimize": "uglify2",
                                                           "pragmas.isBuild": "true"}),
                       output="static/js/pages/start_page.js")

Most of the work done by Naycon (https://github.com/Naycon).
Branch maintaned by Zwant (https://github.com/Zwant)