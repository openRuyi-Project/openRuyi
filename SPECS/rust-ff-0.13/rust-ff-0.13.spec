# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ff
%global full_version 0.13.1
%global pkgname ff-0.13

Name:           rust-ff-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "ff"
License:        MIT OR Apache-2.0
URL:            https://github.com/zkcrypto/ff
#!RemoteAsset:  sha256:c0b50bfb653653f9ca9095b427bed08ab8d75a137839d9ad64eb11810d5b6393
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.6) >= 0.6.0
Requires:       crate(subtle-2/i128) >= 2.2.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ff"

%package     -n %{name}+bitvec
Summary:        Building and interfacing with finite fields - feature "bitvec" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitvec-1) >= 1.0.0
Provides:       crate(%{pkgname}/bits) = %{version}
Provides:       crate(%{pkgname}/bitvec) = %{version}

%description -n %{name}+bitvec
This metapackage enables feature "bitvec" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bits" feature.

%package     -n %{name}+byteorder
Summary:        Building and interfacing with finite fields - feature "byteorder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(byteorder-1) >= 1.0.0
Provides:       crate(%{pkgname}/byteorder) = %{version}

%description -n %{name}+byteorder
This metapackage enables feature "byteorder" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Building and interfacing with finite fields - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bits) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Building and interfacing with finite fields - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/byteorder) = %{version}
Requires:       crate(%{pkgname}/ff-derive) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive-bits
Summary:        Building and interfacing with finite fields - feature "derive_bits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bits) = %{version}
Requires:       crate(ff-derive-0.13/bits) >= 0.13.1
Provides:       crate(%{pkgname}/derive-bits) = %{version}

%description -n %{name}+derive-bits
This metapackage enables feature "derive_bits" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ff-derive
Summary:        Building and interfacing with finite fields - feature "ff_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ff-derive-0.13/default) >= 0.13.1
Provides:       crate(%{pkgname}/ff-derive) = %{version}

%description -n %{name}+ff-derive
This metapackage enables feature "ff_derive" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
