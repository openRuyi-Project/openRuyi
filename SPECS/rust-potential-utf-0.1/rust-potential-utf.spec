# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name potential_utf
%global full_version 0.1.5
%global pkgname potential-utf-0.1

Name:           rust-potential-utf-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "potential_utf"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:0103b1cef7ec0cf76490e969665504990193874ea05c85ff9bab8b911d0a0564
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "potential_utf"

%package     -n %{name}+alloc
Summary:        Unvalidated string and character types - feature "alloc" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/alloc) >= 1.0.220
Requires:       crate(writeable-0.6/alloc) >= 0.6.1
Requires:       crate(zerovec-0.11/alloc) >= 0.11.6
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust potential_utf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+databake
Summary:        Unvalidated string and character types - feature "databake"
Requires:       crate(%{pkgname})
Requires:       crate(databake-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/databake)

%description -n %{name}+databake
This metapackage enables feature "databake" for the Rust potential_utf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Unvalidated string and character types - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.220
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust potential_utf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+writeable
Summary:        Unvalidated string and character types - feature "writeable"
Requires:       crate(%{pkgname})
Requires:       crate(writeable-0.6) >= 0.6.1
Provides:       crate(%{pkgname}/writeable)

%description -n %{name}+writeable
This metapackage enables feature "writeable" for the Rust potential_utf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerovec
Summary:        Unvalidated string and character types - feature "zerovec"
Requires:       crate(%{pkgname})
Requires:       crate(zerovec-0.11) >= 0.11.6
Provides:       crate(%{pkgname}/zerovec)

%description -n %{name}+zerovec
This metapackage enables feature "zerovec" for the Rust potential_utf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
