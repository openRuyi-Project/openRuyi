# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-task
%global full_version 4.7.1
%global pkgname async-task-4

Name:           rust-async-task-4
Version:        4.7.1
Release:        %autorelease
Summary:        Rust crate "async-task"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-task
#!RemoteAsset:  sha256:8b75356056920673b02621b35afd0f7dda9306d03c79a30f5c56c44cf256e3de
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "async-task"

%package     -n %{name}+portable-atomic
Summary:        Task abstraction for building executors - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust async-task crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
