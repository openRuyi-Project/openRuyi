# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cjk) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "unicode-width"

%package     -n %{name}+rustc-dep-of-std
Summary:        Determine displayed width of `char` and `str` types according to Unicode Standard Annex #11 rules - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust unicode-width crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
