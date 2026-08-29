# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fontconfig-parser
%global full_version 0.5.8
%global pkgname fontconfig-parser-0.5

Name:           rust-fontconfig-parser-0.5
Version:        0.5.8
Release:        %autorelease
Summary:        Rust crate "fontconfig-parser"
License:        MIT
URL:            https://github.com/Riey/fontconfig-parser
#!RemoteAsset:  sha256:bbc773e24e02d4ddd8395fd30dc147524273a83e54e0f312d986ea30de5f5646
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(roxmltree-0.20/default) >= 0.20.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fontconfig-parser"

%package     -n %{name}+log
Summary:        Fontconfig file parser in pure Rust - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust fontconfig-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fontconfig file parser in pure Rust - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust fontconfig-parser crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
