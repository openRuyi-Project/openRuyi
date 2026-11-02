# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sval_buffer
%global full_version 2.22.0
%global pkgname sval-buffer-2

Name:           rust-sval-buffer-2
Version:        2.22.0
Release:        %autorelease
Summary:        Rust crate "sval_buffer"
License:        Apache-2.0 OR MIT
URL:            https://github.com/sval-rs/sval
#!RemoteAsset:  sha256:50be352d2822ffafb59e3e2ddac9d5ee60f2eeadbb7b5a2a951b9f3651e87a6f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sval-2/default) >= 2.22.0
Requires:       crate(sval-ref-2/default) >= 2.22.0
Requires:       crate(zerocopy-0.8/default) >= 0.8.0
Requires:       crate(zerocopy-0.8/derive) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/no-debug-assertions) = %{version}

%description
Source code for takopackized Rust crate "sval_buffer"

%package     -n %{name}+alloc
Summary:        Value buffering for sval - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-2/alloc) >= 2.22.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sval_buffer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+std
Summary:        Value buffering for sval - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(sval-2/std) >= 2.22.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sval_buffer crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
