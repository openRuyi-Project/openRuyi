# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_locale_data
%global full_version 2.2.0
%global pkgname icu-locale-data-2

Name:           rust-icu-locale-data-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_locale_data"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:d5fdcc9ac77c6d74ff5cf6e65ef3181d6af32003b16fce3a77fb451d2f695993
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "icu_locale_data"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
