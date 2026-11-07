# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thread-id
%global full_version 3.3.0
%global pkgname thread-id-3

Name:           rust-thread-id-3
Version:        3.3.0
Release:        %autorelease
Summary:        Rust crate "thread-id"
License:        MIT OR Apache-2.0
URL:            https://github.com/ruuda/thread-id
#!RemoteAsset:  sha256:c7fbf4c9d56b320106cd64fd024dadfa0be7cb4706725fc44a7d7ce952d820c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.6
Requires:       crate(redox-syscall-0.1/default) >= 0.1.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thread-id"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
