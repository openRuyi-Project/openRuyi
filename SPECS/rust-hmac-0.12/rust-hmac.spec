# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hmac
%global full_version 0.12.1
%global pkgname hmac-0.12

Name:           rust-hmac-0.12
Version:        0.12.1
Release:        %autorelease
Summary:        Rust crate "hmac"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/MACs
#!RemoteAsset:  sha256:6c49c37c09c17a53d937dfbb742eb3a961d65a994e6bcdcf37e7399d0cc8ab5e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.10/default) >= 0.10.7
Requires:       crate(digest-0.10/mac) >= 0.10.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/reset)

%description
Source code for takopackized Rust crate "hmac"

%package     -n %{name}+std
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC) - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/mac) >= 0.10.7
Requires:       crate(digest-0.10/std) >= 0.10.7
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust hmac crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
