OMERO Python Dependencies
=========================

[![Build Status](https://travis-ci.org/openmicroscopy/ansible-role-omero-python-deps.svg)](https://travis-ci.org/openmicroscopy/ansible-role-omero-python-deps)
[![Ansible Role](https://img.shields.io/ansible/role/14771.svg)](https://galaxy.ansible.com/openmicroscopy/omero-python-deps/)

Python dependencies for OMERO.

OMERO depends on several Python modules, they should be installed from distribution packages.

Dependencies
------------

Requires the EPEL repository for CentOS (automatically setup by the `basedeps` role).
For RHEL7, it requires rhel-7-server-optional-rpms. This role does not install the Ice Python module.


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
