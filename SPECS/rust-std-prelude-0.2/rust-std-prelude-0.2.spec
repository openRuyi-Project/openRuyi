# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name std_prelude
%global full_version 0.2.12
%global pkgname std-prelude-0.2

Name:           rust-std-prelude-0.2
Version:        0.2.12
Release:        %autorelease
Summary:        Rust crate "std_prelude"
License:        MIT
URL:            https://github.com/vitiral/std_prelude
#!RemoteAsset:  sha256:8207e78455ffdf55661170876f88daf85356e4edd54e0a3dbc79586ca1e50cbe
Source:         https://static.crates.io/crates/std_prelude/0.2.12/download#/rust-std-prelude-0.2-0.2.12.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "std_prelude"

%package     -n %{name}+default
Summary:        Prelude that the rust stdlib should have always had - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust std_prelude crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
