# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname paste

Name:           python-%{srcname}
Version:        3.11.0
Release:        %autorelease
Summary:        Tools for using a Web Server Gateway Interface stack
License:        MIT
URL:            https://github.com/pasteorg/paste
#!RemoteAsset:  sha256:c8e95401cbeb80c34bf832a5cd517fbaec7499225b334b2b24ba539a7f54e3ae
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# Exclude broken modules from import tests
# Also exclude paste.deploy, paste.auth.open_id & paste.mod
# As it requires additional dependencies
BuildOption(check):  -e 'paste.debug.*'
BuildOption(check):  -e paste.flup_session
BuildOption(check):  -e paste.transaction
BuildOption(check):  -e paste.util.scgiserver
BuildOption(check):  -e paste.deploy
BuildOption(check):  -e paste.auth.open_id
BuildOption(check):  -e paste.modpython

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# Tests
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
These provide several pieces of "middleware" (or filters) that can be nested
to build web applications.  Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.

%generate_buildrequires
%pyproject_buildrequires

# TODO: Tests require lots of pkg_resources usage
# Track this issue here: https://github.com/pasteorg/paste/pull/105
#check -a
# No internet access during tests
#pytest -W ignore::DeprecationWarning \
#    --deselect tests/test_cgiapp.py::test_form \
#    --deselect tests/test_httpserver.py::test_address_family_v4

%files -f %{pyproject_files}
%doc docs/*

%changelog
%autochangelog
