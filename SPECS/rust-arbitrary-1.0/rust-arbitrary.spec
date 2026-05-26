# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arbitrary
%global full_version 1.4.2
%global pkgname arbitrary-1.0

Name:           rust-arbitrary-1.0
Version:        1.4.2
Release:        %autorelease
Summary:        Rust crate "arbitrary"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-fuzz/arbitrary/
#!RemoteAsset:  sha256:c3d036a3c4ab069c7b410a2ce876bd74808d2d0888a82667669f8e783a898bf1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(arbitrary) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "arbitrary"

%package     -n %{name}+derive-arbitrary
Summary:        Trait for generating structured data from unstructured data - feature "derive_arbitrary" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(derive-arbitrary-1.0/default) >= 1.4.0
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/derive-arbitrary)

%description -n %{name}+derive-arbitrary
This metapackage enables feature "derive_arbitrary" for the Rust arbitrary crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
