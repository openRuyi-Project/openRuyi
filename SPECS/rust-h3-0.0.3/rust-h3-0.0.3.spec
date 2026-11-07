# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name h3
%global full_version 0.0.3
%global pkgname h3-0.0.3

Name:           rust-h3-0.0.3
Version:        0.0.3
Release:        %autorelease
Summary:        Rust crate "h3"
License:        MIT
URL:            https://github.com/hyperium/h3
#!RemoteAsset:  sha256:b83e1915177ea624b5bbbdb16bc54f0c106c9664892c695f995e53f5c6793b80
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(fastrand-2/default) >= 2.0.1
Requires:       crate(futures-util-0.3/io) >= 0.3.0
Requires:       crate(http-0.2/default) >= 0.2.9
Requires:       crate(pin-project-lite-0.2) >= 0.2.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.40

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/i-implement-a-third-party-backend-and-opt-into-breaking-changes) = %{version}

%description
Source code for takopackized Rust crate "h3"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
