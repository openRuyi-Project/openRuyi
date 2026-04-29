# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-build-config
%global full_version 0.26.0
%global pkgname pyo3-build-config-0.26

Name:           rust-pyo3-build-config-0.26
Version:        0.26.0
Release:        %autorelease
Summary:        Rust crate "pyo3-build-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:4fc6ddaf24947d12a9aa31ac65431fb1b851b8f4365426e182901eabfb87df5f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(target-lexicon-0.13/default) >= 0.13.2
Provides:       crate(pyo3-build-config) = %{version}
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

%package     -n %{name}+python3-dll-a
Summary:        Build configuration for the PyO3 ecosystem - feature "python3-dll-a"
Requires:       crate(%{pkgname})
Requires:       crate(python3-dll-a-0.2/default) >= 0.2.14
Provides:       crate(%{pkgname}/python3-dll-a)

%description -n %{name}+python3-dll-a
This metapackage enables feature "python3-dll-a" for the Rust pyo3-build-config crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
