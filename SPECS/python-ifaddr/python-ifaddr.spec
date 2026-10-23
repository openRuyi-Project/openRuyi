# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ifaddr

Name:           python-%{srcname}
Version:        0.2.0
Release:        %autorelease
Summary:        Cross-platform network interface and IP address enumeration library
License:        MIT
URL:            https://github.com/pydron/ifaddr
#!RemoteAsset:  sha256:cc0cbfcaabf765d44595825fb96a99bb12c79716b73b44330ea38ee2b0c4aed4
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# The Win32 backend loads Windows-only system libraries.
BuildOption(check):  -e ifaddr._win32

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ifaddr - Enumerate network interfaces/adapters and their IP addresses

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest --pyargs ifaddr.test_ifaddr

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
