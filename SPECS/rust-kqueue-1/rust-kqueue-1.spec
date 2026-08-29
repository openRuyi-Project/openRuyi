# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kqueue
%global full_version 1.1.1
%global pkgname kqueue-1

Name:           rust-kqueue-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "kqueue"
License:        MIT
URL:            https://gitlab.com/rust-kqueue/rust-kqueue
#!RemoteAsset:  sha256:eac30106d7dce88daf4a3fcb4879ea939476d5074a9b7ddd0fb97fa4bed5596a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kqueue-sys-1/default) >= 1.0.4
Requires:       crate(libc-0.2/default) >= 0.2.17
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "kqueue"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
