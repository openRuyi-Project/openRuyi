# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tendril
%global full_version 0.4.3
%global pkgname tendril-0.4

Name:           rust-tendril-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "tendril"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/tendril
#!RemoteAsset:  sha256:d24a120c5fc464a3458240ee02c299ebcb9d67b5249c8848b09d639dca8d7bb0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futf-0.1/default) >= 0.1.5
Requires:       crate(mac-0.1/default) >= 0.1.0
Requires:       crate(utf-8-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tendril"

%package     -n %{name}+encoding
Summary:        Compact buffer/string type for zero-copy parsing - feature "encoding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/encoding) = %{version}

%description -n %{name}+encoding
This metapackage enables feature "encoding" for the Rust tendril crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding-rs
Summary:        Compact buffer/string type for zero-copy parsing - feature "encoding_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-rs-0.8/default) >= 0.8.12
Provides:       crate(%{pkgname}/encoding-rs) = %{version}

%description -n %{name}+encoding-rs
This metapackage enables feature "encoding_rs" for the Rust tendril crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
