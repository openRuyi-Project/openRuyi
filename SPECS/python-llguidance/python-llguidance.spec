# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname llguidance

Name:           python-%{srcname}
Version:        1.7.5
Release:        %autorelease
Summary:        Low-level guidance Rust library bindings for Python
License:        MIT
URL:            https://github.com/microsoft/llguidance
#!RemoteAsset:  sha256:afaa8f979708cd546c762f06a4fe4748e5ef7f06ed45875dabe7db8f07b73645
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Drop optional/dev Rust dependencies used only for wasm, header-generation, and
# benchmark/test features that are not enabled for the Python extension build.
Patch2000:      2000-remove-unused-optional-rust-dependencies.patch

BuildOption(install):  -l %{srcname} -L
# Skip optional Hugging Face CLI integration: No module named 'huggingface_hub'.
BuildOption(check):  -e 'llguidance.cli'
# Skip optional Transformers tokenizer integration: No module named 'transformers'.
BuildOption(check):  -e 'llguidance.hf'
# Skip llama.cpp integration: No module named 'llama_cpp'.
BuildOption(check):  -e 'llguidance.llamacpp'
# Skip MLX integration: No module named 'mlx'.
BuildOption(check):  -e 'llguidance.mlx'
# Skip optional PyTorch integration: No module named 'torch'.
BuildOption(check):  -e 'llguidance.torch'

BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  rust >= 1.87
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anyhow-1/default) >= 1.0.95
BuildRequires:  crate(bytemuck-1/default) >= 1.21.0
BuildRequires:  crate(derivre-0.3/ahash) >= 0.3.11
BuildRequires:  crate(derivre-0.3/compress) >= 0.3.11
BuildRequires:  crate(indexmap-2/default) >= 2.7.1
BuildRequires:  crate(jsonschema-0.29/default) >= 0.29.0
BuildRequires:  crate(lazy-static-1/default) >= 1.5.0
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.2
BuildRequires:  crate(pyo3-0.28/abi3-py39) >= 0.28.2
BuildRequires:  crate(pyo3-0.28/anyhow) >= 0.28.2
BuildRequires:  crate(pyo3-0.28/extension-module) >= 0.28.2
BuildRequires:  crate(rayon-1/default) >= 1.10.0
BuildRequires:  crate(referencing-0.29/default) >= 0.29.0
BuildRequires:  crate(regex-syntax-0.8/default) >= 0.8.5
BuildRequires:  crate(serde-1/derive) >= 1.0.217
BuildRequires:  crate(serde-json-1/preserve-order) >= 1.0.138
BuildRequires:  crate(tiktoken-rs-0.7/default) >= 0.7.0
BuildRequires:  crate(tokenizers-0.21/fancy-regex) >= 0.21.2
BuildRequires:  crate(tokenizers-0.21/unstable-wasm) >= 0.21.2

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
llguidance provides Python bindings for the low-level Guidance Rust library for
fast structured output generation and grammar-based token guidance.

%prep -a
%rust_setup_registry
rm -f Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
