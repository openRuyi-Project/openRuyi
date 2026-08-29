# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname safetensors

Name:           python-%{srcname}
Version:        0.8.0
Release:        %autorelease
Summary:        Simple, safe way to store and distribute tensors
License:        Apache-2.0
URL:            https://github.com/huggingface/safetensors
#!RemoteAsset:  sha256:fabaf3e0f18a6618d9b36560682562157f77c2b71fcffc7b432be2baed9d753d
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
BuildRequires:  crate(libc-0.2/default) >= 0.2
BuildRequires:  crate(memmap2-0.9/default) >= 0.9
BuildRequires:  crate(pyo3-0.28/abi3) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/abi3-py310) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/extension-module) >= 0.28.3
BuildRequires:  crate(rustversion-1/default) >= 1.0.22
BuildRequires:  crate(serde-1/alloc) >= 1.0
BuildRequires:  crate(serde-1/derive) >= 1.0
BuildRequires:  crate(serde-json-1/alloc) >= 1.0
BuildRequires:  crate(serde-json-1/default) >= 1.0
BuildRequires:  crate(tempfile-3/default) >= 3.27.0

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
