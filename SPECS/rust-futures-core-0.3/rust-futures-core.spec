# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-core
%global full_version 0.3.32
%global pkgname futures-core-0.3

Name:           rust-futures-core-0.3
Version:        0.3.32
Release:        %autorelease
Summary:        Rust crate "futures-core"
License:        MIT OR Apache-2.0
URL:            https://rust-lang.github.io/futures-rs
#!RemoteAsset:  sha256:7e3450815272ef58cec6d564423f6e755e25379b217b0bc688e295ba24df6b1d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/cfg-target-has-atomic)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "futures-core"

%package     -n %{name}+portable-atomic
Summary:        Core traits and types in for the `futures` library - feature "portable-atomic"
Requires:       crate(%{pkgname})
Requires:       crate(portable-atomic-1.0/require-cas) >= 1.3
Provides:       crate(%{pkgname}/portable-atomic)

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust futures-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
