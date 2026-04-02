# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name valuable
%global full_version 0.1.1
%global pkgname valuable-0.1

Name:           rust-valuable-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "valuable"
License:        MIT
URL:            https://github.com/tokio-rs/valuable
#!RemoteAsset:  sha256:ba73ea9cf16a25df0c8caa16c51acb937d5712a8429db78a3ee29d5dcacd3a65
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "valuable"

%package     -n %{name}+valuable-derive
Summary:        Object-safe value inspection, used to pass un-typed structured data across trait-object boundaries - feature "valuable-derive" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(valuable-derive-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/valuable-derive)

%description -n %{name}+valuable-derive
This metapackage enables feature "valuable-derive" for the Rust valuable crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
