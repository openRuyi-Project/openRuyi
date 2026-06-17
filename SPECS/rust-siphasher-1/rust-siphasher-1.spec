# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name siphasher
%global full_version 1.0.3
%global pkgname siphasher-1

Name:           rust-siphasher-1
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "siphasher"
License:        MIT OR Apache-2.0
URL:            https://docs.rs/siphasher
#!RemoteAsset:  sha256:8ee5873ec9cce0195efcb7a4e9507a04cd49aec9c83d0389df45b1ef7ba2e649
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "siphasher"

%package     -n %{name}+serde
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust siphasher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust siphasher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-no-std
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust - feature "serde_no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde-no-std) = %{version}

%description -n %{name}+serde-no-std
This metapackage enables feature "serde_no_std" for the Rust siphasher crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-std
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust - feature "serde_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-std) = %{version}

%description -n %{name}+serde-std
This metapackage enables feature "serde_std" for the Rust siphasher crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
