# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name scroll
%global full_version 0.12.0
%global pkgname scroll-0.12

Name:           rust-scroll-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "scroll"
License:        MIT
URL:            https://github.com/m4b/scroll
#!RemoteAsset:  sha256:6ab8598aa408498679922eff7fa985c25d58a90771bd6be794434c5277eab1a6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "scroll"

%package     -n %{name}+derive
Summary:        Suite of powerful, extensible, generic, endian-aware Read/Write traits for byte buffers - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(scroll-derive-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust scroll crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
