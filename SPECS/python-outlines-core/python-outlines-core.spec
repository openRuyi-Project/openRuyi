# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname outlines-core
%global pypi_name outlines_core

Name:           python-%{srcname}
Version:        0.2.14
Release:        %autorelease
Summary:        Structured Text Generation in Rust
License:        Apache-2.0
URL:            https://github.com/dottxt-ai/outlines-core
#!RemoteAsset:  sha256:64808deed1591ca3029ff64346ceb974cd5d780c916ea82504951fe83523039e
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
# No module named 'mlx'
BuildOption(check):  -e outlines_core.kernels.mlx
# No module named 'numba'
BuildOption(check):  -e outlines_core.kernels.numpy

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(torch)
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(bincode-2.0) >= 2.0.1
BuildRequires:  crate(bincode-derive-2.0) >= 2.0.1
BuildRequires:  crate(once-cell-1.0) >= 1.20
BuildRequires:  crate(regex-1.0) >= 1.10.6
BuildRequires:  crate(regex-automata-0.4) >= 0.4.9
BuildRequires:  crate(rustc-hash-2.0) >= 2.1.0
BuildRequires:  crate(serde-1.0) >= 1.0.0
BuildRequires:  crate(serde-json-1.0) >= 1.0.0
BuildRequires:  crate(thiserror-2.0) >= 2.0.0
BuildRequires:  crate(pyo3-0.27) >= 0.27.0
BuildRequires:  crate(js-sys-0.3) = 0.3.98
BuildRequires:  crate(web-sys-0.3) >= 0.3.98
BuildRequires:  crate(wasm-bindgen-macro-0.2.117) = 0.2.117
BuildRequires:  crate(wasm-bindgen-shared-0.2.117) = 0.2.117
BuildRequires:  crate(wasm-bindgen-macro-support-0.2.117) = 0.2.117
BuildRequires:  crate(wasm-bindgen-0.2.117) = 0.2.117
BuildRequires:  crate(serde-pyobject-0.8) >= 0.8.0
BuildRequires:  crate(python3-dll-a-0.2) >= 0.2.0
BuildRequires:  crate(serde-1.0/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1.0/preserve-order) >= 1.0.0
BuildRequires:  crate(tokenizers-0.22/onig) >= 0.22.2
BuildRequires:  crate(hf-hub-0.4/ureq) = 0.4.1
BuildRequires:  crate(hf-hub-0.4/rustls-tls) = 0.4.1
BuildRequires:  crate(aws-lc-sys-0.41) = 0.41.0
BuildRequires:  crate(aws-lc-rs-1.0) = 1.17.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the core functionality for structured generation,
formerly implemented in Outlines, with a focus on performance and portability,
it offers a convenient way to: build regular expressions from JSON schemas;
construct an Index object by combining a Vocabulary and regular expression to
efficiently map tokens from a given vocabulary to state transitions in a finite-state automation

%prep -a
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"
[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF
rm -rf Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
