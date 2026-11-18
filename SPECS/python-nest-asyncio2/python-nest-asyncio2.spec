# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nest-asyncio2
%global pypi_name nest_asyncio2

Name:           python-%{srcname}
Version:        1.7.4
Release:        %autorelease
Summary:        Patch asyncio to allow nested event loops
License:        BSD-2-Clause
URL:            https://github.com/Chaoses-Ib/nest-asyncio2
#!RemoteAsset:  sha256:995b1409d926ec55e0876ea39a69bffdd8852cf1db3652c177e8c8ffdbcaf3cc
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
By design asyncio does not allow
its event loop to be nested. This presents a practical problem:
When in an environment where the event loop is
already running it's impossible to run tasks and wait
for the result.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
