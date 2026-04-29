# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name matchers
%global full_version 0.2.0
%global pkgname matchers-0.2

Name:           rust-matchers-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "matchers"
License:        MIT
URL:            https://github.com/hawkw/matchers
#!RemoteAsset:  sha256:d1525a2a28c7f4fa0fc98bb91ae755d1e2d1505079e05539e35bc876b5d65ae9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(regex-automata-0.4/dfa-build) >= 0.4.14
Requires:       crate(regex-automata-0.4/dfa-search) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "matchers"

%package     -n %{name}+unicode
Summary:        Regex matching on character and byte streams - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/dfa-build) >= 0.4.14
Requires:       crate(regex-automata-0.4/dfa-search) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Requires:       crate(regex-automata-0.4/unicode) >= 0.4.14
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust matchers crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
