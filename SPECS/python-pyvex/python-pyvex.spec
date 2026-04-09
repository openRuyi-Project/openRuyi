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
#!RemoteAsset
Source0:        https://github.com/angr/pyvex/archive/v%{version}/pyvex-%{version}.tar.gz
#!RemoteAsset
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

Provides:       python3-%{srcname}
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
%license LICENSE
%license LICENSE-pyvex_c

%changelog
%autochangelog
