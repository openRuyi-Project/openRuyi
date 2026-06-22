# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name const-str
%global full_version 1.1.0
%global pkgname const-str-1

Name:           rust-const-str-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "const-str"
License:        MIT
URL:            https://github.com/Nugine/const-str
#!RemoteAsset:  sha256:18f12cc9948ed9604230cdddc7c86e270f9401ccbe3c2e98a4378c5e7632212f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "const-str"

%package     -n %{name}+all
Summary:        Compile-time string operations - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/case) = %{version}
Requires:       crate(%{pkgname}/http) = %{version}
Requires:       crate(%{pkgname}/proc) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust const-str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+case
Summary:        Compile-time string operations - feature "case"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proc) = %{version}
Requires:       crate(const-str-proc-macro-1/heck) >= 1.1.0
Requires:       crate(heck-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/case) = %{version}

%description -n %{name}+case
This metapackage enables feature "case" for the Rust const-str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http
Summary:        Compile-time string operations - feature "http"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proc) = %{version}
Requires:       crate(const-str-proc-macro-1/http) >= 1.1.0
Requires:       crate(http-1/default) >= 1.4.0
Provides:       crate(%{pkgname}/http) = %{version}

%description -n %{name}+http
This metapackage enables feature "http" for the Rust const-str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc
Summary:        Compile-time string operations - feature "proc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-str-proc-macro-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/proc) = %{version}

%description -n %{name}+proc
This metapackage enables feature "proc" for the Rust const-str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Compile-time string operations - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proc) = %{version}
Requires:       crate(const-str-proc-macro-1/regex) >= 1.1.0
Requires:       crate(regex-1/default) >= 1.12.2
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust const-str crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
