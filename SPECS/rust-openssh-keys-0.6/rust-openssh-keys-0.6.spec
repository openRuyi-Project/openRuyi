# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssh-keys
%global full_version 0.6.5
%global pkgname openssh-keys-0.6

Name:           rust-openssh-keys-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "openssh-keys"
License:        MIT OR Apache-2.0
URL:            https://github.com/coreos/openssh-keys
#!RemoteAsset:  sha256:351339c4d45e6bdf2defef3ef1ce0b153810bd59b171b92b6a42e7bb0f32a4ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(byteorder-1/default) >= 1.1.0
Requires:       crate(md-5-0.10/default) >= 0.10.0
Requires:       crate(sha2-0.10/default) >= 0.10.0
Requires:       crate(thiserror-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "openssh-keys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
