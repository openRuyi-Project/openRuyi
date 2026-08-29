# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pecan

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        WSGI object-dispatching web framework
License:        BSD-3-Clause
URL:            https://github.com/pecan/pecan
VCS:            git:https://github.com/pecan/pecan.git
#!RemoteAsset:  sha256:2f9fbcea86e8dbf1a2d28954225547634a289db7201e7764516a5dce86c116de
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# pecan.tests imports webtest, which openRuyi does not package
BuildOption(check):  -e 'pecan.tests*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A WSGI object-dispatching web framework, designed to be lean and fast
with few dependencies and easy-to-use tools. Pecan was created to fill
a void in the Python web-framework world: a very lightweight framework
that provides object-dispatch style routing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/gunicorn_pecan
%{_bindir}/pecan

%changelog
%autochangelog
