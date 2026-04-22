# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname GitPython

Name:           python-%{srcname}
Version:        3.1.46
Release:        %autorelease
Summary:        Python Git Library
License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/GitPython
#!RemoteAsset:  sha256:400124c7d0ef4ea03f7310ac2fbf7151e09ff97f2a3288d64a440c584a29c37f
Source0:        https://files.pythonhosted.org/packages/source/g/gitpython/gitpython-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l git

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(gitdb)
# used for check
BuildRequires:  git

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
GitPython is a python library used to interact with git repositories,
high-level like git-porcelain, or low-level like git-plumbing.

It provides abstractions of git objects for easy access of repository data, and
additionally allows you to access the git repository more directly using either
a pure python implementation, or the faster, but more resource intensive git
command implementation.

The object database implementation is optimized for handling large quantities
of objects and large datasets, which is achieved by using low-level structures
and data streaming.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES AUTHORS

%changelog
%autochangelog
