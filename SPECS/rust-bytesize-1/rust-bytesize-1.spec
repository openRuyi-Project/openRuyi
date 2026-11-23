# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytesize
%global full_version 1.3.3
%global pkgname bytesize-1

Name:           rust-bytesize-1
Version:        1.3.3
Release:        %autorelease
Summary:        Rust crate "bytesize"
License:        Apache-2.0
URL:            https://github.com/bytesize-rs/bytesize/
#!RemoteAsset:  sha256:2e93abca9e28e0a1b9877922aacb20576e05d4679ffa78c3d6dc22a26a216659
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bytesize"

%package     -n %{name}+serde
Summary:        Utility for human-readable bytes representations - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.185
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bytesize crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
