# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyrsistent

Name:           python-%{srcname}
Version:        0.20.0
Release:        %autorelease
Summary:        Persistent/Functional/Immutable data structures
License:        MIT AND BSD-3-Clause
URL:            https://github.com/tobgu/pyrsistent
#!RemoteAsset:  sha256:4c48f78f62ab596c679086084d0dd13254ae4f3d6c72a83ffdf5ebdef8f265a4
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} _pyrsistent_version

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are
immutable.

All methods on a data structure that would normally mutate it instead
return a new copy of the structure containing the requested updates. The
original structure is left untouched.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES.txt README.rst

%changelog
%autochangelog
