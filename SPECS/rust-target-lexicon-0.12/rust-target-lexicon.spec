# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name target-lexicon
%global full_version 0.12.16
%global pkgname target-lexicon-0.12

Name:           rust-target-lexicon-0.12
Version:        0.12.16
Release:        %autorelease
Summary:        Rust crate "target-lexicon"
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/bytecodealliance/target-lexicon
#!RemoteAsset:  sha256:61c41af27dd6d1e27b1b16b489db798443478cef1f06a660c96db617ba5de3b1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/arch-zkasm)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "target-lexicon"

%package     -n %{name}+serde
Summary:        Targeting utilities for compilers and related tools - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust target-lexicon crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-support
Summary:        Targeting utilities for compilers and related tools - feature "serde_support"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/serde-support)

%description -n %{name}+serde-support
This metapackage enables feature "serde_support" for the Rust target-lexicon crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
