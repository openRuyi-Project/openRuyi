# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexical-util
%global full_version 1.0.7
%global pkgname lexical-util-1.0

Name:           rust-lexical-util-1.0
Version:        1.0.7
Release:        %autorelease
Summary:        Rust crate "lexical-util"
License:        MIT/Apache-2.0
URL:            https://github.com/Alexhuszagh/rust-lexical
#!RemoteAsset:  sha256:2604dd126bb14f13fb5d1bd6a66155079cb9fa655b37f875b3a742c705dbed17
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/compact)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/format)
Provides:       crate(%{pkgname}/lint)
Provides:       crate(%{pkgname}/parse-floats)
Provides:       crate(%{pkgname}/parse-integers)
Provides:       crate(%{pkgname}/power-of-two)
Provides:       crate(%{pkgname}/radix)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/write-floats)
Provides:       crate(%{pkgname}/write-integers)

%description
Source code for takopackized Rust crate "lexical-util"

%package     -n %{name}+f128
Summary:        Shared utilities for lexical creates - feature "f128"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/parse-floats)
Requires:       crate(%{pkgname}/write-floats)
Provides:       crate(%{pkgname}/f128)

%description -n %{name}+f128
This metapackage enables feature "f128" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f16
Summary:        Shared utilities for lexical creates - feature "f16"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/float16)
Requires:       crate(%{pkgname}/parse-floats)
Requires:       crate(%{pkgname}/write-floats)
Provides:       crate(%{pkgname}/f16)

%description -n %{name}+f16
This metapackage enables feature "f16" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+float16
Summary:        Shared utilities for lexical creates - feature "float16"
Requires:       crate(%{pkgname})
Requires:       crate(float16-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/float16)

%description -n %{name}+float16
This metapackage enables feature "float16" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
