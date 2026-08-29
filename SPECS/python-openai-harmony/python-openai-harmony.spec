# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname openai-harmony
%global pypi_name openai_harmony

Name:           python-%{srcname}
Version:        0.0.8
Release:        %autorelease
Summary:        Renderer for OpenAI's harmony response format
License:        Apache-2.0
URL:            https://github.com/openai/harmony
VCS:            git:https://github.com/openai/harmony.git
#!RemoteAsset:  sha256:6e43f98e6c242fa2de6f8ea12eab24af63fa2ed3e89c06341fb9d92632c5cbdf
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

# The Python wheel does not use WASM bindings; drop optional WASM and test-only
# crates to keep the offline Cargo dependency closure minimal.
Patch2000:      2000-disable-wasm-bindings-for-python-build.patch

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pydantic)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anyhow-1/default) >= 1.0.98
BuildRequires:  crate(base64-0.22/default) >= 0.22.1
BuildRequires:  crate(bstr-1/default) >= 1.5.0
BuildRequires:  crate(clap-4/default) >= 4
BuildRequires:  crate(clap-4/derive) >= 4
BuildRequires:  crate(fancy-regex-0.13/default) >= 0.13.0
BuildRequires:  crate(futures-0.3/default) >= 0.3
BuildRequires:  crate(image-0.25/default) >= 0.25.6
BuildRequires:  crate(pyo3-0.25/abi3-py38) >= 0.25.0
BuildRequires:  crate(pyo3-0.25/default) >= 0.25.0
BuildRequires:  crate(pyo3-0.25/extension-module) >= 0.25.0
BuildRequires:  crate(regex-1/default) >= 1.10.3
BuildRequires:  crate(reqwest-0.12/blocking) >= 0.12.5
BuildRequires:  crate(reqwest-0.12/json) >= 0.12.5
BuildRequires:  crate(reqwest-0.12/multipart) >= 0.12.5
BuildRequires:  crate(reqwest-0.12/rustls-tls) >= 0.12.5
BuildRequires:  crate(reqwest-0.12/stream) >= 0.12.5
BuildRequires:  crate(rustc-hash-1/default) >= 1.1.0
BuildRequires:  crate(serde-1/default) >= 1.0.219
BuildRequires:  crate(serde-1/derive) >= 1.0.219
BuildRequires:  crate(serde-json-1/default) >= 1.0.140
BuildRequires:  crate(serde-json-1/preserve-order) >= 1.0.140
BuildRequires:  crate(serde-with-3/default) >= 3.12.0
BuildRequires:  crate(sha1-0.10/default) >= 0.10.6
BuildRequires:  crate(sha2-0.10/default) >= 0.10.9
BuildRequires:  crate(thiserror-2/default) >= 2.0.12

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
openai-harmony provides Python bindings for rendering OpenAI's harmony
response format used by the gpt-oss open-weight model series.

%prep -a
%rust_setup_registry
rm -f Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
