# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-pemfile
%global full_version 2.2.0
%global pkgname rustls-pemfile-2

Name:           rust-rustls-pemfile-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "rustls-pemfile"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/rustls/pemfile
#!RemoteAsset:  sha256:dce314e5fee3f39953d46bb63bb8a46d40c2f8fb7cc5a3b6cab2bde9721d6e50
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-pki-types-1/default) >= 1.9.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rustls-pemfile"

%package     -n %{name}+std
Summary:        Basic .pem file parser for keys and certificates - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pki-types-1/std) >= 1.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustls-pemfile crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
