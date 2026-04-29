# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex
%global full_version 1.12.3
%global pkgname regex-1.0

Name:           rust-regex-1.0
Version:        1.12.3
Release:        %autorelease
Summary:        Rust crate "regex"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex
#!RemoteAsset:  sha256:e10754a14b9137dd7b1e3e5b0493cc9171fdd105e0ab477f51b72e7f3ac0e276
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-syntax-0.8) >= 0.8.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/pattern)
Provides:       crate(%{pkgname}/perf-cache)
Provides:       crate(%{pkgname}/unstable)

%description
This implementation uses finite automata and guarantees linear time matching on all inputs.
Source code for takopackized Rust crate "regex"

%package     -n %{name}+default
Summary:        Regular expressions for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/perf)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unicode)
Requires:       crate(regex-syntax-0.8/default) >= 0.8.5
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "default" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Regular expressions for Rust - feature "logging"
Requires:       crate(%{pkgname})
Requires:       crate(aho-corasick-1.0/logging) >= 1.0.0
Requires:       crate(memchr-2.0/logging) >= 2.6.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/logging) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+logging
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "logging" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf
Summary:        Regular expressions for Rust - feature "perf"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/perf-backtrack)
Requires:       crate(%{pkgname}/perf-cache)
Requires:       crate(%{pkgname}/perf-dfa)
Requires:       crate(%{pkgname}/perf-inline)
Requires:       crate(%{pkgname}/perf-literal)
Requires:       crate(%{pkgname}/perf-onepass)
Provides:       crate(%{pkgname}/perf)

%description -n %{name}+perf
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "perf" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-backtrack
Summary:        Regular expressions for Rust - feature "perf-backtrack"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-backtrack) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Provides:       crate(%{pkgname}/perf-backtrack)

%description -n %{name}+perf-backtrack
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "perf-backtrack" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-dfa
Summary:        Regular expressions for Rust - feature "perf-dfa"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Provides:       crate(%{pkgname}/perf-dfa)

%description -n %{name}+perf-dfa
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "perf-dfa" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-dfa-full
Summary:        Regular expressions for Rust - feature "perf-dfa-full"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/dfa-build) >= 0.4.12
Requires:       crate(regex-automata-0.4/dfa-search) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Provides:       crate(%{pkgname}/perf-dfa-full)

%description -n %{name}+perf-dfa-full
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "perf-dfa-full" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-inline
Summary:        Regular expressions for Rust - feature "perf-inline"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/perf-inline) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Provides:       crate(%{pkgname}/perf-inline)

%description -n %{name}+perf-inline
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "perf-inline" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal
Summary:        Regular expressions for Rust - feature "perf-literal"
Requires:       crate(%{pkgname})
Requires:       crate(aho-corasick-1.0) >= 1.0.0
Requires:       crate(memchr-2.0) >= 2.6.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/perf-literal) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Provides:       crate(%{pkgname}/perf-literal)

%description -n %{name}+perf-literal
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "perf-literal" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-onepass
Summary:        Regular expressions for Rust - feature "perf-onepass"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/dfa-onepass) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Provides:       crate(%{pkgname}/perf-onepass)

%description -n %{name}+perf-onepass
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "perf-onepass" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Regular expressions for Rust - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(aho-corasick-1.0/std) >= 1.0.0
Requires:       crate(memchr-2.0/std) >= 2.6.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/std) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-syntax-0.8/std) >= 0.8.5
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/use-std)

%description -n %{name}+std
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "std" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_std" feature.

%package     -n %{name}+unicode
Summary:        Regular expressions for Rust - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unicode-age)
Requires:       crate(%{pkgname}/unicode-bool)
Requires:       crate(%{pkgname}/unicode-case)
Requires:       crate(%{pkgname}/unicode-gencat)
Requires:       crate(%{pkgname}/unicode-perl)
Requires:       crate(%{pkgname}/unicode-script)
Requires:       crate(%{pkgname}/unicode-segment)
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode) >= 0.4.12
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.5
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "unicode" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-age
Summary:        Regular expressions for Rust - feature "unicode-age"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode-age) >= 0.4.12
Requires:       crate(regex-syntax-0.8/unicode-age) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-age)

%description -n %{name}+unicode-age
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "unicode-age" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-bool
Summary:        Regular expressions for Rust - feature "unicode-bool"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode-bool) >= 0.4.12
Requires:       crate(regex-syntax-0.8/unicode-bool) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-bool)

%description -n %{name}+unicode-bool
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "unicode-bool" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-case
Summary:        Regular expressions for Rust - feature "unicode-case"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode-case) >= 0.4.12
Requires:       crate(regex-syntax-0.8/unicode-case) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-case)

%description -n %{name}+unicode-case
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "unicode-case" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-gencat
Summary:        Regular expressions for Rust - feature "unicode-gencat"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode-gencat) >= 0.4.12
Requires:       crate(regex-syntax-0.8/unicode-gencat) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-gencat)

%description -n %{name}+unicode-gencat
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "unicode-gencat" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-perl
Summary:        Regular expressions for Rust - feature "unicode-perl"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode-perl) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode-word-boundary) >= 0.4.12
Requires:       crate(regex-syntax-0.8/unicode-perl) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-perl)

%description -n %{name}+unicode-perl
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "unicode-perl" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-script
Summary:        Regular expressions for Rust - feature "unicode-script"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode-script) >= 0.4.12
Requires:       crate(regex-syntax-0.8/unicode-script) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-script)

%description -n %{name}+unicode-script
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "unicode-script" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-segment
Summary:        Regular expressions for Rust - feature "unicode-segment"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.12
Requires:       crate(regex-automata-0.4/meta) >= 0.4.12
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.12
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.12
Requires:       crate(regex-automata-0.4/unicode-segment) >= 0.4.12
Requires:       crate(regex-syntax-0.8/unicode-segment) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-segment)

%description -n %{name}+unicode-segment
This implementation uses finite automata and guarantees linear time matching on all inputs.
This metapackage enables feature "unicode-segment" for the Rust regex crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
