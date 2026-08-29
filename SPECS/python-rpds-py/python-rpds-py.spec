# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rpds-py
%global pypi_name rpds_py

Name:           python-%{srcname}
Version:        0.30.0
Release:        %autorelease
Summary:        Python bindings to Rust's persistent data structures
License:        MIT
URL:            https://github.com/crate-py/rpds
#!RemoteAsset:  sha256:dd8ff7cf90014af0c0f787eea34794ebf6415242ee1d6fa91eaba725cc441e84
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  rpds

BuildRequires:  crate(archery-1/default) >= 1.2.2
BuildRequires:  crate(pyo3-0.27/default) >= 0.27.2
BuildRequires:  crate(pyo3-0.27/extension-module) >= 0.27.2
BuildRequires:  crate(pyo3-0.27/generate-import-lib) >= 0.27.2
BuildRequires:  crate(rpds-1/default) >= 1.2.0
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
rpds-py provides Python bindings to Rust's persistent data structures.

%prep -a
%rust_setup_registry

rm -f Cargo.lock
sed -e '/^[[:space:]]*\\(rpds\\|archery\\)[[:space:]]*=/ s/= *"/= ">=/' \
  -e '/\\bpyo3\\b/ s/version *= *"/version = ">=/' \
  -i Cargo.toml

%build -p
%ifarch riscv64
# Work around rustc SIGSEGV while compiling pyo3 under release optimization.
export RUST_MIN_STACK=33554432
export CARGO_BUILD_JOBS=1
export CARGO_PROFILE_RELEASE_OPT_LEVEL=1
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=256
%endif

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
