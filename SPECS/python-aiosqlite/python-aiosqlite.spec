# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiosqlite

Name:           python-%{srcname}
Version:        0.22.1
Release:        %autorelease
Summary:        Asyncio bridge to the standard sqlite3 module
License:        MIT
URL:            https://github.com/omnilib/aiosqlite
VCS:            git:https://github.com/omnilib/aiosqlite.git
#!RemoteAsset:  sha256:043e0bd78d32888c0a9ca90fc788b38796843360c855a7262a532813133a0650
Source:         https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
aiosqlite provides a friendly, async interface to sqlite3, wrapping the
standard library sqlite3 module in a thin layer of async/await syntax.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
