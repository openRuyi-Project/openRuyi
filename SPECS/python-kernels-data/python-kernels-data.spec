# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname kernels-data
%global pypi_name kernels_data

Name:           python-%{srcname}
Version:        0.16.0
Release:        %autorelease
Summary:        Data structures for Hugging Face compute kernels
License:        Apache-2.0
URL:            https://github.com/huggingface/kernels
VCS:            git:https://github.com/huggingface/kernels.git
#!RemoteAsset:  sha256:a4dae006305a572122ae8550a224b678d747ffaba431dff8a3f21817271e7148
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(maturin) >= 1
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(pip)
BuildRequires:  rust >= 1.85
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(base64-0.22/default) >= 0.22.0
BuildRequires:  crate(digest-0.11/default) >= 0.11.0
BuildRequires:  crate(eyre-0.6/default) >= 0.6.12
BuildRequires:  crate(itertools-0.13/default) >= 0.13.0
BuildRequires:  crate(pyo3-0.26/abi3) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/abi3-py38) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/default) >= 0.26.0
BuildRequires:  crate(regex-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(serde-value-0.7/default) >= 0.7.0
BuildRequires:  crate(sha2-0.11/default) >= 0.11.0
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
BuildRequires:  crate(thiserror-1/default) >= 1.0.0
BuildRequires:  crate(url-2/default) >= 2.0.0
BuildRequires:  crate(url-2/serde) >= 2.0.0
BuildRequires:  crate(walkdir-2/default) >= 2.0.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Rust-backed Python data structures used to describe and validate Hugging Face
compute kernel metadata.

%prep -a
%rust_setup_registry
rm -f Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
