# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cryptography

Name:           python-%{srcname}
Version:        50.0.0
Release:        %autorelease
Summary:        PyCA's cryptography library
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://cryptography.io/en/latest/
VCS:            git:https://github.com/pyca/cryptography
#!RemoteAsset:  sha256:eeac2acb5a20ed25e0ad6d1df9891a520b78b404266b6d11778f25d5d691a6c9
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cffi)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(maturin)
BuildRequires:  crate(asn1-0.24) >= 0.24.1
BuildRequires:  crate(base64-0.23/default) >= 0.23.0
BuildRequires:  crate(cc-1/default) >= 1.2.63
BuildRequires:  crate(cfg-if-1/default) >= 1.0.4
BuildRequires:  crate(foreign-types-0.3/default) >= 0.3.2
BuildRequires:  crate(foreign-types-shared-0.1/default) >= 0.1.1
BuildRequires:  crate(openssl-0.10/default) >= 0.10.80
BuildRequires:  crate(openssl-sys-0.9/default) >= 0.9.117
BuildRequires:  crate(pem-4) >= 4.0.0
BuildRequires:  crate(pyo3-0.29/abi3) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/abi3t) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/default) >= 0.29.0
BuildRequires:  crate(pyo3-build-config-0.29/default) >= 0.29.0
BuildRequires:  crate(self-cell-1/default) >= 1.2.2

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       openssl

%description
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%prep -a
%rust_setup_registry
rm -f Cargo.lock
sed -i 's/^[[:space:]]*locked[[:space:]]*=.*/locked = false/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%install -p
# https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete

%files -f %{pyproject_files}
%doc README.rst docs
%license LICENSE LICENSE.APACHE LICENSE.BSD

%changelog
%autochangelog
