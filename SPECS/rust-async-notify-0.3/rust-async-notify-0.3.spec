# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-notify
%global full_version 0.3.4
%global pkgname async-notify-0.3

Name:           rust-async-notify-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "async-notify"
License:        MIT
URL:            https://github.com/Sherlock-Holo/async-notify
#!RemoteAsset:  sha256:63273b0e33b8941a02eabc1684f0230d3011ea45117351beb94c69253065a194
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(event-listener-5/default) >= 5.4.1
Requires:       crate(futures-core-0.3/default) >= 0.3.32
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.16

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-notify"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
