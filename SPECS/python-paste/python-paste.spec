# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname paste

Name:           python-%{srcname}
Version:        3.10.1
Release:        %autorelease
Summary:        Tools for using a Web Server Gateway Interface stack
License:        MIT
URL:            https://github.com/pasteorg/paste
#!RemoteAsset:  sha256:1c3d12065a5e8a7a18c0c7be1653a97cf38cc3e9a5a0c8334a9dd992d3a05e4a
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

%check -a
# No internet access during tests
%pytest -W ignore::DeprecationWarning \
    --deselect tests/test_cgiapp.py::test_form \
    --deselect tests/test_httpserver.py::test_address_family_v4

%files -f %{pyproject_files}
%doc docs/*
# Why this file?
%{python3_sitelib}/Paste-%{version}-py*-nspkg.pth

%changelog
%autochangelog
