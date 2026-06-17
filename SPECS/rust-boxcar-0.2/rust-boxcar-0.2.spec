# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name boxcar
%global full_version 0.2.14
%global pkgname boxcar-0.2

Name:           rust-boxcar-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "boxcar"
License:        MIT
URL:            https://github.com/ibraheemdev/boxcar
#!RemoteAsset:  sha256:36f64beae40a84da1b4b26ff2761a5b895c12adc41dc25aaee1c4f2bbfe97a6e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "boxcar"

%package     -n %{name}+loom
Summary:        Concurrent, append-only vector - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(loom-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust boxcar crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
