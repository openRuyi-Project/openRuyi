# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyvex

Name:           python-%{srcname}
Version:        9.2.214
Release:        %autorelease
Summary:        A Python interface to libvex and VEX IR
License:        BSD-2-Clause AND GPL-3.0-or-later AND LGPL-2.0-only
URL:            https://github.com/angr/pyvex
#!RemoteAsset:  sha256:4e2e1220de8b8cb163d8e500c8eb6eca964184d78aefad392526488cdfb64416
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Allow repository-provided scikit-build-core 0.12.x.
Patch2000:         2000-relax-scikit-build-core-upper-bound.patch

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

%generate_buildrequires
%pyproject_buildrequires

%install -a
mv pyvex_c/LICENSE LICENSE-pyvex_c

%files -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE-pyvex_c

%changelog
%autochangelog
