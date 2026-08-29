# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name eyre
%global full_version 0.6.12
%global pkgname eyre-0.6

Name:           rust-eyre-0.6
Version:        0.6.12
Release:        %autorelease
Summary:        Rust crate "eyre"
License:        MIT OR Apache-2.0
URL:            https://github.com/eyre-rs/eyre
#!RemoteAsset:  sha256:7cd915d99f24784cdc19fd37ef22b97e3ff0ae756c7e492e9fbfe897d61e2aec
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indenter-0.3/default) >= 0.3.0
Requires:       crate(once-cell-1/default) >= 1.18.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/auto-install) = %{version}
Provides:       crate(%{pkgname}/track-caller) = %{version}

%description
Source code for takopackized Rust crate "eyre"

%package     -n %{name}+default
Summary:        Flexible concrete Error Reporting type built on std::error::Error with customizable Reports - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/auto-install) = %{version}
Requires:       crate(%{pkgname}/track-caller) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust eyre crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pyo3
Summary:        Flexible concrete Error Reporting type built on std::error::Error with customizable Reports - feature "pyo3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-0.20) >= 0.20.0
Provides:       crate(%{pkgname}/pyo3) = %{version}

%description -n %{name}+pyo3
This metapackage enables feature "pyo3" for the Rust eyre crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
