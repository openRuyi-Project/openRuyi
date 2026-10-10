# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name embedded-hal
%global full_version 1.0.0
%global pkgname embedded-hal-1

Name:           rust-embedded-hal-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "embedded-hal"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/embedded-hal
#!RemoteAsset:  sha256:361a90feb7004eca4019fb28352a9465666b24f840f5c3cddf0ff13920590b89
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "embedded-hal"

%package     -n %{name}+defmt-03
Summary:        Hardware Abstraction Layer (HAL) for embedded systems - feature "defmt-03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/defmt-03) = %{version}

%description -n %{name}+defmt-03
This metapackage enables feature "defmt-03" for the Rust embedded-hal crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
