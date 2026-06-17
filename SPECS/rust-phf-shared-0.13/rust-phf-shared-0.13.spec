# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_shared
%global full_version 0.13.1
%global pkgname phf-shared-0.13

Name:           rust-phf-shared-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "phf_shared"
License:        MIT
URL:            https://github.com/rust-phf/rust-phf
#!RemoteAsset:  sha256:e57fef6bc5981e38c2ce2d63bfa546861309f875b8a75f092d1d54ae2d64f266
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(siphasher-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "phf_shared"

%package     -n %{name}+uncased
Summary:        Support code shared by PHF libraries - feature "uncased"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uncased-0.9) >= 0.9.9
Provides:       crate(%{pkgname}/uncased) = %{version}

%description -n %{name}+uncased
This metapackage enables feature "uncased" for the Rust phf_shared crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase
Summary:        Support code shared by PHF libraries - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2/default) >= 2.4.0
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust phf_shared crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
