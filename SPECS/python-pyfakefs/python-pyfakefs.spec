# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyfakefs

Name:           python-%{srcname}
Version:        6.2.0
Release:        %autorelease
Summary:        Fake file system that mocks the Python file system modules
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pyfakefs
#!RemoteAsset:  sha256:e59a36db447bf509ce9c97ab3d1510c08cc51895c5311325a560a5e5b5dc1940
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):    -e 'pyfakefs.pytest*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pyfakefs implements a fake file system that mocks the Python file system
modules. Using pyfakefs, your tests operate on a fake file system in memory
without touching the real disk. The software is pip-installable and works as
a pytest plugin or with unittest.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGES.md

%changelog
%autochangelog
