# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stacker
%global full_version 0.1.24
%global pkgname stacker-0.1

Name:           rust-stacker-0.1
Version:        0.1.24
Release:        %autorelease
Summary:        Rust crate "stacker"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/stacker
#!RemoteAsset:  sha256:640c8cdd92b6b12f5bcb1803ca3bbf5ab96e5e6b6b96b9ab77dabe9e880b3190
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.2.33
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.156
Requires:       crate(psm-0.1/default) >= 0.1.7
Requires:       crate(windows-sys-0.60/default) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-memory) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-threading) >= 0.60.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stacker"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
