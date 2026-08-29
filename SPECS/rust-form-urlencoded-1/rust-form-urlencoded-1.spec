# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name form_urlencoded
%global full_version 1.2.2
%global pkgname form-urlencoded-1

Name:           rust-form-urlencoded-1
Version:        1.2.2
Release:        %autorelease
Summary:        Rust crate "form_urlencoded"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url
#!RemoteAsset:  sha256:cb4cb245038516f5f85277875cdaa4f7d2c9a0fa0468de06ed190163b1581fcf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(percent-encoding-2) >= 2.3.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "form_urlencoded"

%package     -n %{name}+alloc
Summary:        Parser and serializer for the application/x-www-form-urlencoded syntax, as used by HTML forms - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(percent-encoding-2/alloc) >= 2.3.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust form_urlencoded crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Parser and serializer for the application/x-www-form-urlencoded syntax, as used by HTML forms - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(percent-encoding-2/std) >= 2.3.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust form_urlencoded crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
