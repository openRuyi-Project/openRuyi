# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-index
%global full_version 0.41.0
%global pkgname gix-index-0.41

Name:           rust-gix-index-0.41
Version:        0.41.0
Release:        %autorelease
Summary:        Rust crate "gix-index"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:2af39fde3ce4ce11371d9ce826f2936ec347318f2d1972fe98c2e7134e267e25
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(bstr-1) >= 1.12.0
Requires:       crate(filetime-0.2/default) >= 0.2.15
Requires:       crate(fnv-1/default) >= 1.0.7
Requires:       crate(gix-bitmap-0.2/default) >= 0.2.14
Requires:       crate(gix-features-0.43/default) >= 0.43.0
Requires:       crate(gix-features-0.43/progress) >= 0.43.0
Requires:       crate(gix-fs-0.16/default) >= 0.16.0
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-lock-18/default) >= 18.0.0
Requires:       crate(gix-object-0.50/default) >= 0.50.0
Requires:       crate(gix-traverse-0.47/default) >= 0.47.0
Requires:       crate(gix-utils-0.3/default) >= 0.3.0
Requires:       crate(gix-validate-0.10/default) >= 0.10.0
Requires:       crate(hashbrown-0.15/default) >= 0.15.4
Requires:       crate(itoa-1/default) >= 1.0.3
Requires:       crate(libc-0.2/default) >= 0.2.174
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Requires:       crate(rustix-1/fs) >= 1.0.7
Requires:       crate(rustix-1/std) >= 1.0.7
Requires:       crate(smallvec-1/default) >= 1.15.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-index"

%package     -n %{name}+document-features
Summary:        Work-in-progress crate of the gitoxide project dedicated implementing the git index file - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-index crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Work-in-progress crate of the gitoxide project dedicated implementing the git index file - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(serde-1/derive) >= 1.0.114
Requires:       crate(smallvec-1/serde) >= 1.15.1
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-index crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
