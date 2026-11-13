# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name      open-enum
%global full_version    0.3.0
%global pkgname         open-enum-0.3

Name:           rust-open-enum-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "open-enum"
License:        Apache-2.0
URL:            https://github.com/kupiakos/open-enum
#!RemoteAsset:  sha256:9807f1199cf84ec7cc801a79e5ee9aa5178e4762c6b9c7066c30b3cabdcd911e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

Requires:       crate(open-enum-derive-0.3/default) >= 0.3.0

%description
Source code for takopackized Rust crate "open-enum"

%package     -n %{name}+libc
Summary:        Attribute for generating "open" fieldless enums, those that accept any integer value, by using a newtype struct and associated constants - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust open-enum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc-
Summary:        Attribute for generating "open" fieldless enums, those that accept any integer value, by using a newtype struct and associated constants - feature "libc_"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(open-enum-derive-0.3/repr-c) >= 0.3.0
Provides:       crate(%{pkgname}/libc-) = %{version}

%description -n %{name}+libc-
This metapackage enables feature "libc_" for the Rust open-enum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Attribute for generating "open" fieldless enums, those that accept any integer value, by using a newtype struct and associated constants - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(open-enum-derive-0.3/repr-c) >= 0.3.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust open-enum crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
