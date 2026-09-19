# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name faccess
%global full_version 0.2.4
%global pkgname faccess-0.2

Name:           rust-faccess-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "faccess"
License:        MIT
URL:            https://github.com/Freaky/faccess
#!RemoteAsset:  sha256:59ae66425802d6a903e268ae1a08b8c38ba143520f227a205edf4e9c7e3e26d5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.2.1
Requires:       crate(libc-0.2/default) >= 0.2.68
Requires:       crate(winapi-0.3/accctrl) >= 0.3.8
Requires:       crate(winapi-0.3/aclapi) >= 0.3.8
Requires:       crate(winapi-0.3/default) >= 0.3.8
Requires:       crate(winapi-0.3/handleapi) >= 0.3.8
Requires:       crate(winapi-0.3/impl-default) >= 0.3.8
Requires:       crate(winapi-0.3/minwindef) >= 0.3.8
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.8
Requires:       crate(winapi-0.3/securitybaseapi) >= 0.3.8
Requires:       crate(winapi-0.3/winbase) >= 0.3.8
Requires:       crate(winapi-0.3/winerror) >= 0.3.8
Requires:       crate(winapi-0.3/winnt) >= 0.3.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "faccess"

%files
%license LICENSE.txt
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
