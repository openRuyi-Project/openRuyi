# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name embedded-io
%global full_version 0.7.1
%global pkgname embedded-io-0.7

Name:           rust-embedded-io-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "embedded-io"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/embedded-hal
#!RemoteAsset:  sha256:9eb1aa714776b75c7e67e1da744b81a129b3ff919c8712b5e1b32252c1f07cc7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for the Rust crate "embedded-io"

%package     -n %{name}+defmt
Summary:        Embedded IO traits - feature "defmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/defmt) = %{version}

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust embedded-io crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE-APACHE LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
