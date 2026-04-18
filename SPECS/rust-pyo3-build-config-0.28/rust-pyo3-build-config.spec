# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-build-config
%global full_version 0.28.3
%global pkgname pyo3-build-config-0.28

Name:           rust-pyo3-build-config-0.28
Version:        0.28.3
Release:        %autorelease
Summary:        Rust crate "pyo3-build-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:e368e7ddfdeb98c9bca7f8383be1648fd84ab466bf2bc015e94008db6d35611e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(target-lexicon-0.13/default) >= 0.13.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/abi3)
Provides:       crate(%{pkgname}/abi3-py310)
Provides:       crate(%{pkgname}/abi3-py311)
Provides:       crate(%{pkgname}/abi3-py312)
Provides:       crate(%{pkgname}/abi3-py313)
Provides:       crate(%{pkgname}/abi3-py314)
Provides:       crate(%{pkgname}/abi3-py37)
Provides:       crate(%{pkgname}/abi3-py38)
Provides:       crate(%{pkgname}/abi3-py39)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/extension-module)
Provides:       crate(%{pkgname}/resolve-config)

%description
Source code for takopackized Rust crate "pyo3-build-config"

%package     -n %{name}+generate-import-lib
Summary:        Build configuration for the PyO3 ecosystem - feature "generate-import-lib"
Requires:       crate(%{pkgname})
Requires:       crate(python3-dll-a-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}/generate-import-lib)

%description -n %{name}+generate-import-lib
This metapackage enables feature "generate-import-lib" for the Rust pyo3-build-config crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
