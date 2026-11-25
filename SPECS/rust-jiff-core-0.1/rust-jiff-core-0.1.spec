# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiff-core
%global full_version 0.1.0
%global pkgname jiff-core-0.1

Name:           rust-jiff-core-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "jiff-core"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff/tree/master/crates/jiff-core
#!RemoteAsset:  sha256:7feca88439efe53da3754500c1851dedf3cb36c524dd5cf8225cc0794de95d09
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/tz-fat) = %{version}

%description
Source code for takopackized Rust crate "jiff-core"

%package     -n %{name}+alloc
Summary:        Low level datetime primitives for the Jiff library - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust jiff-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+default
Summary:        Low level datetime primitives for the Jiff library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tz-fat) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust jiff-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+defmt
Summary:        Low level datetime primitives for the Jiff library - feature "defmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/defmt) = %{version}

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust jiff-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Low level datetime primitives for the Jiff library - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.21
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust jiff-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
