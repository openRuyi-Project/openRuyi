# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ff
%global full_version 0.13.1
%global pkgname ff-0.13

Name:           rust-ff-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "ff"
License:        MIT/Apache-2.0
URL:            https://github.com/zkcrypto/ff
#!RemoteAsset:  sha256:c0b50bfb653653f9ca9095b427bed08ab8d75a137839d9ad64eb11810d5b6393
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.6) >= 0.6.4
Requires:       crate(subtle-2.0/i128) >= 2.6.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "ff"

%package     -n %{name}+bitvec
Summary:        Building and interfacing with finite fields - feature "bitvec" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bitvec-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bits)
Provides:       crate(%{pkgname}/bitvec)

%description -n %{name}+bitvec
This metapackage enables feature "bitvec" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bits" feature.

%package     -n %{name}+byteorder
Summary:        Building and interfacing with finite fields - feature "byteorder"
Requires:       crate(%{pkgname})
Requires:       crate(byteorder-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/byteorder)

%description -n %{name}+byteorder
This metapackage enables feature "byteorder" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Building and interfacing with finite fields - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bits)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Building and interfacing with finite fields - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/byteorder)
Requires:       crate(%{pkgname}/ff-derive)
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive-bits
Summary:        Building and interfacing with finite fields - feature "derive_bits"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bits)
Requires:       crate(ff-derive-0.13/bits) >= 0.13.1
Provides:       crate(%{pkgname}/derive-bits)

%description -n %{name}+derive-bits
This metapackage enables feature "derive_bits" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ff-derive
Summary:        Building and interfacing with finite fields - feature "ff_derive"
Requires:       crate(%{pkgname})
Requires:       crate(ff-derive-0.13/default) >= 0.13.1
Provides:       crate(%{pkgname}/ff-derive)

%description -n %{name}+ff-derive
This metapackage enables feature "ff_derive" for the Rust ff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
