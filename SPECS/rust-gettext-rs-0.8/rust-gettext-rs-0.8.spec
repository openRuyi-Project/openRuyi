# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gettext-rs
%global full_version 0.8.0
%global pkgname gettext-rs-0.8

Name:           rust-gettext-rs-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "gettext-rs"
License:        MIT
URL:            https://github.com/gettext-rs/gettext-rs
#!RemoteAsset:  sha256:9df5e3fa8c077b15fdfa8ce130e2bc73d663b8aaa6d51b71421b8659980b1d80
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gettext-sys-0.27/default) >= 0.27.0
Requires:       crate(locale-config-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gettext-rs"

%package     -n %{name}+gettext-system
Summary:        Safe bindings for gettext - feature "gettext-system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gettext-sys-0.27/gettext-system) >= 0.27.0
Provides:       crate(%{pkgname}/gettext-system) = %{version}

%description -n %{name}+gettext-system
This metapackage enables feature "gettext-system" for the Rust gettext-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
