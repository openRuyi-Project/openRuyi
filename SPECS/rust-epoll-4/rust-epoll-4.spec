# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name epoll
%global full_version 4.4.0
%global pkgname epoll-4

Name:           rust-epoll-4
Version:        4.4.0
Release:        %autorelease
Summary:        Rust crate "epoll"
License:        MPL-2.0
URL:            https://github.com/nathansizemore/epoll
#!RemoteAsset:  sha256:e74d68fe2927dbf47aa976d14d93db9b23dced457c7bb2bdc6925a16d31b736e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "epoll"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
