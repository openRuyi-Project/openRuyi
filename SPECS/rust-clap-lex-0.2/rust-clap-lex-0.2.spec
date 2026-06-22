# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_lex
%global full_version 0.2.4
%global pkgname clap-lex-0.2

Name:           rust-clap-lex-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "clap_lex"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap/tree/master/clap_lex
#!RemoteAsset:  sha256:2850f2f5a82cbf437dd5af4d49848fbdfc27c157c3d010345776f952765261c5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(os-str-bytes-6/raw-os-str) >= 6.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clap_lex"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
