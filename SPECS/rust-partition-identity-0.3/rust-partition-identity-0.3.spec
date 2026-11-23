# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name partition-identity
%global full_version 0.3.0
%global pkgname partition-identity-0.3

Name:           rust-partition-identity-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "partition-identity"
License:        MIT
URL:            https://github.com/pop-os/partition-identity
#!RemoteAsset:  sha256:9fa925f9becb532d758b0014b472c576869910929cf4c3f8054b386f19ab9e21
Source:         https://static.crates.io/crates/partition-identity/0.3.0/download#/rust-partition-identity-0.3-0.3.0.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-1/default) >= 1.0.30
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "partition-identity"

%package     -n %{name}+default
Summary:        Find the ID of a device by its path, or find a device path by its ID - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust partition-identity crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
