# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cursor-icon
%global full_version 1.2.0
%global pkgname cursor-icon-1

Name:           rust-cursor-icon-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "cursor-icon"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/rust-windowing/cursor-icon
#!RemoteAsset:  sha256:f27ae1dd37df86211c42e150270f82743308803d90a6f6e6651cd730d5e1732f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "cursor-icon"

%package     -n %{name}+serde
Summary:        Cross platform cursor icon type - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.162
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cursor-icon crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
