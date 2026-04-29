# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-targets
%global full_version 0.53.5
%global pkgname windows-targets-0.53

Name:           rust-windows-targets-0.53
Version:        0.53.5
Release:        %autorelease
Summary:        Rust crate "windows-targets"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:4945f9f551b88e0d65f3db0bc25c33b8acea4d9e41163edf90dcd0b19f9069f3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-aarch64-gnullvm-0.53/default) >= 0.53.1
Requires:       crate(windows-aarch64-msvc-0.53/default) >= 0.53.1
Requires:       crate(windows-i686-gnu-0.53/default) >= 0.53.1
Requires:       crate(windows-i686-gnullvm-0.53/default) >= 0.53.1
Requires:       crate(windows-i686-msvc-0.53/default) >= 0.53.1
Requires:       crate(windows-link-0.2) >= 0.2.1
Requires:       crate(windows-x86-64-gnu-0.53/default) >= 0.53.1
Requires:       crate(windows-x86-64-gnullvm-0.53/default) >= 0.53.1
Requires:       crate(windows-x86-64-msvc-0.53/default) >= 0.53.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "windows-targets"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
