# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memmap2
%global full_version 0.9.10
%global pkgname memmap2-0.9

Name:           rust-memmap2-0.9
Version:        0.9.10
Release:        %autorelease
Summary:        Rust crate "memmap2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RazrFalcon/memmap2-rs
#!RemoteAsset:  sha256:714098028fe011992e1c3962653c96b2d578c4b4bce9036e15ff220319b1e0e3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.151
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "memmap2"

%package     -n %{name}+stable-deref-trait
Summary:        Cross-platform Rust API for memory-mapped file IO - feature "stable_deref_trait"
Requires:       crate(%{pkgname})
Requires:       crate(stable-deref-trait-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/stable-deref-trait)

%description -n %{name}+stable-deref-trait
This metapackage enables feature "stable_deref_trait" for the Rust memmap2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
