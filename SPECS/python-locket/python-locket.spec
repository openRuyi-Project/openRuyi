# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname locket

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        File-based locks for Python on Linux and Windows
License:        BSD-2-Clause
URL:            https://github.com/mwilliamson/locket.py
#!RemoteAsset:  sha256:5c0d4c052a8bbbf750e056a8e65ccd309086f4f0f18a2eac306a8dfa4112a632
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Locket is a Python package that provides file-based locking for Linux and
Windows. It allows you to lock files for reading and writing, which is useful
for coordinating access to shared resources.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
