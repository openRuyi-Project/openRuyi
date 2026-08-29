# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname partd

Name:           python-%{srcname}
Version:        1.4.2
Release:        %autorelease
Summary:        Appendable key-value storage
License:        BSD-3-Clause
URL:            https://github.com/dask/partd
#!RemoteAsset:  sha256:d022c33afbdc8405c226621b015e8067888173d85f7f5ecebb3cafed9a20f02c
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(locket)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyzmq)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toolz)
BuildRequires:  python3dist(versioneer[toml])

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Partd is an appendable key-value storage. It is used by dask for shuffling
data between workers in distributed computing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
