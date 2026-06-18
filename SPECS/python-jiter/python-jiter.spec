# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jiter

Name:           python-%{srcname}
Version:        0.14.0
Release:        %autorelease
Summary:        Fast iterable JSON parser
License:        MIT
URL:            https://github.com/pydantic/jiter
#!RemoteAsset:  sha256:e8a39e66dac7153cf3f964a12aad515afa8d74938ec5cc0018adcdae5367c79e
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  crate(ahash-0.8/default) >= 0.8.0
BuildRequires:  crate(autocfg-1/default) >= 1.5.0
BuildRequires:  crate(bitvec-1/default) >= 1.0.1
BuildRequires:  crate(lexical-parse-float-1/format) >= 1.0.5
BuildRequires:  crate(num-bigint-0.4/default) >= 0.4.4
BuildRequires:  crate(num-traits-0.2/default) >= 0.2.16
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.2
BuildRequires:  crate(pyo3-0.28/generate-import-lib) >= 0.28.2
BuildRequires:  crate(pyo3-0.28/num-bigint) >= 0.28.2
BuildRequires:  crate(pyo3-build-config-0.28/default) >= 0.28.2
BuildRequires:  crate(smallvec-1/default) >= 1.11.0
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
jiter is a high-performance iterable JSON parser used by pydantic ecosystem
components.

%prep -a
%rust_setup_registry

rm -f Cargo.lock
# Cargo metadata resolves dev/bench dependencies even though this package only
# builds the Python extension and runs import checks.
perl -0pi -e 's/\n\[dev-dependencies\].*?(?=\n\[\[test\]\]|\n\[\[bench\]\]|\n\[package\.metadata|\z)//s;
              s/\n\[\[(?:test|bench)\]\].*?(?=\n\[\[(?:test|bench)\]\]|\n\[package\.metadata|\z)//gs' \
  crates/jiter/Cargo.toml
cat >> crates/jiter/Cargo.toml <<'EOF'

[build-dependencies]
pyo3-build-config = { workspace = true, optional = true }
EOF
sed -e '/^[[:space:]]*\\(ahash\\|bitvec\\|lexical-parse-float\\|num-bigint\\|num-traits\\|smallvec\\)[[:space:]]*=/ s/version *= *"/version = ">=/' \
  -e '/^[[:space:]]*\\(ahash\\|bitvec\\|lexical-parse-float\\|num-bigint\\|num-traits\\|smallvec\\)[[:space:]]*=/ s/= *"/= ">=/' \
  -e '/\\bpyo3\\b/ s/version *= *"/version = ">=/' \
  -i Cargo.toml crates/jiter/Cargo.toml crates/jiter-python/Cargo.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
