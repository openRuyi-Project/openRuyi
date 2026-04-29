# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fancy-regex
%global full_version 0.13.0
%global pkgname fancy-regex-0.13

Name:           rust-fancy-regex-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "fancy-regex"
License:        MIT
URL:            https://github.com/fancy-regex/fancy-regex
#!RemoteAsset:  sha256:531e46835a22af56d1e3b66f04844bed63158bc094a628bec1d321d9b4c44bf2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-set-0.5) >= 0.5.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-syntax-0.8) >= 0.8.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/track-caller)

%description
Source code for takopackized Rust crate "fancy-regex"

%package     -n %{name}+default
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/perf)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unicode)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "perf"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/perf) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Provides:       crate(%{pkgname}/perf)

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(bit-set-0.5/std) >= 0.5.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/std) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-syntax-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-automata-0.4/unicode) >= 0.4.0
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.0
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
