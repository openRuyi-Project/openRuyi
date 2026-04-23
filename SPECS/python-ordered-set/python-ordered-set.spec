# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ordered-set

Name:           python-%{srcname}
Version:        4.1.0
Release:        %autorelease
Summary:        Custom MutableSet that remembers its order
License:        MIT
URL:            https://github.com/rspeer/ordered-set
#!RemoteAsset:  sha256:694a8e44c87657c59292ede72891eb91d34131f6531463aab3009191c77364a8
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  ordered_set

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An OrderedSet is a custom MutableSet that remembers its order, so that every
entry has an index that can be looked up.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license MIT-LICENSE

%changelog
%autochangelog
