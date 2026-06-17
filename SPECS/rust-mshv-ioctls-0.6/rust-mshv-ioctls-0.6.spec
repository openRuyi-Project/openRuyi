# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mshv-ioctls
%global full_version 0.6.9
%global pkgname mshv-ioctls-0.6

Name:           rust-mshv-ioctls-0.6
Version:        0.6.9
Release:        %autorelease
Summary:        Rust crate "mshv-ioctls"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/mshv
#!RemoteAsset:  sha256:1db4449ac7012237b133da366f5b32ce4af1f8caf770486e5a9d54f7f6b73c4c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(mshv-bindings-0.6/default) >= 0.6.9
Requires:       crate(mshv-bindings-0.6/fam-wrappers) >= 0.6.9
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(vmm-sys-util-0.12/default) >= 0.12.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mshv-ioctls"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
