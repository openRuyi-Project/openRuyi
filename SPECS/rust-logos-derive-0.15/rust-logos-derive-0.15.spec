# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name logos-derive
%global full_version 0.15.1
%global pkgname logos-derive-0.15

Name:           rust-logos-derive-0.15
Version:        0.15.1
Release:        %autorelease
Summary:        Rust crate "logos-derive"
License:        MIT OR Apache-2.0
URL:            https://logos.maciej.codes/
#!RemoteAsset:  sha256:605d9697bcd5ef3a42d38efc51541aa3d6a4a25f7ab6d1ed0da5ac632a26b470
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(logos-codegen-0.15/default) >= 0.15.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "logos-derive"

%package     -n %{name}+debug
Summary:        Create ridiculously fast Lexers - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-codegen-0.15/debug) >= 0.15.1
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust logos-derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+forbid-unsafe
Summary:        Create ridiculously fast Lexers - feature "forbid_unsafe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-codegen-0.15/forbid-unsafe) >= 0.15.1
Provides:       crate(%{pkgname}/forbid-unsafe) = %{version}

%description -n %{name}+forbid-unsafe
This metapackage enables feature "forbid_unsafe" for the Rust logos-derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
