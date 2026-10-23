# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gettext-sys
%global full_version 0.27.0
%global pkgname gettext-sys-0.27

Name:           rust-gettext-sys-0.27
Version:        0.27.0
Release:        %autorelease
Summary:        Rust crate "gettext-sys"
License:        MIT
URL:            https://github.com/gettext-rs/gettext-rs
#!RemoteAsset:  sha256:4caa7e4460b196107cc1bb2629488e8b6dbb7f34f6683ea6753c4ac22f590785
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(temp-dir-0.1) >= 0.1.11

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gettext-system) = %{version}

%description
Source code for takopackized Rust crate "gettext-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
