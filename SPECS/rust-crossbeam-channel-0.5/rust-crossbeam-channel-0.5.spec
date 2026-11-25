# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-channel
%global full_version 0.5.17
%global pkgname crossbeam-channel-0.5

Name:           rust-crossbeam-channel-0.5
Version:        0.5.17
Release:        %autorelease
Summary:        Rust crate "crossbeam-channel"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel
#!RemoteAsset:  sha256:98b0cc327b5bc766e7fda9c9260cc0fa81b43a8e240440422dff70788e3f9ef1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-utils-0.8) >= 0.8.18

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "crossbeam-channel"

%package     -n %{name}+std
Summary:        Multi-producer multi-consumer channels for message passing - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.8/std) >= 0.8.18
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust crossbeam-channel crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
