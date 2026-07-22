# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-remotedata

Name:           python-%{srcname}
Version:        0.4.1
Release:        %autorelease
Summary:        Pytest plugin for controlling remote data access
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-remotedata
#!RemoteAsset:  sha256:05c08bf638cdd1ed66eb01738a1647c3c714737c3ec3abe009d2c1f793b4bb59
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pytest_remotedata

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pytest-remotedata is a pytest plugin for controlling access to data hosted on
remote servers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst

%changelog
%autochangelog
