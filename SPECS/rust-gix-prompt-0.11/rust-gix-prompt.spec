# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-prompt
%global full_version 0.11.2
%global pkgname gix-prompt-0.11

Name:           rust-gix-prompt-0.11
Version:        0.11.2
Release:        %autorelease
Summary:        Rust crate "gix-prompt"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:868e6516dfa16fdcbc5f8c935167d085f2ae65ccd4c9476a4319579d12a69d8d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-command-0.6/default) >= 0.6.5
Requires:       crate(gix-config-value-0.15/default) >= 0.15.3
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(rustix-1.0/default) >= 1.1.4
Requires:       crate(rustix-1.0/termios) >= 1.1.4
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-prompt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
