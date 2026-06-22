# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name embedded-io
%global full_version 0.6.1
%global pkgname embedded-io-0.6

Name:           rust-embedded-io-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "embedded-io"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/embedded-hal
#!RemoteAsset:  sha256:edd0f118536f44f5ccd48bcb8b111bdc3de888b58c74639dfb034a357d0f206d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "embedded-io"

%package     -n %{name}+defmt-03
Summary:        Embedded IO traits - feature "defmt-03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/defmt-03) = %{version}

%description -n %{name}+defmt-03
This metapackage enables feature "defmt-03" for the Rust embedded-io crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
