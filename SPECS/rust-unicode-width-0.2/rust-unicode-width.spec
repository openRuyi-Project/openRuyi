# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-width
%global full_version 0.2.2
%global pkgname unicode-width-0.2

Name:           rust-unicode-width-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "unicode-width"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-width
#!RemoteAsset:  sha256:b4ac048d71ede7ee76d585517add45da530660ef4390e49b098733c6e897f254
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cjk)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/no-std)

%description
Source code for takopackized Rust crate "unicode-width"

%package     -n %{name}+core
Summary:        Determine displayed width of `char` and `str` types according to Unicode Standard Annex #11 rules - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust unicode-width crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Determine displayed width of `char` and `str` types according to Unicode Standard Annex #11 rules - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/core)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust unicode-width crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Determine displayed width of `char` and `str` types according to Unicode Standard Annex #11 rules - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-std-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust unicode-width crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
