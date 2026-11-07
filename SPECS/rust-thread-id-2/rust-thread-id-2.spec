# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thread-id
%global full_version 2.0.0
%global pkgname thread-id-2

Name:           rust-thread-id-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "thread-id"
License:        Apache-2.0
URL:            https://github.com/ruud-v-a/thread-id
#!RemoteAsset:  sha256:a9539db560102d1cef46b8b78ce737ff0bb64e7e18d35b2a5688f7d097d0ff03
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kernel32-sys-0.2/default) >= 0.2.1
Requires:       crate(libc-0.2/default) >= 0.2.6

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thread-id"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
