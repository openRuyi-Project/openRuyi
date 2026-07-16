# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rtoolbox
%global full_version 0.0.3
%global pkgname rtoolbox-0.0.3

Name:           rust-rtoolbox-0.0.3
Version:        0.0.3
Release:        %autorelease
Summary:        Rust crate "rtoolbox"
License:        Apache-2.0
URL:            https://github.com/conradkleinespel/duck
#!RemoteAsset:  sha256:a7cc970b249fbe527d6e02e0a227762c9108b2f49d81094fe357ffc6d14d7f6f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rtoolbox"

%package     -n %{name}+serde
Summary:        Utility functions for other crates, no backwards compatibility guarantees - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rtoolbox crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
