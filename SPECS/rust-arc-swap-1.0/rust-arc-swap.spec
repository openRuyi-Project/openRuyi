# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arc-swap
%global full_version 1.9.0
%global pkgname arc-swap-1.0

Name:           rust-arc-swap-1.0
Version:        1.9.0
Release:        %autorelease
Summary:        Rust crate "arc-swap"
License:        MIT OR Apache-2.0
URL:            https://github.com/vorner/arc-swap
#!RemoteAsset:  sha256:a07d1f37ff60921c83bdfc7407723bdefe89b44b98a9b772f225c8f9d67141a6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustversion-1.0/default) >= 1.0.22
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/experimental-strategies)
Provides:       crate(%{pkgname}/experimental-thread-local)
Provides:       crate(%{pkgname}/internal-test-strategies)
Provides:       crate(%{pkgname}/weak)

%description
Source code for takopackized Rust crate "arc-swap"

%package     -n %{name}+serde
Summary:        Atomically swappable Arc - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/rc) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust arc-swap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
