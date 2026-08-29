# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aioitertools

Name:           python-%{srcname}
Version:        0.13.0
Release:        %autorelease
Summary:        itertools and builtins for AsyncIO and mixed iterables
License:        MIT
URL:            http://aioitertools.omnilib.dev/
VCS:            git:https://github.com/omnilib/aioitertools.git
#!RemoteAsset:  sha256:620bd241acc0bbb9ec819f1ab215866871b4bbd1f73836a55f799200ee86950c
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Implementation of itertools, builtins, and more for AsyncIO and mixed-type iterables.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
