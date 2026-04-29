# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-chrome
%global full_version 0.7.2
%global pkgname tracing-chrome-0.7

Name:           rust-tracing-chrome-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "tracing-chrome"
License:        MIT
URL:            https://github.com/thoren-d/tracing-chrome
#!RemoteAsset:  sha256:bf0a738ed5d6450a9fb96e86a23ad808de2b727fd1394585da5cdd6788ffe724
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(tracing-core-0.1/default) >= 0.1.36
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.23
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tracing-chrome"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
