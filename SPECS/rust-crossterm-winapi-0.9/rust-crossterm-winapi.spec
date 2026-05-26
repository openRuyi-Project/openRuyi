# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossterm_winapi
%global full_version 0.9.1
%global pkgname crossterm-winapi-0.9

Name:           rust-crossterm-winapi-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "crossterm_winapi"
License:        MIT
URL:            https://github.com/crossterm-rs/crossterm-winapi
#!RemoteAsset:  sha256:acdd7c62a3665c7f6830a51635d9ac9b23ed385797f70a83bb8bafe9c572ab2b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.3/consoleapi) >= 0.3.9
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/handleapi) >= 0.3.9
Requires:       crate(winapi-0.3/impl-default) >= 0.3.9
Requires:       crate(winapi-0.3/processenv) >= 0.3.9
Requires:       crate(winapi-0.3/synchapi) >= 0.3.9
Requires:       crate(winapi-0.3/winbase) >= 0.3.9
Provides:       crate(crossterm-winapi) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "crossterm_winapi"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
