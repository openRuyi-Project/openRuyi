# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name diplomat
%global full_version 0.16.0
%global pkgname diplomat-0.16

Name:           rust-diplomat-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "diplomat"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-diplomat/diplomat
#!RemoteAsset:  sha256:26fdfa02eb9a2e1ff82a375524be1ce9fd50ae63787f5737da6951b25d21e857
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(diplomat-core-0.16) >= 0.16.0
Requires:       crate(proc-macro2-1/default) >= 1.0.27
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-3/default) >= 3.0.0
Requires:       crate(syn-3/extra-traits) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "diplomat"

%package     -n %{name}+pretty-print
Summary:        Diplomat FFI generation macro - feature "pretty-print"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(diplomat-core-0.16/pretty-print) >= 0.16.0
Provides:       crate(%{pkgname}/pretty-print) = %{version}

%description -n %{name}+pretty-print
This metapackage enables feature "pretty-print" for the Rust diplomat crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
