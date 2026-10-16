# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_shared
%global full_version 0.7.24
%global pkgname phf-shared-0.7

Name:           rust-phf-shared-0.7
Version:        0.7.24
Release:        %autorelease
Summary:        Rust crate "phf_shared"
License:        MIT
URL:            https://github.com/sfackler/rust-phf
#!RemoteAsset:  sha256:234f71a15de2288bcb7e3b6515828d22af7ec8598ee6d24c3b526fa0a80b67a0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(siphasher-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_shared"

%package     -n %{name}+unicase
Summary:        Support code shared by PHF libraries - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-1/default) >= 1.4.0
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust phf_shared crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
