# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname legacy-cgi
%global pypi_name legacy_cgi

Name:           python-%{srcname}
Version:        2.6.4
Release:        %autorelease
Summary:        Fork of the standard library cgi and cgitb modules
License:        PSF-2.0
URL:            https://github.com/jackrosenthal/legacy-cgi
VCS:            git:https://github.com/jackrosenthal/legacy-cgi.git
#!RemoteAsset:  sha256:abb9dfc7835772f7c9317977c63253fd22a7484b5c9bbcdca60a29dcce97c577
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l cgi cgitb

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a fork of the standard library modules cgi and cgitb, which were
removed in Python 3.13. The aim is to provide a drop-in replacement for
code that still depends on these modules.

%prep -a
# Upstream shebang #!/usr/local/bin/python would become an unsatisfiable
# auto-Requires; point it at the system interpreter.
%py3_shebang_fix cgi.py cgitb.py

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
