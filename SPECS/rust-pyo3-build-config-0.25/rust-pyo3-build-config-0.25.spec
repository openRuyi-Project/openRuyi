# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-build-config
%global full_version 0.25.1
%global pkgname pyo3-build-config-0.25

Name:           rust-pyo3-build-config-0.25
Version:        0.25.1
Release:        %autorelease
Summary:        Rust crate "pyo3-build-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:458eb0c55e7ece017adeba38f2248ff3ac615e53660d7c71a238d7d2a01c7598
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(target-lexicon-0.13) >= 0.13.0
Requires:       crate(target-lexicon-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/abi3) = %{version}
Provides:       crate(%{pkgname}/abi3-py310) = %{version}
Provides:       crate(%{pkgname}/abi3-py311) = %{version}
Provides:       crate(%{pkgname}/abi3-py312) = %{version}
Provides:       crate(%{pkgname}/abi3-py313) = %{version}
Provides:       crate(%{pkgname}/abi3-py314) = %{version}
Provides:       crate(%{pkgname}/abi3-py37) = %{version}
Provides:       crate(%{pkgname}/abi3-py38) = %{version}
Provides:       crate(%{pkgname}/abi3-py39) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/extension-module) = %{version}
Provides:       crate(%{pkgname}/resolve-config) = %{version}

%description
Source code for takopackized Rust crate "pyo3-build-config"

%package     -n %{name}+python3-dll-a
Summary:        Build configuration for the PyO3 ecosystem - feature "python3-dll-a"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(python3-dll-a-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}/python3-dll-a) = %{version}

%description -n %{name}+python3-dll-a
This metapackage enables feature "python3-dll-a" for the Rust pyo3-build-config crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
