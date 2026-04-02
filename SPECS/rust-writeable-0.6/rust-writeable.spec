# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name writeable
%global full_version 0.6.2
%global pkgname writeable-0.6

Name:           rust-writeable-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "writeable"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:9edde0db4769d2dc68579893f2306b26c6ecfbe0ef499b013d731b7b9247e0b9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "writeable"

%package     -n %{name}+either
Summary:        More efficient alternative to fmt::Display - feature "either"
Requires:       crate(%{pkgname})
Requires:       crate(either-1.0) >= 1.9.0
Provides:       crate(%{pkgname}/either)

%description -n %{name}+either
This metapackage enables feature "either" for the Rust writeable crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
