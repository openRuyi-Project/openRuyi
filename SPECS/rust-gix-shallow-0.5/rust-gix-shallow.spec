# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-shallow
%global full_version 0.5.0
%global pkgname gix-shallow-0.5

Name:           rust-gix-shallow-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "gix-shallow"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:d936745103243ae4c510f19e0760ce73fb0f08096588fdbe0f0d7fb7ce8944b7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-lock-18.0/default) >= 18.0.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-shallow"

%package     -n %{name}+serde
Summary:        Handle files specifying the shallow boundary - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(serde-1.0/derive) >= 1.0.114
Requires:       crate(serde-1.0/std) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-shallow crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
