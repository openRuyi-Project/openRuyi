# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name email_address
%global full_version 0.2.9
%global pkgname email-address-0.2

Name:           rust-email-address-0.2
Version:        0.2.9
Release:        %autorelease
Summary:        Rust crate "email_address"
License:        MIT
URL:            https://github.com/johnstonskj/rust-email_address.git
#!RemoteAsset:  sha256:e079f19b08ca6239f47f8ba8509c11cf3ea30095831f7fed61441475edd8c449
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "email_address"

%package     -n %{name}+serde
Summary:        Rust crate providing an implementation of an RFC-compliant `EmailAddress` newtype - feature "serde" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-support) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust email_address crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "serde_support" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
