# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fancy-regex
%global full_version 0.16.2
%global pkgname fancy-regex-0.16

Name:           rust-fancy-regex-0.16
Version:        0.16.2
Release:        %autorelease
Summary:        Rust crate "fancy-regex"
License:        MIT
URL:            https://github.com/fancy-regex/fancy-regex
#!RemoteAsset:  sha256:998b056554fbe42e03ae0e152895cd1a7e1002aec800fdc6635d20270260c46f
Source:         https://static.crates.io/crates/fancy-regex/0.16.2/download
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-set-0.8) >= 0.8.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-syntax-0.8) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "fancy-regex"

%package     -n %{name}+default
Summary:        Implementation of regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/perf) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Requires:       crate(bit-set-0.8/std) >= 0.8.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/perf) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/std) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-automata-0.4/unicode) >= 0.4.0
Requires:       crate(regex-syntax-0.8/std) >= 0.8.0
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.0
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf
Summary:        Implementation of regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "perf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/perf) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Provides:       crate(%{pkgname}/perf) = %{version}

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Implementation of regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bit-set-0.8/std) >= 0.8.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/std) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-syntax-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+track-caller
Summary:        Implementation of regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "track_caller"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/track-caller) = %{version}

%description -n %{name}+track-caller
This metapackage enables feature "track_caller" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Implementation of regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-automata-0.4/unicode) >= 0.4.0
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.0
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
