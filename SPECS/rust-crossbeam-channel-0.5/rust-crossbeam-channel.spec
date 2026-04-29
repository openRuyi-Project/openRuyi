# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-channel
%global full_version 0.5.15
%global pkgname crossbeam-channel-0.5

Name:           rust-crossbeam-channel-0.5
Version:        0.5.15
Release:        %autorelease
Summary:        Rust crate "crossbeam-channel"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel
#!RemoteAsset:  sha256:82b8f8f868b36967f9606790d1903570de9ceaf870a7bf9fbbd3016d636a2cb2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-utils-0.8) >= 0.8.21
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "crossbeam-channel"

%package     -n %{name}+std
Summary:        Multi-producer multi-consumer channels for message passing - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(crossbeam-utils-0.8/std) >= 0.8.21
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust crossbeam-channel crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
