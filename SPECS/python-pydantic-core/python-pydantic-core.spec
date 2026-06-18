# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydantic-core
%global pypi_name pydantic_core

Name:           python-%{srcname}
Version:        2.41.5
Release:        %autorelease
Summary:        Core functionality for Pydantic validation and serialization
License:        MIT
URL:            https://github.com/pydantic/pydantic-core
#!RemoteAsset:  sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(puccinialin)
BuildRequires:  python3dist(maturin)
BuildRequires:  crate(ahash-0.8/default) >= 0.8.12
BuildRequires:  crate(base64-0.22/default) >= 0.22.1
BuildRequires:  crate(enum-dispatch-0.3/default) >= 0.3.13
BuildRequires:  crate(hex-0.4/default) >= 0.4.3
BuildRequires:  crate(idna-1/default) >= 1.1.0
BuildRequires:  crate(jiter-0.11/default) >= 0.11.1
BuildRequires:  crate(jiter-0.11/python) >= 0.11.1
BuildRequires:  crate(num-bigint-0.4/default) >= 0.4.6
BuildRequires:  crate(num-traits-0.2/default) >= 0.2.19
BuildRequires:  crate(percent-encoding-2/default) >= 2.3.2
BuildRequires:  crate(pyo3-0.26/default) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/generate-import-lib) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/num-bigint) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/py-clone) >= 0.26.0
BuildRequires:  crate(pyo3-build-config-0.26/default) >= 0.26.0
BuildRequires:  crate(regex-1/default) >= 1.12.3
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/arbitrary-precision) >= 1.0.150
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(smallvec-1/default) >= 1.15.1
BuildRequires:  crate(speedate-0.17/default) >= 0.17.0
BuildRequires:  crate(strum-0.27/default) >= 0.27.2
BuildRequires:  crate(strum-0.27/derive) >= 0.27.2
BuildRequires:  crate(strum-macros-0.27/default) >= 0.27.2
BuildRequires:  crate(url-2/default) >= 2.5.8
BuildRequires:  crate(uuid-1/default) >= 1.23.2
BuildRequires:  crate(version-check-0.9/default) >= 0.9.5

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the core functionality for
pydantic validation and serialization. Pydantic-core is
currently around 17x faster than pydantic V1.

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
