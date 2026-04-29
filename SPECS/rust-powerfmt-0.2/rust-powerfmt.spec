# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name powerfmt
%global full_version 0.2.0
%global pkgname powerfmt-0.2

Name:           rust-powerfmt-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "powerfmt"
License:        MIT OR Apache-2.0
URL:            https://github.com/jhpratt/powerfmt
#!RemoteAsset:  sha256:439ee305def115ba05938db6eb1644ff94165c5ab5e9420d1c1bcedbba909391
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)

%description
This crate makes it     significantly easier to support filling to a minimum width with alignment, avoid heap     allocation, and avoid repetitive calculations.
Source code for takopackized Rust crate "powerfmt"

%package     -n %{name}+default
Summary:        `powerfmt` is a library that provides utilities for formatting values - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This crate makes it     significantly easier to support filling to a minimum width with alignment, avoid heap     allocation, and avoid repetitive calculations.
This metapackage enables feature "default" for the Rust powerfmt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        `powerfmt` is a library that provides utilities for formatting values - feature "macros"
Requires:       crate(%{pkgname})
Requires:       crate(powerfmt-macros-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
This crate makes it     significantly easier to support filling to a minimum width with alignment, avoid heap     allocation, and avoid repetitive calculations.
This metapackage enables feature "macros" for the Rust powerfmt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
