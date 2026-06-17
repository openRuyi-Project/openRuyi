# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name psm
%global full_version 0.1.31
%global pkgname psm-0.1

Name:           rust-psm-0.1
Version:        0.1.31
Release:        %autorelease
Summary:        Rust crate "psm"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/stacker/
#!RemoteAsset:  sha256:645dbe486e346d9b5de3ef16ede18c26e6c70ad97418f4874b8b1889d6e761ea
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ar-archive-writer-0.5) >= 0.5.0
Requires:       crate(cc-1) >= 1.2.33
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "psm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
