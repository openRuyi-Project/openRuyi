# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fuchsia-zircon-sys
%global full_version 0.3.3
%global pkgname fuchsia-zircon-sys-0.3

Name:           rust-fuchsia-zircon-sys-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "fuchsia-zircon-sys"
License:        BSD-3-Clause
URL:            https://fuchsia.googlesource.com/garnet/
#!RemoteAsset:  sha256:3dcaa9ae7725d12cdb85b3ad99a434db70b468c09ded17e012d86b5c1010f7a7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fuchsia-zircon-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
