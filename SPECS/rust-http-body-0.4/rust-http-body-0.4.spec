# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name http-body
%global full_version 0.4.6
%global pkgname http-body-0.4

Name:           rust-http-body-0.4
Version:        0.4.6
Release:        %autorelease
Summary:        Rust crate "http-body"
License:        MIT
URL:            https://github.com/hyperium/http-body
#!RemoteAsset:  sha256:7ceab25649e9960c0311ea418d17bee82c0dcec1bd053b5f9a66e265a693bed2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(http-0.2/default) >= 0.2.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "http-body"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
