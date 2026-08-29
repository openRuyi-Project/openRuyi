# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

%global srcname ethtool

Name:           python-%{srcname}
Version:        0.15
Release:        %autorelease
Summary:        Python module to interface with ethtool
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-python/python-ethtool
#!RemoteAsset:  sha256:567260ea5805063bbcff71dabd6fb820f89bc84f720e9ebe315c7eef1449d908
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libnl-3.0)
%if %{with doc}
BuildRequires:  asciidoc
%endif

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python bindings for the ethtool kernel interface, that allows querying and
changing of Ethernet card settings, such as speed, port, auto-negotiation, and
PCI locations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license COPYING
%{_bindir}/pifconfig
%{_bindir}/pethtool

%changelog
%autochangelog
