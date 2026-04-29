# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kqueue-sys
%global full_version 1.0.4
%global pkgname kqueue-sys-1.0

Name:           rust-kqueue-sys-1.0
Version:        1.0.4
Release:        %autorelease
Summary:        Rust crate "kqueue-sys"
License:        MIT
URL:            https://gitlab.com/rust-kqueue/rust-kqueue-sys
#!RemoteAsset:  sha256:ed9625ffda8729b85e45cf04090035ac368927b8cebc34898e7c120f52e4838b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1.0/default) >= 1.3.2
Requires:       crate(libc-0.2/default) >= 0.2.169
Provides:       crate(kqueue-sys) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "kqueue-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
