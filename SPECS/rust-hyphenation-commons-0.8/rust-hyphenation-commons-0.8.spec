# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyphenation_commons
%global full_version 0.8.4
%global pkgname hyphenation-commons-0.8

Name:           rust-hyphenation-commons-0.8
Version:        0.8.4
Release:        %autorelease
Summary:        Rust crate "hyphenation_commons"
License:        Apache-2.0 OR MIT
URL:            https://github.com/tapeinosyne/hyphenation
#!RemoteAsset:  sha256:5febe7a2ade5c7d98eb8b75f946c046b335324b06a14ea0998271504134c05bf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fst-0.4/default) >= 0.4.0
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
