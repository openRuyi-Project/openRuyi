# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-priority-channel
%global full_version 0.2.0
%global pkgname async-priority-channel-0.2

Name:           rust-async-priority-channel-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "async-priority-channel"
License:        Apache-2.0 OR MIT
URL:            https://github.com/rmcgibbo/async-priority-channel
#!RemoteAsset:  sha256:acde96f444d31031f760c5c43dc786b97d3e1cb2ee49dd06898383fe9a999758
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(event-listener-4/default) >= 4.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-priority-channel"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
