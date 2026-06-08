# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cheroot

Name:           python-%{srcname}
Version:        11.1.2
Release:        %autorelease
Summary:        Highly-optimized, pure-python HTTP server
License:        BSD-3-Clause
URL:            https://cheroot.cherrypy.dev/
VCS:            git:https://github.com/cherrypy/cheroot.git
#!RemoteAsset:  sha256:bfb70c49663f63b0440f2b54dbc6b0d1650e56dfe4e2641f59b2c6f727b44aca
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l cheroot +auto
# cheroot.test* and cheroot.testing import pytest, which is not packaged
BuildOption(check):  -e 'cheroot.test*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Cheroot is the high-performance, pure-Python HTTP server used by CherryPy.
It can be used as a generic, production-ready WSGI server.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.md

%changelog
%autochangelog
