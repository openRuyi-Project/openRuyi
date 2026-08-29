# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zune-jpeg
%global full_version 0.4.21
%global pkgname zune-jpeg-0.4

Name:           rust-zune-jpeg-0.4
Version:        0.4.21
Release:        %autorelease
Summary:        Rust crate "zune-jpeg"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/etemesi254/zune-image/tree/dev/crates/zune-jpeg
#!RemoteAsset:  sha256:29ce2c8a9384ad323cf564b67da86e21d3cfdff87908bc1223ed5c99bc792713
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zune-core-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/neon) = %{version}
Provides:       crate(%{pkgname}/x86) = %{version}

%description
Source code for takopackized Rust crate "zune-jpeg"

%package     -n %{name}+default
Summary:        Fast, correct and safe jpeg decoder - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/neon) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/x86) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zune-jpeg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Fast, correct and safe jpeg decoder - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zune-core-0.4/log) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust zune-jpeg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fast, correct and safe jpeg decoder - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zune-core-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust zune-jpeg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
