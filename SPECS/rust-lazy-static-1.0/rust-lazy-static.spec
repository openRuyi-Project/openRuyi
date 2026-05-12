# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lazy_static
%global full_version 1.5.0
%global pkgname lazy-static-1.0

Name:           rust-lazy-static-1.0
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "lazy_static"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang-nursery/lazy-static.rs
#!RemoteAsset:  sha256:bbd2bcb4c963f2ddae06a2efc7e9f3591312473c50c6685e1f298068316e66fe
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "lazy_static"

%package     -n %{name}+spin
Summary:        Macro for declaring lazily evaluated statics in Rust - feature "spin" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(spin-0.9/once) >= 0.9.8
Provides:       crate(%{pkgname}/spin)
Provides:       crate(%{pkgname}/spin-no-std)

%description -n %{name}+spin
This metapackage enables feature "spin" for the Rust lazy_static crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "spin_no_std" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
