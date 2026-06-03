# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dirs-sys
%global full_version 0.4.1
%global pkgname dirs-sys-0.4

Name:           rust-dirs-sys-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "dirs-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/dirs-dev/dirs-sys-rs
#!RemoteAsset:  sha256:520f05a5cbd335fae5a99ff7a6ab8627577660ee5cfd6a94a6a929b52ff0321c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

# Remove Windows-only target dependencies from Linux/RISC-V packaging; cargo
# metadata still checks target dependency sources when using a replacement registry.
Patch2000:      2000-remove-windows-target-dependencies.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.180
Requires:       crate(option-ext-0.2/default) >= 0.2.0
Requires:       crate(redox-users-0.4) >= 0.4.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "dirs-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
