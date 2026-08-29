# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyroute2

Name:           python-%{srcname}
Version:        0.7.12
Release:        %autorelease
Summary:        Python netlink library
License:        Apache-2.0 OR GPL-2.0-or-later
URL:            https://github.com/svinota/pyroute2
#!RemoteAsset:  sha256:54d226fc3ff2732f49bac9b26853c50c9d05be05a4d9daf09c7cf6d77301eff3
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
BuildOption(check):  -e 'pyroute2.cli.auth.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(mitogen)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyRoute2 provides several levels of API to work with Netlink
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,
IPQ.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE.GPL-2.0-or-later LICENSE.Apache-2.0
%{_bindir}/ss2
%{_bindir}/%{srcname}-cli
%{_bindir}/%{srcname}-dhcp-client
%{_bindir}/%{srcname}-test-platform
%{python3_sitelib}/pr2modules

%changelog
%autochangelog
