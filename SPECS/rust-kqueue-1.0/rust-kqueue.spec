# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kqueue
%global full_version 1.0.8
%global pkgname kqueue-1.0

Name:           rust-kqueue-1.0
Version:        1.0.8
Release:        %autorelease
Summary:        Rust crate "kqueue"
License:        MIT
URL:            https://gitlab.com/rust-kqueue/rust-kqueue
#!RemoteAsset:  sha256:7447f1ca1b7b563588a205fe93dea8df60fd981423a768bc1c0ded35ed147d0c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kqueue-sys-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2/default) >= 0.2.169
Provides:       crate(kqueue) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "kqueue"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
