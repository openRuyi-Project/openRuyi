# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syslog
%global full_version 7.0.0
%global pkgname syslog-7

Name:           rust-syslog-7
Version:        7.0.0
Release:        %autorelease
Summary:        Rust crate "syslog"
License:        MIT
URL:            https://github.com/Geal/rust-syslog
#!RemoteAsset:  sha256:019f1500a13379b7d051455df397c75770de6311a7a188a699499502704d9f10
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hostname-0.4/default) >= 0.4.0
Requires:       crate(libc-0.2/default) >= 0.2.112
Requires:       crate(log-0.4/default) >= 0.4.8
Requires:       crate(log-0.4/std) >= 0.4.8
Requires:       crate(time-0.3/default) >= 0.3.5
Requires:       crate(time-0.3/formatting) >= 0.3.5
Requires:       crate(time-0.3/local-offset) >= 0.3.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "syslog"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
