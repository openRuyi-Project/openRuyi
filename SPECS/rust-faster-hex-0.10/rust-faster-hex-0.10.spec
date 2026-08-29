# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name faster-hex
%global full_version 0.10.0
%global pkgname faster-hex-0.10

Name:           rust-faster-hex-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "faster-hex"
License:        MIT
URL:            https://github.com/NervosFoundation/faster-hex
#!RemoteAsset:  sha256:7223ae2d2f179b803433d9c830478527e92b8117eab39460edae7f1614d9fb73
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heapless-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "faster-hex"

%package     -n %{name}+default
Summary:        Fast hex encoding - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust faster-hex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fast hex encoding - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust faster-hex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fast hex encoding - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust faster-hex crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
