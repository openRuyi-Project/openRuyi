# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name human-bandwidth
%global full_version 0.1.4
%global pkgname human-bandwidth-0.1

Name:           rust-human-bandwidth-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "human-bandwidth"
License:        Apache-2.0
URL:            https://github.com/stack-rs/human-bandwidth
#!RemoteAsset:  sha256:8a5afe042873d564e1fccc5d50983e1e6341ffcae8fb7603c6c542de7129a785
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bandwidth-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/binary-system) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/display-integer) = %{version}

%description
Source code for takopackized Rust crate "human-bandwidth"

%package     -n %{name}+serde
Summary:        Representing bandwidth speed in a human-readable format - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bandwidth-0.3/serde) >= 0.3.0
Requires:       crate(serde-1/default) >= 1.0.130
Requires:       crate(serde-1/derive) >= 1.0.130
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust human-bandwidth crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
