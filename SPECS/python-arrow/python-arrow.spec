# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname arrow

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Better dates and times for Python
License:        Apache-2.0
URL:            https://github.com/arrow-py/arrow
#!RemoteAsset:  sha256:ed0cc050e98001b8779e84d461b0098c4ac597e88704a655582b21d116e526d7
Source:         https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(pytzdata)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Arrow is a Python library that offers a sensible and human-friendly approach to
creating, manipulating, formatting and converting dates, times and timestamps.
It implements and updates the datetime type, plugging gaps in functionality.

%prep -a
# Fix python tzdata dependency
sed -i 's/tzdata;python_version/pytzdata;python_version/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.rst

%changelog
%autochangelog
