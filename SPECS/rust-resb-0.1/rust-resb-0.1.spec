# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name resb
%global full_version 0.1.2
%global pkgname resb-0.1

Name:           rust-resb-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "resb"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:22d392791f3c6802a1905a509e9d1a6039cbbcb5e9e00e5a6d3661f7c874f390
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(potential-utf-0.1) >= 0.1.3
Requires:       crate(serde-core-1/alloc) >= 1.0.220

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "resb"

%package     -n %{name}+logging
Summary:        Utilities for reading and writing ICU resource bundle files - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.17
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust resb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+text
Summary:        Utilities for reading and writing ICU resource bundle files - feature "text"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(nom-7/default) >= 7.0.0
Provides:       crate(%{pkgname}/text) = %{version}

%description -n %{name}+text
This metapackage enables feature "text" for the Rust resb crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
