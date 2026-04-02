# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jobserver
%global full_version 0.1.34
%global pkgname jobserver-0.1

Name:           rust-jobserver-0.1
Version:        0.1.34
Release:        %autorelease
Summary:        Rust crate "jobserver"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/jobserver-rs
#!RemoteAsset:  sha256:9afb3de4395d6b3e67a780b6de64b51c978ecf11cb9a462c66be7d4ca9039d33
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.3/default) >= 0.3.4
Requires:       crate(getrandom-0.3/std) >= 0.3.4
Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "jobserver"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
