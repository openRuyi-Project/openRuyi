# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sval_nested
%global full_version 2.22.0
%global pkgname sval-nested-2

Name:           rust-sval-nested-2
Version:        2.22.0
Release:        %autorelease
Summary:        Rust crate "sval_nested"
License:        Apache-2.0 OR MIT
URL:            https://github.com/sval-rs/sval
#!RemoteAsset:  sha256:07c059969ca5ca163ea7fef6c9661758973d17691aba92abdcf5c428f4ec122c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sval-2/default) >= 2.22.0
Requires:       crate(sval-buffer-2) >= 2.22.0
Requires:       crate(sval-ref-2/default) >= 2.22.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/no-debug-assertions) = %{version}

%description
Source code for takopackized Rust crate "sval_nested"

%package     -n %{name}+alloc
Summary:        Recursive variant of sval - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-2/alloc) >= 2.22.0
Requires:       crate(sval-buffer-2/alloc) >= 2.22.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sval_nested crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+std
Summary:        Recursive variant of sval - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(sval-2/std) >= 2.22.0
Requires:       crate(sval-buffer-2/std) >= 2.22.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sval_nested crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
