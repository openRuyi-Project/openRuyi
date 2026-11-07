# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytes
%global full_version 0.4.12
%global pkgname bytes-0.4

Name:           rust-bytes-0.4
Version:        0.4.12
Release:        %autorelease
Summary:        Rust crate "bytes"
License:        MIT
URL:            https://github.com/carllerche/bytes
#!RemoteAsset:  sha256:206fdffcfa2df7cbe15601ef46c813fce0965eb3286db6b56c583b814b51c81c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.1.0
Requires:       crate(iovec-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bytes"

%package     -n %{name}+either
Summary:        Types and traits for working with bytes - feature "either"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(either-1) >= 1.5.0
Provides:       crate(%{pkgname}/either) = %{version}

%description -n %{name}+either
This metapackage enables feature "either" for the Rust bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+i128
Summary:        Types and traits for working with bytes - feature "i128"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(byteorder-1/i128) >= 1.1.0
Provides:       crate(%{pkgname}/i128) = %{version}

%description -n %{name}+i128
This metapackage enables feature "i128" for the Rust bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Types and traits for working with bytes - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bytes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
