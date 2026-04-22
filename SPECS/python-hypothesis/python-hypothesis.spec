# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hypothesis

Name:           python-%{srcname}
Version:        6.148.6
Release:        %autorelease
Summary:        Library for property based testing
License:        MPL-2.0
URL:            https://github.com/HypothesisWorks/hypothesis
#!RemoteAsset:  sha256:0ef1381f893650590f2c5918318d4c8240c79e481bbb621a49acc3dba868d80f
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} '_%{srcname}_*'
# We don't have python-libcst
BuildOption(check):  -e hypothesis.extra.codemods
# We don't have python-dpcontracts
BuildOption(check):  -e hypothesis.extra.dpcontracts
# We don't have python-black
BuildOption(check):  -e hypothesis.extra.ghostwriter
# We don't have python-lark
BuildOption(check):  -e hypothesis.extra.lark
# Test won't run even with django installed, so skip it
BuildOption(check):  -e hypothesis.extra.django
BuildOption(check):  -e hypothesis.extra.pandas
BuildOption(check):  -e 'hypothesis.extra.pandas.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# For tests
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(redis)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Flask-RESTful provides the building blocks for creating a REST API.

%pyproject_extras_subpkg -n python-hypothesis pytz,dateutil,lark,numpy,pandas,pytest,redis,zoneinfo,cli,ghostwriter,django,codemods

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/hypothesis

%changelog
%autochangelog
