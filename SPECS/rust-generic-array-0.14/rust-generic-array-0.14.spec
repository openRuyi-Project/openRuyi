# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name generic-array
%global full_version 0.14.9
%global pkgname generic-array-0.14

Name:           rust-generic-array-0.14
Version:        0.14.9
Release:        %autorelease
Summary:        Rust crate "generic-array"
License:        MIT
URL:            https://github.com/fizyk20/generic-array.git
#!RemoteAsset:  sha256:4bb6743198531e02858aeaea5398fcc883e71851fcbcb5a2f773e2fb6cb1edf2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(typenum-1/default) >= 1.12.0
Requires:       crate(version-check-0.9) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/more-lengths) = %{version}

%description
Source code for takopackized Rust crate "generic-array"

%package     -n %{name}+serde
Summary:        Generic types implementing functionality of arrays - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Generic types implementing functionality of arrays - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
