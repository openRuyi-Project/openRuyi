# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yeslogic-fontconfig-sys
%global full_version 6.0.1
%global pkgname yeslogic-fontconfig-sys-6

Name:           rust-yeslogic-fontconfig-sys-6
Version:        6.0.1
Release:        %autorelease
Summary:        Rust crate "yeslogic-fontconfig-sys"
License:        MIT
URL:            https://github.com/yeslogic/fontconfig-rs
#!RemoteAsset:  sha256:1d8b8abf912b9a29ff112e1671c97c33636903d13a69712037190e6805af4f76
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dlib-0.5/default) >= 0.5.0
Requires:       crate(once-cell-1/default) >= 1.9.0
Requires:       crate(pkg-config-0.3) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dlopen) = %{version}

%description
Source code for takopackized Rust crate "yeslogic-fontconfig-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
