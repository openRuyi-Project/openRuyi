# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name waker-fn
%global full_version 1.2.0
%global pkgname waker-fn-1

Name:           rust-waker-fn-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "waker-fn"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/waker-fn
#!RemoteAsset:  sha256:317211a0dc0ceedd78fb2ca9a44aed3d7b9b26f81870d485c07122b4350673b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "waker-fn"

%package     -n %{name}+portable-atomic-util
Summary:        Convert closures into wakers - feature "portable-atomic-util" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-util-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}
Provides:       crate(%{pkgname}/portable-atomic-util) = %{version}

%description -n %{name}+portable-atomic-util
This metapackage enables feature "portable-atomic-util" for the Rust waker-fn crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "portable-atomic" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
