# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aho-corasick
%global full_version 0.5.3
%global pkgname aho-corasick-0.5

Name:           rust-aho-corasick-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "aho-corasick"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/aho-corasick
#!RemoteAsset:  sha256:ca972c2ea5f742bfce5687b9aef75506a764f61d37f8f649047846a9686ddb66
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-0.1/default) >= 0.1.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "aho-corasick"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
