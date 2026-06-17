# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name virtio-bindings
%global full_version 0.2.7
%global pkgname virtio-bindings-0.2

Name:           rust-virtio-bindings-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "virtio-bindings"
License:        BSD-3-Clause OR Apache-2.0
URL:            https://github.com/rust-vmm/vm-virtio
#!RemoteAsset:  sha256:091f1f09cfbf2a78563b562e7a949465cce1aef63b6065645188d995162f8868
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "virtio-bindings"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
