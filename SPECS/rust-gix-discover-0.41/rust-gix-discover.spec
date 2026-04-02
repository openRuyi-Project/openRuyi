# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-discover
%global full_version 0.41.0
%global pkgname gix-discover-0.41

Name:           rust-gix-discover-0.41
Version:        0.41.0
Release:        %autorelease
Summary:        Rust crate "gix-discover"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:ffb180c91ca1a2cf53e828bb63d8d8f8fa7526f49b83b33d7f46cbeb5d79d30a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(bstr-1.0/unicode) >= 1.12.1
Requires:       crate(dunce-1.0/default) >= 1.0.5
Requires:       crate(gix-fs-0.16/default) >= 0.16.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-ref-0.53/default) >= 0.53.1
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-discover"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
