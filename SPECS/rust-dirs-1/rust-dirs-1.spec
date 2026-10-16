# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dirs
%global full_version 1.0.5
%global pkgname dirs-1

Name:           rust-dirs-1
Version:        1.0.5
Release:        %autorelease
Summary:        Rust crate "dirs"
License:        MIT OR Apache-2.0
URL:            https://github.com/soc/dirs-rs
#!RemoteAsset:  sha256:3fd78930633bd1c6e35c4b42b1df7b0cbc6bc191146e512bb3bedf243fcc3901
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(redox-users-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/knownfolders) >= 0.3.0
Requires:       crate(winapi-0.3/objbase) >= 0.3.0
Requires:       crate(winapi-0.3/shlobj) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dirs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
