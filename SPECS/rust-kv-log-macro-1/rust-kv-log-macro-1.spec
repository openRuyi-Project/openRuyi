# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kv-log-macro
%global full_version 1.0.7
%global pkgname kv-log-macro-1

Name:           rust-kv-log-macro-1
Version:        1.0.7
Release:        %autorelease
Summary:        Rust crate "kv-log-macro"
License:        MIT OR Apache-2.0
URL:            https://github.com/yoshuawuyts/kv-log-macro
#!RemoteAsset:  sha256:0de8b303297635ad57c9f5059fd9cee7a47f8e8daa09df0fcd07dd39fb22977f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.8
Requires:       crate(log-0.4/kv-unstable) >= 0.4.8
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "kv-log-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
