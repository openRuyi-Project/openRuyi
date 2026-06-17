# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lzma-rust2
%global full_version 0.16.4
%global pkgname lzma-rust2-0.16

Name:           rust-lzma-rust2-0.16
Version:        0.16.4
Release:        %autorelease
Summary:        Rust crate "lzma-rust2"
License:        Apache-2.0
URL:            https://github.com/hasenbanck/lzma-rust2/
#!RemoteAsset:  sha256:ce716bf1a316f47a280fc76295f6495b5bea4752bca01c3b3885e101b1c23c02
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/encoder) = %{version}
Provides:       crate(%{pkgname}/lzip) = %{version}
Provides:       crate(%{pkgname}/optimization) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "lzma-rust2"

%package     -n %{name}+default
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java' - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encoder) = %{version}
Requires:       crate(%{pkgname}/lzip) = %{version}
Requires:       crate(%{pkgname}/optimization) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/xz) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust lzma-rust2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java' - feature "sha2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/xz) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust lzma-rust2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "xz" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
