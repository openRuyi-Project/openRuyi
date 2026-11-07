# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ring
%global full_version 0.16.20
%global pkgname ring-0.16

Name:           rust-ring-0.16
Version:        0.16.20
Release:        %autorelease
Summary:        Rust crate "ring"
License:        FIXME
URL:            https://github.com/briansmith/ring
#!RemoteAsset:  sha256:3053cf52e236a3ed746dfc745aa9cacf1b791d846bdaf412f60a8d7d6e17c8fc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.62
Requires:       crate(libc-0.2) >= 0.2.69
Requires:       crate(once-cell-1/std) >= 1.5.2
Requires:       crate(spin-0.5) >= 0.5.2
Requires:       crate(untrusted-0.7/default) >= 0.7.1
Requires:       crate(web-sys-0.3/crypto) >= 0.3.37
Requires:       crate(web-sys-0.3/window) >= 0.3.37
Requires:       crate(winapi-0.3/ntsecapi) >= 0.3.8
Requires:       crate(winapi-0.3/wtypesbase) >= 0.3.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/internal-benches) = %{version}
Provides:       crate(%{pkgname}/slow-tests) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/test-logging) = %{version}
Provides:       crate(%{pkgname}/wasm32-c) = %{version}

%description
Source code for takopackized Rust crate "ring"

%package     -n %{name}+default
Summary:        Safe, fast, small crypto using Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/dev-urandom-fallback) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Safe, fast, small crypto using Rust - feature "once_cell" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/std) >= 1.5.2
Provides:       crate(%{pkgname}/dev-urandom-fallback) = %{version}
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust ring crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev_urandom_fallback" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
