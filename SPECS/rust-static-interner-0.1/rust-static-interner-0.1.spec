# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name static_interner
%global full_version 0.1.3
%global pkgname static-interner-0.1

Name:           rust-static-interner-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "static_interner"
License:        MIT OR Apache-2.0
URL:            https://github.com/facebook/buck2
#!RemoteAsset:  sha256:c0a72d2480db611b8ee9287b4a2e0adc63c4d7fdd647d2a1a65d529fc234fd16
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(equivalent-1/default) >= 1.0.2
Requires:       crate(lock-free-hashtable-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "static_interner"

%package     -n %{name}+allocative
Summary:        Similar to `internment` crate, but with interface and performance tweaks - feature "allocative"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(allocative-0.3) >= 0.3.6
Provides:       crate(%{pkgname}/allocative) = %{version}

%description -n %{name}+allocative
This metapackage enables feature "allocative" for the Rust static_interner crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dupe
Summary:        Similar to `internment` crate, but with interface and performance tweaks - feature "dupe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dupe-0.9/default) >= 0.9.1
Provides:       crate(%{pkgname}/dupe) = %{version}

%description -n %{name}+dupe
This metapackage enables feature "dupe" for the Rust static_interner crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+strong-hash
Summary:        Similar to `internment` crate, but with interface and performance tweaks - feature "strong_hash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(strong-hash-0.1/default) >= 0.1.0
Requires:       crate(strong-hash-0.1/num-bigint) >= 0.1.0
Requires:       crate(strong-hash-0.1/triomphe) >= 0.1.0
Provides:       crate(%{pkgname}/strong-hash) = %{version}

%description -n %{name}+strong-hash
This metapackage enables feature "strong_hash" for the Rust static_interner crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
