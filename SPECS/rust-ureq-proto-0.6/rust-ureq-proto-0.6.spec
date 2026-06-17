# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ureq-proto
%global full_version 0.6.0
%global pkgname ureq-proto-0.6

Name:           rust-ureq-proto-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "ureq-proto"
License:        MIT OR Apache-2.0
URL:            https://github.com/algesten/ureq-proto
#!RemoteAsset:  sha256:e994ba84b0bd1b1b0cf92878b7ef898a5c1760108fe7b6010327e274917a808c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/std) >= 0.22.1
Requires:       crate(http-1/std) >= 1.1.0
Requires:       crate(httparse-1) >= 1.8.0
Requires:       crate(log-0.4/default) >= 0.4.22
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/client) = %{version}
Provides:       crate(%{pkgname}/server) = %{version}

%description
Source code for takopackized Rust crate "ureq-proto"

%package     -n %{name}+default
Summary:        Ureq support crate - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/client) = %{version}
Requires:       crate(%{pkgname}/server) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ureq-proto crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
