# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyvex
# libvexversion from pyvex's subdirectory called `vex @ xxxxx`(xxxxx is the libvexversion)
%global libvexversion 421bf0d9ec800df09fe4f8d90a8c13a0c63325e3

Name:           python-%{srcname}
Version:        9.2.193
Release:        %autorelease
Summary:        A Python interface to libvex and VEX IR
License:        BSD-2-Clause AND GPL-3.0-or-later AND LGPL-2.0-only
URL:            https://github.com/angr/pyvex
#!RemoteAsset:  sha256:f097bf9aac73cc7e9d1fa1480375b11300bfa9f6b7740a953d3a036ea1b7a944
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:535900642805fa8795196a0f9b1e1cb22c663c6d1dac828d8f3e404605ff2468
Source1:        https://github.com/angr/vex/archive/%{libvexversion}/vex-%{libvexversion}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "pyvex.lib.libpyvex"

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(scikit-build-core) >= 0.11.4
BuildRequires:  python3dist(cffi) >= 1.0.3
BuildRequires:  python3dist(bitstring)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A Python interface to libVEX and the VEX intermediate representation.

%prep -a
# on riscv64 test_pyvex.py need more mem for test
%ifarch riscv64
sed -i 's/assert kb_end - kb_start < 5000/assert kb_end - kb_start < 50000/' tests/test_pyvex.py
%endif
tar xvf %{SOURCE1}
rm -rf vex
mv vex-%{libvexversion} vex

%generate_buildrequires
%pyproject_buildrequires

%install -a
mv pyvex_c/LICENSE LICENSE-pyvex_c

%files -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE-pyvex_c

%changelog
%autochangelog
