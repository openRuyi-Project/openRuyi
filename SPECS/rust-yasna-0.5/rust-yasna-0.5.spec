# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yasna
%global full_version 0.5.2
%global pkgname yasna-0.5

Name:           rust-yasna-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "yasna"
License:        MIT OR Apache-2.0
URL:            https://github.com/qnighy/yasna.rs
#!RemoteAsset:  sha256:e17bb3549cc1321ae1296b9cdc2698e2b6cb1992adfa19a8c72e5b7a738f44cd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "yasna"

%package     -n %{name}+bit-vec
Summary:        ASN.1 library for Rust - feature "bit-vec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bit-vec-0.6/std) >= 0.6.1
Provides:       crate(%{pkgname}/bit-vec) = %{version}

%description -n %{name}+bit-vec
This metapackage enables feature "bit-vec" for the Rust yasna crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        ASN.1 library for Rust - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust yasna crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        ASN.1 library for Rust - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/std) >= 0.3.1
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust yasna crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
