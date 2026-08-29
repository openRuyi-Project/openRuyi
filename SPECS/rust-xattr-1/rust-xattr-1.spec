# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xattr
%global full_version 1.6.1
%global pkgname xattr-1

Name:           rust-xattr-1
Version:        1.6.1
Release:        %autorelease
Summary:        Rust crate "xattr"
License:        MIT OR Apache-2.0
URL:            https://github.com/Stebalien/xattr
#!RemoteAsset:  sha256:32e45ad4206f6d2479085147f02bc2ef834ac85886624a23575ae137c8aa8156
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.150
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(rustix-1/std) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unsupported) = %{version}

%description
Source code for takopackized Rust crate "xattr"

%prep -a
# Upstream helper scripts are packaged as source files only, not runtime executables.
find . -type f -name '*.sh' -exec chmod a-x {} +

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
