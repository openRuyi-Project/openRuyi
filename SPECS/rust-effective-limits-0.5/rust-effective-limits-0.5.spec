# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name effective-limits
%global full_version 0.5.5
%global pkgname effective-limits-0.5

Name:           rust-effective-limits-0.5
Version:        0.5.5
Release:        %autorelease
Summary:        Rust crate "effective-limits"
License:        Apache-2.0
URL:            https://github.com/rbtcollins/effective-limits.rs
#!RemoteAsset:  sha256:37195f01a7464b2bc99ba33c5b2b61929bb294632bce96987f88e2ade8e29a07
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-0.1/default) >= 0.1.10
Requires:       crate(libc-0.2/default) >= 0.2.78
Requires:       crate(sys-info-0.9/default) >= 0.9.0
Requires:       crate(thiserror-1/default) >= 1.0.20
Requires:       crate(winapi-0.3/combaseapi) >= 0.3.9
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.9
Requires:       crate(winapi-0.3/fileapi) >= 0.3.9
Requires:       crate(winapi-0.3/handleapi) >= 0.3.9
Requires:       crate(winapi-0.3/impl-default) >= 0.3.9
Requires:       crate(winapi-0.3/ioapiset) >= 0.3.9
Requires:       crate(winapi-0.3/jobapi) >= 0.3.9
Requires:       crate(winapi-0.3/jobapi2) >= 0.3.9
Requires:       crate(winapi-0.3/minwindef) >= 0.3.9
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.9
Requires:       crate(winapi-0.3/psapi) >= 0.3.9
Requires:       crate(winapi-0.3/shlobj) >= 0.3.9
Requires:       crate(winapi-0.3/shtypes) >= 0.3.9
Requires:       crate(winapi-0.3/synchapi) >= 0.3.9
Requires:       crate(winapi-0.3/sysinfoapi) >= 0.3.9
Requires:       crate(winapi-0.3/tlhelp32) >= 0.3.9
Requires:       crate(winapi-0.3/userenv) >= 0.3.9
Requires:       crate(winapi-0.3/winbase) >= 0.3.9
Requires:       crate(winapi-0.3/winerror) >= 0.3.9
Requires:       crate(winapi-0.3/winioctl) >= 0.3.9
Requires:       crate(winapi-0.3/winnt) >= 0.3.9
Requires:       crate(winapi-0.3/winuser) >= 0.3.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
how much RAM is available for use.
Source code for takopackized Rust crate "effective-limits"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
