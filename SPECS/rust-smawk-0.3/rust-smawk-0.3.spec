# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smawk
%global full_version 0.3.2
%global pkgname smawk-0.3

Name:           rust-smawk-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "smawk"
License:        MIT
URL:            https://github.com/mgeisler/smawk
#!RemoteAsset:  sha256:b7c388c1b5e93756d0c740965c41e8822f866621d41acbdf6336a6a168f8840c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "smawk"

%package     -n %{name}+ndarray
Summary:        Functions for finding row-minima in a totally monotone matrix - feature "ndarray"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndarray-0.15/default) >= 0.15.4
Provides:       crate(%{pkgname}/ndarray) = %{version}

%description -n %{name}+ndarray
This metapackage enables feature "ndarray" for the Rust smawk crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
