# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-pathspec
%global full_version 0.12.0
%global pkgname gix-pathspec-0.12

Name:           rust-gix-pathspec-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "gix-pathspec"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:daedead611c9bd1f3640dc90a9012b45f790201788af4d659f28d94071da7fba
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-attributes-0.27/default) >= 0.27.0
Requires:       crate(gix-config-value-0.15/default) >= 0.15.3
Requires:       crate(gix-glob-0.21/default) >= 0.21.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-pathspec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
