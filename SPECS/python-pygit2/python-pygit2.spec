# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pygit2

Name:           python-%{srcname}
Version:        1.18.2
Release:        %autorelease
Summary:        Python bindings for libgit2
License:        GPL-2.0-only WITH GCC-exception-2.0
URL:            https://www.pygit2.org/
VCS:            git:https://github.com/libgit2/pygit2
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  make

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license COPYING

%changelog
%{?autochangelog}
