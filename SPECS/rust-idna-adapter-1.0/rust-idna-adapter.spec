# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name idna_adapter
%global full_version 1.2.1
%global pkgname idna-adapter-1.0

Name:           rust-idna-adapter-1.0
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "idna_adapter"
License:        Apache-2.0 OR MIT
URL:            https://docs.rs/crate/idna_adapter/latest
#!RemoteAsset:  sha256:3acae9609540aa318d1bc588455225fb2085b9ed0c4f6bd0d9d5bcd86f1a0344
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(icu-normalizer-2.0) >= 2.2.0
Requires:       crate(icu-properties-2.0) >= 2.2.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "idna_adapter"

%package     -n %{name}+compiled-data
Summary:        Back end adapter for idna - feature "compiled_data"
Requires:       crate(%{pkgname})
Requires:       crate(icu-normalizer-2.0/compiled-data) >= 2.2.0
Requires:       crate(icu-properties-2.0/compiled-data) >= 2.2.0
Provides:       crate(%{pkgname}/compiled-data)

%description -n %{name}+compiled-data
This metapackage enables feature "compiled_data" for the Rust idna_adapter crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
