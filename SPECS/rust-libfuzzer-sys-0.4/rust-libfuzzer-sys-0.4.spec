# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libfuzzer-sys
%global full_version 0.4.13
%global pkgname libfuzzer-sys-0.4

Name:           rust-libfuzzer-sys-0.4
Version:        0.4.13
Release:        %autorelease
Summary:        Rust crate "libfuzzer-sys"
License:        (MIT OR Apache-2.0) AND NCSA
URL:            https://github.com/rust-fuzz/libfuzzer
#!RemoteAsset:  sha256:a9fd2f41a1cba099f79a0b6b6c35656cf7c03351a7bae8ff0f28f25270f929d2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arbitrary-1/default) >= 1.0.0
Requires:       crate(cc-1) >= 1.0.83
Requires:       crate(cc-1/parallel) >= 1.0.83
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/link-libfuzzer) = %{version}

%description
Source code for takopackized Rust crate "libfuzzer-sys"

%package     -n %{name}+arbitrary-derive
Summary:        Wrapper around LLVM's libFuzzer runtime - feature "arbitrary-derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary-derive) = %{version}

%description -n %{name}+arbitrary-derive
This metapackage enables feature "arbitrary-derive" for the Rust libfuzzer-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
