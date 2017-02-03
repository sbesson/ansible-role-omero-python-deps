OMERO Python Dependencies
=========================

Python dependencies for OMERO.

OMERO depends on several Python modules, they should be installed from distribution packages.


In addition you can choose to install all recommended Python dependencies or a minimal subset which should allow OMERO to run, but with reduced functionality.
For example, if you are running OMERO.web standalone you may not need all dependencies.


Most users should use the defaults.


Dependencies
------------

Requires the EPEL repository (automatically setup by the `basedeps` role).
This role does not install the Ice Python module.


Role Variables
--------------

Optional variables:
- `omero_python_deps_recommended`: If `False` install a minimal set of Python dependencies, default `True`.


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
