# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytes
%global full_version 1.11.1
%global pkgname bytes-1.0

Name:           rust-bytes-1.0
Version:        1.11.1
Release:        %autorelease
Summary:        Rust crate "bytes"
License:        MIT
URL:            https://github.com/tokio-rs/bytes
#!RemoteAsset:  sha256:1e748733b7cbc798e1434b6ac524f0c1ff2ab456fe201501e6497c8417a4fc33
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "bytes"

%package     -n %{name}+extra-platforms
Summary:        Types and traits for working with bytes - feature "extra-platforms"
Requires:       crate(%{pkgname})
Requires:       crate(portable-atomic-1.0/require-cas) >= 1.3
Provides:       crate(%{pkgname}/extra-platforms)

%description -n %{name}+extra-platforms
This metapackage enables feature "extra-platforms" for the Rust bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Types and traits for working with bytes - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.60
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bytes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
