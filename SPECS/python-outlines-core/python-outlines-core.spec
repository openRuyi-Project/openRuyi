# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
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
# ImportError: libomp.so: cannot open shared object file: No such file or directory
BuildOption(check):  -e outlines_core.kernels.torch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(torch)
BuildRequires:  rust
BuildRequires:  cmake
BuildRequires:  rust-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  crate(bincode-2/default) >= 2.0.1
BuildRequires:  crate(hf-hub-0.4/rustls-tls) >= 0.4.1
BuildRequires:  crate(hf-hub-0.4/ureq) >= 0.4.1
BuildRequires:  crate(once-cell-1/default) >= 1.20
BuildRequires:  crate(pyo3-0.27/default) >= 0.27.0
BuildRequires:  crate(pyo3-0.27/extension-module) >= 0.27.0
BuildRequires:  crate(pyo3-0.27/generate-import-lib) >= 0.27.0
BuildRequires:  crate(regex-1/default) >= 1.10.6
BuildRequires:  crate(regex-automata-0.4/default) >= 0.4.9
BuildRequires:  crate(rustc-hash-2/default) >= 2.1.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(serde-json-1/preserve-order) >= 1.0.0
BuildRequires:  crate(serde-pyobject-0.8/default) >= 0.8.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.0
BuildRequires:  crate(tokenizers-0.22/http) >= 0.22.2
BuildRequires:  crate(tokenizers-0.22/onig) >= 0.22.2
BuildRequires:  crate(tokenizers-0.22/rustls-tls) >= 0.22.2
BuildRequires:  crate(winapi-i686-pc-windows-gnu-0.4/default) >= 0.4.0
BuildRequires:  crate(winapi-x86-64-pc-windows-gnu-0.4/default) >= 0.4.0

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
%rust_setup_registry
rm -f Cargo.lock

%build -p
export AWS_LC_SYS_NO_JITTER_ENTROPY=1

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
