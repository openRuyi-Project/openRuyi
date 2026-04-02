# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-submodule
%global full_version 0.20.0
%global pkgname gix-submodule-0.20

Name:           rust-gix-submodule-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "gix-submodule"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:657cc5dd43cbc7a14d9c5aaf02cfbe9c2a15d077cded3f304adb30ef78852d3e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(gix-config-0.46/default) >= 0.46.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-pathspec-0.12/default) >= 0.12.0
Requires:       crate(gix-refspec-0.31/default) >= 0.31.0
Requires:       crate(gix-url-0.32/default) >= 0.32.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-submodule"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
