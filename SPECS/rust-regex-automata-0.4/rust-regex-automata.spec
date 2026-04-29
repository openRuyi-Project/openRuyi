# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex-automata
%global full_version 0.4.14
%global pkgname regex-automata-0.4

Name:           rust-regex-automata-0.4
Version:        0.4.14
Release:        %autorelease
Summary:        Rust crate "regex-automata"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex/tree/master/regex-automata
#!RemoteAsset:  sha256:6e1dd4122fc1595e8162618945476892eefca7b88c52820e74af6262213cae8f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/dfa-onepass)
Provides:       crate(%{pkgname}/dfa-search)
Provides:       crate(%{pkgname}/nfa-backtrack)
Provides:       crate(%{pkgname}/nfa-pikevm)
Provides:       crate(%{pkgname}/nfa-thompson)
Provides:       crate(%{pkgname}/perf-inline)
Provides:       crate(%{pkgname}/unicode-word-boundary)

%description
Source code for takopackized Rust crate "regex-automata"

%package     -n %{name}+default
Summary:        Automata construction and matching using regular expressions - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/dfa)
Requires:       crate(%{pkgname}/hybrid)
Requires:       crate(%{pkgname}/meta)
Requires:       crate(%{pkgname}/nfa)
Requires:       crate(%{pkgname}/perf)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/syntax)
Requires:       crate(%{pkgname}/unicode)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dfa
Summary:        Automata construction and matching using regular expressions - feature "dfa"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/dfa-build)
Requires:       crate(%{pkgname}/dfa-onepass)
Requires:       crate(%{pkgname}/dfa-search)
Provides:       crate(%{pkgname}/dfa)

%description -n %{name}+dfa
This metapackage enables feature "dfa" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dfa-build
Summary:        Automata construction and matching using regular expressions - feature "dfa-build"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/dfa-search)
Requires:       crate(%{pkgname}/nfa-thompson)
Provides:       crate(%{pkgname}/dfa-build)

%description -n %{name}+dfa-build
This metapackage enables feature "dfa-build" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hybrid
Summary:        Automata construction and matching using regular expressions - feature "hybrid"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/nfa-thompson)
Provides:       crate(%{pkgname}/hybrid)

%description -n %{name}+hybrid
This metapackage enables feature "hybrid" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+internal-instrument-pikevm
Summary:        Automata construction and matching using regular expressions - feature "internal-instrument-pikevm" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/logging)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/internal-instrument)
Provides:       crate(%{pkgname}/internal-instrument-pikevm)

%description -n %{name}+internal-instrument-pikevm
This metapackage enables feature "internal-instrument-pikevm" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "internal-instrument" feature.

%package     -n %{name}+logging
Summary:        Automata construction and matching using regular expressions - feature "logging"
Requires:       crate(%{pkgname})
Requires:       crate(aho-corasick-1.0/logging) >= 1.1.4
Requires:       crate(log-0.4/default) >= 0.4.14
Requires:       crate(memchr-2.0/logging) >= 2.8.0
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+meta
Summary:        Automata construction and matching using regular expressions - feature "meta"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/nfa-pikevm)
Requires:       crate(%{pkgname}/syntax)
Provides:       crate(%{pkgname}/meta)

%description -n %{name}+meta
This metapackage enables feature "meta" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nfa
Summary:        Automata construction and matching using regular expressions - feature "nfa"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/nfa-backtrack)
Requires:       crate(%{pkgname}/nfa-pikevm)
Requires:       crate(%{pkgname}/nfa-thompson)
Provides:       crate(%{pkgname}/nfa)

%description -n %{name}+nfa
This metapackage enables feature "nfa" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf
Summary:        Automata construction and matching using regular expressions - feature "perf"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/perf-inline)
Requires:       crate(%{pkgname}/perf-literal)
Provides:       crate(%{pkgname}/perf)

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal
Summary:        Automata construction and matching using regular expressions - feature "perf-literal"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/perf-literal-multisubstring)
Requires:       crate(%{pkgname}/perf-literal-substring)
Provides:       crate(%{pkgname}/perf-literal)

%description -n %{name}+perf-literal
This metapackage enables feature "perf-literal" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal-multisubstring
Summary:        Automata construction and matching using regular expressions - feature "perf-literal-multisubstring"
Requires:       crate(%{pkgname})
Requires:       crate(aho-corasick-1.0) >= 1.1.4
Provides:       crate(%{pkgname}/perf-literal-multisubstring)

%description -n %{name}+perf-literal-multisubstring
This metapackage enables feature "perf-literal-multisubstring" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal-substring
Summary:        Automata construction and matching using regular expressions - feature "perf-literal-substring"
Requires:       crate(%{pkgname})
Requires:       crate(aho-corasick-1.0/perf-literal) >= 1.1.4
Requires:       crate(memchr-2.0) >= 2.8.0
Provides:       crate(%{pkgname}/perf-literal-substring)

%description -n %{name}+perf-literal-substring
This metapackage enables feature "perf-literal-substring" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Automata construction and matching using regular expressions - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(aho-corasick-1.0/std) >= 1.1.4
Requires:       crate(memchr-2.0/std) >= 2.8.0
Requires:       crate(regex-syntax-0.8/std) >= 0.8.10
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntax
Summary:        Automata construction and matching using regular expressions - feature "syntax"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(regex-syntax-0.8) >= 0.8.10
Provides:       crate(%{pkgname}/syntax)

%description -n %{name}+syntax
This metapackage enables feature "syntax" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Automata construction and matching using regular expressions - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unicode-age)
Requires:       crate(%{pkgname}/unicode-bool)
Requires:       crate(%{pkgname}/unicode-case)
Requires:       crate(%{pkgname}/unicode-gencat)
Requires:       crate(%{pkgname}/unicode-perl)
Requires:       crate(%{pkgname}/unicode-script)
Requires:       crate(%{pkgname}/unicode-segment)
Requires:       crate(%{pkgname}/unicode-word-boundary)
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.10
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-age
Summary:        Automata construction and matching using regular expressions - feature "unicode-age"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/unicode-age) >= 0.8.10
Provides:       crate(%{pkgname}/unicode-age)

%description -n %{name}+unicode-age
This metapackage enables feature "unicode-age" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-bool
Summary:        Automata construction and matching using regular expressions - feature "unicode-bool"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/unicode-bool) >= 0.8.10
Provides:       crate(%{pkgname}/unicode-bool)

%description -n %{name}+unicode-bool
This metapackage enables feature "unicode-bool" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-case
Summary:        Automata construction and matching using regular expressions - feature "unicode-case"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/unicode-case) >= 0.8.10
Provides:       crate(%{pkgname}/unicode-case)

%description -n %{name}+unicode-case
This metapackage enables feature "unicode-case" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-gencat
Summary:        Automata construction and matching using regular expressions - feature "unicode-gencat"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/unicode-gencat) >= 0.8.10
Provides:       crate(%{pkgname}/unicode-gencat)

%description -n %{name}+unicode-gencat
This metapackage enables feature "unicode-gencat" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-perl
Summary:        Automata construction and matching using regular expressions - feature "unicode-perl"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/unicode-perl) >= 0.8.10
Provides:       crate(%{pkgname}/unicode-perl)

%description -n %{name}+unicode-perl
This metapackage enables feature "unicode-perl" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-script
Summary:        Automata construction and matching using regular expressions - feature "unicode-script"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/unicode-script) >= 0.8.10
Provides:       crate(%{pkgname}/unicode-script)

%description -n %{name}+unicode-script
This metapackage enables feature "unicode-script" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-segment
Summary:        Automata construction and matching using regular expressions - feature "unicode-segment"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/unicode-segment) >= 0.8.10
Provides:       crate(%{pkgname}/unicode-segment)

%description -n %{name}+unicode-segment
This metapackage enables feature "unicode-segment" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
