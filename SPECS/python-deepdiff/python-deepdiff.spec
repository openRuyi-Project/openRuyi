# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname deepdiff

Name:           python-%{srcname}
Version:        9.0.0
Release:        %autorelease
Summary:        Deep Difference and search of any Python object/data
License:        MIT
URL:            https://zepworks.com/deepdiff/
VCS:            git:https://github.com/qlustered/deepdiff.git
#!RemoteAsset:  sha256:4872005306237b5b50829803feff58a1dfd20b2b357a55de22e7ded65b2008a7
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(click)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Deep Difference and search of any Python object/data.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/deep

%changelog
%autochangelog
