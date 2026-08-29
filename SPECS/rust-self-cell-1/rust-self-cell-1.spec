# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name self_cell
%global full_version 1.2.2
%global pkgname self-cell-1

Name:           rust-self-cell-1
Version:        1.2.2
Release:        %autorelease
Summary:        Rust crate "self_cell"
License:        Apache-2.0 OR GPL-2.0-only
URL:            https://github.com/Voultapher/self_cell
#!RemoteAsset:  sha256:b12e76d157a900eb52e81bc6e9f3069344290341720e9178cde2407113ac8d89
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "self_cell"

%package     -n %{name}+rustversion
Summary:        Safe-to-use proc-macro-free self-referential structs in stable Rust - feature "rustversion" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustversion-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/old-rust) = %{version}
Provides:       crate(%{pkgname}/rustversion) = %{version}

%description -n %{name}+rustversion
This metapackage enables feature "rustversion" for the Rust self_cell crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "old_rust" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
