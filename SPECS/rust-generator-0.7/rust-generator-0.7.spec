# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name generator
%global full_version 0.7.5
%global pkgname generator-0.7

Name:           rust-generator-0.7
Version:        0.7.5
Release:        %autorelease
Summary:        Rust crate "generator"
License:        MIT OR Apache-2.0
URL:            https://github.com/Xudong-Huang/generator-rs.git
#!RemoteAsset:  sha256:5cc16584ff22b460a382b7feec54b23d2908d858152e5739a120b949293bd74e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(rustversion-1) >= 1.0.0
Requires:       crate(windows-0.48/default) >= 0.48.0
Requires:       crate(windows-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-0.48/win32-system-diagnostics-debug) >= 0.48.0
Requires:       crate(windows-0.48/win32-system-memory) >= 0.48.0
Requires:       crate(windows-0.48/win32-system-systeminformation) >= 0.48.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "generator"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
