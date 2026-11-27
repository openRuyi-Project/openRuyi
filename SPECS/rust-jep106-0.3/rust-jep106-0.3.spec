# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jep106
%global full_version 0.3.0
%global pkgname jep106-0.3

Name:           rust-jep106-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "jep106"
License:        MIT OR Apache-2.0
URL:            https://github.com/Yatekii/jep106
#!RemoteAsset:  sha256:4a1354c92c91fd5595fd4cc46694b6914749cc90ea437246549c26b6ff0ec6d1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "jep106"

%package     -n %{name}+default
Summary:        Pollable collection of all JEP106 manufacturer codes - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust jep106 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pollable collection of all JEP106 manufacturer codes - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust jep106 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
