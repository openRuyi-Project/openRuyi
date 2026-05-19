# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-indicatif
%global full_version 0.3.14
%global pkgname tracing-indicatif-0.3

Name:           rust-tracing-indicatif-0.3
Version:        0.3.14
Release:        %autorelease
Summary:        Rust crate "tracing-indicatif"
License:        MIT
URL:            https://github.com/emersonford/tracing-indicatif
#!RemoteAsset:  sha256:e1ef6990e0438749f0080573248e96631171a0b5ddfddde119aa5ba8c3a9c47e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indicatif-0.18/default) >= 0.18.3
Requires:       crate(indicatif-0.18/in-memory) >= 0.18.3
Requires:       crate(tracing-0.1/default) >= 0.1.43
Requires:       crate(tracing-core-0.1/default) >= 0.1.35
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.22
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tracing-indicatif"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
