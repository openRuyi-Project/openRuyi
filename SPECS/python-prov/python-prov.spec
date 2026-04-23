# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname prov

Name:           python-%{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        W3C Provenance Data Model library
License:        MIT
URL:            https://github.com/trungdong/prov
#!RemoteAsset:  sha256:7d012b164f5bbb42e118ed9d25788ab012d09082b722bc9dd4e811a309ea57f5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pydot)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(rdflib)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A library for W3C Provenance Data Model supporting PROV-JSON and PROV-XML
import/export.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS.rst HISTORY.rst README.rst
%license LICENSE
%{_bindir}/prov-compare
%{_bindir}/prov-convert

%changelog
%autochangelog
