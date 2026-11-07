# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyphenation_commons
%global full_version 0.7.1
%global pkgname hyphenation-commons-0.7

Name:           rust-hyphenation-commons-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "hyphenation_commons"
License:        Apache-2.0 OR MIT
URL:            https://github.com/tapeinosyne/hyphenation
#!RemoteAsset:  sha256:9e3461ab51107f7beb8e0c46606d6eb7dfa48880014a29c170afad3ce6b25add
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atlatl-0.1/default) >= 0.1.2
Requires:       crate(atlatl-0.1/serde) >= 0.1.2
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hyphenation_commons"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
