# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aniso8601

Name:           python-%{srcname}
Version:        9.0.1
Release:        %autorelease
Summary:        Another ISO 8601 parser for Python
License:        BSD-3-Clause
URL:            https://bitbucket.org/nielsenb/aniso8601
#!RemoteAsset:  sha256:72e3117667eedf66951bb2d93f4296a56b94b078a8a95905a052611fb3f1b973
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python 3 library for parsing date strings in ISO 8601 format into
datetime format.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
