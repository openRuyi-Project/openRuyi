# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nipype

%bcond tests 0

Name:           python-%{srcname}
Version:        1.10.0
Release:        %autorelease
Summary:        Neuroimaging in Python: Pipelines and Interfaces
License:        Apache-2.0
URL:            https://github.com/nipy/nipype
#!RemoteAsset:  sha256:19e5d6cefa70997198f78bc665ef4d3d3cb53325b5b98a72e51aefadaf6b3e0e
Source:         https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(simplejson)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(rdflib)
BuildRequires:  python3dist(acres)
BuildRequires:  python3dist(etelemetry)
BuildRequires:  python3dist(prov)
BuildRequires:  python3dist(pydot)
BuildRequires:  python3dist(puremagic)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(traits)
BuildRequires:  python3dist(looseversion)
BuildRequires:  python3dist(nibabel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
Provides:       nipypecli = %{version}-%{release}

%description
Nipype is a Python project that provides a uniform interface to existing
neuroimaging software and facilitates interaction between these packages
within a single workflow.

%generate_buildrequires
%pyproject_buildrequires

%check
# skip tests as some deps we don't have yet. like pandas.

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/nipypecli

%changelog
%{?autochangelog}
