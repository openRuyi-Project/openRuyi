# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name str_stack
%global full_version 0.1.1
%global pkgname str-stack-0.1

Name:           rust-str-stack-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "str_stack"
License:        MIT OR Apache-2.0
URL:            https://github.com/Stebalien/str_stack
#!RemoteAsset:  sha256:7f446288b699d66d0fd2e30d1cfe7869194312524b3b9252594868ed26ef056a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
This library is primarily useful for parsing where you need to repeatedly build many strings, use them, and then throw them away. Instead of allocating many independent strings, this library will put them all in the same buffer.
Source code for takopackized Rust crate "str_stack"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
