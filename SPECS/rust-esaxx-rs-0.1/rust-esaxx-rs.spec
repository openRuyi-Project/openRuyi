# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name esaxx-rs
%global full_version 0.1.10
%global pkgname esaxx-rs-0.1

Name:           rust-esaxx-rs-0.1
Version:        0.1.10
Release:        %autorelease
Summary:        Rust crate "esaxx-rs"
License:        Apache-2.0
URL:            https://github.com/Narsil/esaxx-rs
#!RemoteAsset:  sha256:d817e038c30374a4bcb22f94d0a8a0e216958d4c3dcde369b1439fec4bdda6e6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "esaxx-rs"

%package     -n %{name}+cc
Summary:        Wrapping around sentencepiece's esaxxx library - feature "cc" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(cc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/cc)
Provides:       crate(%{pkgname}/cpp)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust esaxx-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cpp", and "default" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
