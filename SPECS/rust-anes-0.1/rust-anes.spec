# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anes
%global full_version 0.1.6
%global pkgname anes-0.1

Name:           rust-anes-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "anes"
License:        MIT OR Apache-2.0
URL:            https://github.com/zrzka/anes-rs
#!RemoteAsset:  sha256:4b46cbb362ab8752921c97e041f5e366ee6297bd428a31275b9fcf1e380f7299
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "anes"

%package     -n %{name}+bitflags
Summary:        ANSI Escape Sequences provider & parser - feature "bitflags" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-1.0/default) >= 1.2
Provides:       crate(%{pkgname}/bitflags)
Provides:       crate(%{pkgname}/parser)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust anes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "parser" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
