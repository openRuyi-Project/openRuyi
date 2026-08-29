# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dtor
%global full_version 0.1.1
%global pkgname dtor-0.1

Name:           rust-dtor-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "dtor"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/rust-ctor
#!RemoteAsset:  sha256:404d02eeb088a82cfd873006cb713fe411306c7d182c344905e101fb1167d301
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/no-warn-on-missing-unsafe) = %{version}
Provides:       crate(%{pkgname}/used-linker) = %{version}

%description
Source code for takopackized Rust crate "dtor"

%package     -n %{name}+default
Summary:        __attribute__((destructor)) for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/no-warn-on-missing-unsafe) = %{version}
Requires:       crate(%{pkgname}/proc-macro) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust dtor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro
Summary:        __attribute__((destructor)) for Rust - feature "proc_macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dtor-proc-macro-0.0.6/default) >= 0.0.6
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc_macro" for the Rust dtor crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
