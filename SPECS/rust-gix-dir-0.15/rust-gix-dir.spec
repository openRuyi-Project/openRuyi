# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-dir
%global full_version 0.15.0
%global pkgname gix-dir-0.15

Name:           rust-gix-dir-0.15
Version:        0.15.0
Release:        %autorelease
Summary:        Rust crate "gix-dir"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:dad34e4f373f94902df1ba1d2a1df3a1b29eacd15e316ac5972d842e31422dd7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(gix-discover-0.41/default) >= 0.41.0
Requires:       crate(gix-fs-0.16/default) >= 0.16.1
Requires:       crate(gix-ignore-0.16/default) >= 0.16.0
Requires:       crate(gix-index-0.41/default) >= 0.41.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-pathspec-0.12/default) >= 0.12.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-utils-0.3/bstr) >= 0.3.1
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(gix-worktree-0.42) >= 0.42.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-dir"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
