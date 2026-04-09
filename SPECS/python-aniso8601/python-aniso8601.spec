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
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install): -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-dateutil
BuildRequires:  python3-setuptools

Provides:       python3-%{srcname}
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
