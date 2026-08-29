# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atty
%global full_version 0.2.14
%global pkgname atty-0.2

Name:           rust-atty-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "atty"
License:        MIT
URL:            https://github.com/softprops/atty
#!RemoteAsset:  sha256:d9b39be18770d11421cdb1b9947a45dd3f37e93092cbf377614828a319d5fee8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hermit-abi-0.1/default) >= 0.1.6
Requires:       crate(libc-0.2) >= 0.2.0
Requires:       crate(winapi-0.3/consoleapi) >= 0.3.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/minwinbase) >= 0.3.0
Requires:       crate(winapi-0.3/minwindef) >= 0.3.0
Requires:       crate(winapi-0.3/processenv) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "atty"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
