# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ormsgpack

Name:           python-%{srcname}
Version:        1.12.2
Release:        %autorelease
Summary:        Fast Python MessagePack library
License:        Apache-2.0 OR MIT
URL:            https://github.com/ormsgpack/ormsgpack
VCS:            git:https://github.com/ormsgpack/ormsgpack.git
#!RemoteAsset:  sha256:944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  crate(ahash-0.8) >= 0.8.0
BuildRequires:  crate(bytecount-0.6) >= 0.6.9
BuildRequires:  crate(bytecount-0.6/generic-simd) >= 0.6.9
BuildRequires:  crate(bytecount-0.6/runtime-dispatch-simd) >= 0.6.9
BuildRequires:  crate(chrono-0.4) >= 0.4.43
BuildRequires:  crate(half-2.0) >= 2.6.0
BuildRequires:  crate(itoa-1.0) >= 1.0.0
BuildRequires:  crate(pyo3-0.27) >= 0.27.2
BuildRequires:  crate(pyo3-0.27/extension-module) >= 0.27.2
BuildRequires:  crate(pyo3-build-config-0.27/default) >= 0.27.0
BuildRequires:  crate(serde-1.0) >= 1.0.0
BuildRequires:  crate(serde-bytes-0.11) >= 0.11.19
BuildRequires:  crate(serde-bytes-0.11/std) >= 0.11.19
BuildRequires:  crate(simdutf8-0.1) >= 0.1.5
BuildRequires:  crate(simdutf8-0.1/std) >= 0.1.5
BuildRequires:  crate(smallvec-1.0) >= 1.15.0
BuildRequires:  crate(smallvec-1.0/union) >= 1.15.0
BuildRequires:  crate(smallvec-1.0/write) >= 1.15.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ormsgpack is a fast MessagePack serialization library for Python.

%prep -a
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF
rm -f Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE-APACHE LICENSE-MIT

%changelog
%autochangelog
