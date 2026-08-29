# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname uuid-utils
%global pypi_name uuid_utils

Name:           python-%{srcname}
Version:        0.16.0
Release:        %autorelease
Summary:        Fast UUID utilities powered by Rust
License:        BSD-3-Clause
URL:            https://github.com/aminalaee/uuid-utils
VCS:            git:https://github.com/aminalaee/uuid-utils.git
#!RemoteAsset:  sha256:d6902d4375dfba4c9902c736bb82d3c040417b67f7d0fa48910ddfdb1ac95de7
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  crate(ahash-0.8/default) >= 0.8.12
BuildRequires:  crate(mac-address-1/default) >= 1.1.8
BuildRequires:  crate(memoffset-0.9/default) >= 0.9.1
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/extension-module) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/generate-import-lib) >= 0.28.3
BuildRequires:  crate(rand-0.10/default) >= 0.10.1
BuildRequires:  crate(uuid-1/default) >= 1.23.1
BuildRequires:  crate(uuid-1/fast-rng) >= 1.23.1
BuildRequires:  crate(uuid-1/v1) >= 1.23.1
BuildRequires:  crate(uuid-1/v3) >= 1.23.1
BuildRequires:  crate(uuid-1/v4) >= 1.23.1
BuildRequires:  crate(uuid-1/v5) >= 1.23.1
BuildRequires:  crate(uuid-1/v6) >= 1.23.1
BuildRequires:  crate(uuid-1/v7) >= 1.23.1
BuildRequires:  crate(uuid-1/v8) >= 1.23.1
BuildRequires:  crate(winapi-0.3) >= 0.3.9
BuildRequires:  crate(winapi-0.3/default) >= 0.3.9
BuildRequires:  crate(winapi-0.3/winerror) >= 0.3.9
BuildRequires:  crate(winapi-0.3/ws2def) >= 0.3.9
BuildRequires:  crate(winapi-0.3/iphlpapi) >= 0.3.9
BuildRequires:  crate(winapi-i686-pc-windows-gnu-0.4/default) >= 0.4.0
BuildRequires:  crate(winapi-x86-64-pc-windows-gnu-0.4/default) >= 0.4.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
uuid-utils is a fast replacement for Python's uuid module, implemented with
Rust and exposed as a Python extension module.

%prep -a
%rust_setup_registry
rm -rf Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
%autochangelog
