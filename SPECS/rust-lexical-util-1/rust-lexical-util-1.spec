# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexical-util
%global full_version 1.0.7
%global pkgname lexical-util-1

Name:           rust-lexical-util-1
Version:        1.0.7
Release:        %autorelease
Summary:        Rust crate "lexical-util"
License:        MIT OR Apache-2.0
URL:            https://github.com/Alexhuszagh/rust-lexical
#!RemoteAsset:  sha256:2604dd126bb14f13fb5d1bd6a66155079cb9fa655b37f875b3a742c705dbed17
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compact) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/format) = %{version}
Provides:       crate(%{pkgname}/lint) = %{version}
Provides:       crate(%{pkgname}/parse-floats) = %{version}
Provides:       crate(%{pkgname}/parse-integers) = %{version}
Provides:       crate(%{pkgname}/power-of-two) = %{version}
Provides:       crate(%{pkgname}/radix) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/write-floats) = %{version}
Provides:       crate(%{pkgname}/write-integers) = %{version}

%description
Source code for takopackized Rust crate "lexical-util"

%package     -n %{name}+f128
Summary:        Shared utilities for lexical creates - feature "f128"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parse-floats) = %{version}
Requires:       crate(%{pkgname}/write-floats) = %{version}
Provides:       crate(%{pkgname}/f128) = %{version}

%description -n %{name}+f128
This metapackage enables feature "f128" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f16
Summary:        Shared utilities for lexical creates - feature "f16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/float16) = %{version}
Requires:       crate(%{pkgname}/parse-floats) = %{version}
Requires:       crate(%{pkgname}/write-floats) = %{version}
Provides:       crate(%{pkgname}/f16) = %{version}

%description -n %{name}+f16
This metapackage enables feature "f16" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+float16
Summary:        Shared utilities for lexical creates - feature "float16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(float16-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/float16) = %{version}

%description -n %{name}+float16
This metapackage enables feature "float16" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
