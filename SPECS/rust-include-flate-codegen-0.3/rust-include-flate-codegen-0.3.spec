# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name include-flate-codegen
%global full_version 0.3.4
%global pkgname include-flate-codegen-0.3

Name:           rust-include-flate-codegen-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "include-flate-codegen"
License:        Apache-2.0
URL:            https://github.com/SOF3/include-flate
#!RemoteAsset:  sha256:4a7875b62a72ad3f3203cdd8950d4cf9947db036030b974b8b37ceae90c8d8c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(include-flate-compress-0.3) >= 0.3.1
Requires:       crate(proc-macro-error3-3/default) >= 3.0.2
Requires:       crate(proc-macro2-1/default) >= 1.0.95
Requires:       crate(quote-1/default) >= 1.0.40
Requires:       crate(syn-2/default) >= 2.0.104
Requires:       crate(syn-2/full) >= 2.0.104

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/no-compression-warnings) = %{version}

%description
Source code for takopackized Rust crate "include-flate-codegen"

%package     -n %{name}+default
Summary:        Macro codegen for the include-flate crate - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust include-flate-codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Macro codegen for the include-flate crate - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-flate-compress-0.3/deflate) >= 0.3.1
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust include-flate-codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Macro codegen for the include-flate crate - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-flate-compress-0.3/zstd) >= 0.3.1
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust include-flate-codegen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
