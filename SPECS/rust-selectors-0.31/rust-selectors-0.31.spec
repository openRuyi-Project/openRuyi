# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name selectors
%global full_version 0.31.0
%global pkgname selectors-0.31

Name:           rust-selectors-0.31
Version:        0.31.0
Release:        %autorelease
Summary:        Rust crate "selectors"
License:        MPL-2.0
URL:            https://github.com/servo/stylo
#!RemoteAsset:  sha256:5685b6ae43bfcf7d2e7dfcfb5d8e8f61b46442c902531e41a32a9a8bf0ee0fb6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(cssparser-0.35/default) >= 0.35.0
Requires:       crate(derive-more-2/add) >= 2.0.0
Requires:       crate(derive-more-2/add-assign) >= 2.0.0
Requires:       crate(derive-more-2/default) >= 2.0.0
Requires:       crate(fxhash-0.2/default) >= 0.2.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(new-debug-unreachable-1/default) >= 1.0.0
Requires:       crate(phf-0.11/default) >= 0.11.0
Requires:       crate(phf-codegen-0.11) >= 0.11.0
Requires:       crate(precomputed-hash-0.1/default) >= 0.1.0
Requires:       crate(servo-arc-0.4/default) >= 0.4.0
Requires:       crate(smallvec-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "selectors"

%package     -n %{name}+to-shmem
Summary:        CSS Selectors matching for Rust - feature "to_shmem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(to-shmem-0.2/default) >= 0.2.0
Requires:       crate(to-shmem-0.2/servo-arc) >= 0.2.0
Requires:       crate(to-shmem-derive-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/to-shmem) = %{version}

%description -n %{name}+to-shmem
This metapackage enables feature "to_shmem" for the Rust selectors crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
