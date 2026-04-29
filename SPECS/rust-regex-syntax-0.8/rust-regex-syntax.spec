# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex-syntax
%global full_version 0.8.10
%global pkgname regex-syntax-0.8

Name:           rust-regex-syntax-0.8
Version:        0.8.10
Release:        %autorelease
Summary:        Rust crate "regex-syntax"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex/tree/master/regex-syntax
#!RemoteAsset:  sha256:dc897dd8d9e8bd1ed8cdad82b5966c3e0ecae09fb1907d58efaa013543185d0a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unicode-age)
Provides:       crate(%{pkgname}/unicode-bool)
Provides:       crate(%{pkgname}/unicode-case)
Provides:       crate(%{pkgname}/unicode-gencat)
Provides:       crate(%{pkgname}/unicode-perl)
Provides:       crate(%{pkgname}/unicode-script)
Provides:       crate(%{pkgname}/unicode-segment)

%description
Source code for takopackized Rust crate "regex-syntax"

%package     -n %{name}+arbitrary
Summary:        Regular expression parser - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.3.0
Requires:       crate(arbitrary-1.0/derive) >= 1.3.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust regex-syntax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Regular expression parser - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unicode)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust regex-syntax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Regular expression parser - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unicode-age)
Requires:       crate(%{pkgname}/unicode-bool)
Requires:       crate(%{pkgname}/unicode-case)
Requires:       crate(%{pkgname}/unicode-gencat)
Requires:       crate(%{pkgname}/unicode-perl)
Requires:       crate(%{pkgname}/unicode-script)
Requires:       crate(%{pkgname}/unicode-segment)
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust regex-syntax crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
