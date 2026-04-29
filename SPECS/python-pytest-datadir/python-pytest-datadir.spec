# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-datadir
%global pypi_name pytest_datadir

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        Pytest plugin for test data directories and files
License:        MIT
URL:            https://pypi.org/project/pytest-datadir/
#!RemoteAsset:  sha256:7a15faed76cebe87cc91941dd1920a9a38eba56a09c11e9ddf1434d28a0f78eb
Source0:        https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{modname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(docutils)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package contains a pytest plugin for manipulating test data
directories and files.

%prep -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%generate_buildrequires
%pyproject_buildrequires

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%build -a
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html

%files -f %{pyproject_files}
%doc AUTHORS CHANGELOG.html README.md

%changelog
%{?autochangelog}
