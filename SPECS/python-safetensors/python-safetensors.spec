# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname safetensors

Name:           python-%{srcname}
Version:        0.7.0
Release:        %autorelease
Summary:        Simple, safe way to store and distribute tensors
License:        Apache-2.0
URL:            https://github.com/huggingface/safetensors
#!RemoteAsset:  sha256:07663963b67e8bd9f0b8ad15bb9163606cd27cc5a1b96235a50d8369803b96b0
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Drop test-only dependencies to keep the offline build closure minimal.
Patch2000:      2000-fix-cargo.patch

BuildOption(install):  -l %{srcname}
# Needs additional dependencies
BuildOption(check):  -e "safetensors.torch" -e "safetensors.tensorflow" -e "safetensors.paddle" -e "safetensors.flax" -e "safetensors.mlx"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cargo
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(numpy)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(hashbrown-0.16/default) >= 0.16
BuildRequires:  crate(hashbrown-0.16/serde) >= 0.16
BuildRequires:  crate(memmap2-0.9/default) >= 0.9
BuildRequires:  crate(pyo3-0.25/abi3) >= 0.25.1
BuildRequires:  crate(pyo3-0.25/abi3-py38) >= 0.25.1
BuildRequires:  crate(pyo3-0.25/default) >= 0.25.1
BuildRequires:  crate(pyo3-0.25/extension-module) >= 0.25.1
BuildRequires:  crate(pyo3-build-config-0.25/abi3) >= 0.25.1
BuildRequires:  crate(pyo3-build-config-0.25/abi3-py38) >= 0.25.1
BuildRequires:  crate(pyo3-build-config-0.25/default) >= 0.25.1
BuildRequires:  crate(pyo3-build-config-0.25/extension-module) >= 0.25.1
BuildRequires:  crate(pyo3-build-config-0.25/resolve-config) >= 0.25.1
BuildRequires:  crate(pyo3-ffi-0.25/abi3) >= 0.25.1
BuildRequires:  crate(pyo3-ffi-0.25/abi3-py38) >= 0.25.1
BuildRequires:  crate(pyo3-ffi-0.25/default) >= 0.25.1
BuildRequires:  crate(pyo3-ffi-0.25/extension-module) >= 0.25.1
BuildRequires:  crate(pyo3-macros-0.25/default) >= 0.25.1
BuildRequires:  crate(pyo3-macros-backend-0.25/default) >= 0.25.1
BuildRequires:  crate(rustversion-1/default) >= 1.0.22
BuildRequires:  crate(serde-1/alloc) >= 1.0
BuildRequires:  crate(serde-1/derive) >= 1.0
BuildRequires:  crate(serde-json-1/alloc) >= 1.0
BuildRequires:  crate(serde-json-1/default) >= 1.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This repository implements a new simple format for storing
tensors safely (as opposed to pickle) and that is still fast (zero-copy).

%prep -a
%rust_setup_registry
rm -f bindings/python/Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc safetensors/README.md
%license safetensors/LICENSE

%changelog
%autochangelog
