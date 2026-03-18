# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hypothesis

Name:           python-%{srcname}
Version:        6.151.9
Release:        %autorelease
Summary:        Library for property based testing
License:        MPL-2.0
URL:            https://github.com/HypothesisWorks/hypothesis
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} '_%{srcname}_*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3-devel
BuildRequires:  python3dist(sortedcontainers)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%{pyproject_extras_subpkg -n python%{python3_pkgversion}-hypothesis pytz,dateutil,lark,numpy,pandas,pytest,redis,zoneinfo,cli,ghostwriter,django,codemods}

%description
Flask-RESTful provides the building blocks for creating a REST API.

%generate_buildrequires
%pyproject_buildrequires

%check

%files -f %{pyproject_files}
%{_bindir}/hypothesis

%changelog
%{?autochangelog}
