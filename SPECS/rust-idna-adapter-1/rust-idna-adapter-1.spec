# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name idna_adapter
%global full_version 1.2.1
%global pkgname idna-adapter-1

Name:           rust-idna-adapter-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "idna_adapter"
License:        Apache-2.0 OR MIT
URL:            https://docs.rs/crate/idna_adapter/latest
#!RemoteAsset:  sha256:3acae9609540aa318d1bc588455225fb2085b9ed0c4f6bd0d9d5bcd86f1a0344
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(icu-normalizer-2) >= 2.0.0
Requires:       crate(icu-properties-2) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "idna_adapter"

%package     -n %{name}+compiled-data
Summary:        Back end adapter for idna - feature "compiled_data"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-normalizer-2/compiled-data) >= 2.0.0
Requires:       crate(icu-properties-2/compiled-data) >= 2.0.0
Provides:       crate(%{pkgname}/compiled-data) = %{version}

%description -n %{name}+compiled-data
This metapackage enables feature "compiled_data" for the Rust idna_adapter crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
