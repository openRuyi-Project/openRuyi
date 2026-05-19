# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name siphasher
%global full_version 1.0.1
%global pkgname siphasher-1.0

Name:           rust-siphasher-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "siphasher"
License:        MIT/Apache-2.0
URL:            https://docs.rs/siphasher
#!RemoteAsset:  sha256:56199f7ddabf13fe5074ce809e7d3f42b42ae711800501b5b16ea82ad029c39d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "siphasher"

%package     -n %{name}+serde
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust siphasher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust - feature "serde_json"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json)

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust siphasher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-no-std
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust - feature "serde_no_std"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde-no-std)

%description -n %{name}+serde-no-std
This metapackage enables feature "serde_no_std" for the Rust siphasher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-std
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust - feature "serde_std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(serde-1.0/derive) >= 1.0.0
Requires:       crate(serde-1.0/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-std)

%description -n %{name}+serde-std
This metapackage enables feature "serde_std" for the Rust siphasher crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
