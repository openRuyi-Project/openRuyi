# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytecheck
%global full_version 0.6.12
%global pkgname bytecheck-0.6

Name:           rust-bytecheck-0.6
Version:        0.6.12
Release:        %autorelease
Summary:        Rust crate "bytecheck"
License:        MIT
URL:            https://github.com/djkoloski/bytecheck
#!RemoteAsset:  sha256:23cdc57ce23ac53c931e88a43d06d070a6fd142f2617be5855eb75efc9beb1c2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytecheck-derive-0.6) >= 0.6.12
Requires:       crate(ptr-meta-0.1) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/verbose) = %{version}

%description
Source code for takopackized Rust crate "bytecheck"

%package     -n %{name}+default
Summary:        Derive macro for bytecheck - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/simdutf8) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bytecheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simdutf8
Summary:        Derive macro for bytecheck - feature "simdutf8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simdutf8-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/simdutf8) = %{version}

%description -n %{name}+simdutf8
This metapackage enables feature "simdutf8" for the Rust bytecheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Derive macro for bytecheck - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-derive-0.6/std) >= 0.6.12
Requires:       crate(ptr-meta-0.1/std) >= 0.1.0
Requires:       crate(simdutf8-0.1/std) >= 0.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bytecheck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Derive macro for bytecheck - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust bytecheck crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
