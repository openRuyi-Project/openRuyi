# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global crate_name read-process-memory
%global full_version 0.1.6
%global pkgname read-process-memory-0.1

Name:           rust-read-process-memory-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "read-process-memory"
License:        MIT
URL:            https://github.com/rbspy/read-process-memory
#!RemoteAsset:  sha256:8497683b2f0b6887786f1928c118f26ecc6bb3d78bbb6ed23e8e7ba110af3bb0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "read-process-memory"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
