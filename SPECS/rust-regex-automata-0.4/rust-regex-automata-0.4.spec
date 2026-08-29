# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/dfa-onepass) = %{version}
Provides:       crate(%{pkgname}/dfa-search) = %{version}
Provides:       crate(%{pkgname}/nfa-backtrack) = %{version}
Provides:       crate(%{pkgname}/nfa-pikevm) = %{version}
Provides:       crate(%{pkgname}/nfa-thompson) = %{version}
Provides:       crate(%{pkgname}/perf-inline) = %{version}
Provides:       crate(%{pkgname}/unicode-word-boundary) = %{version}

%description
Source code for takopackized Rust crate "regex-automata"

%package     -n %{name}+default
Summary:        Automata construction and matching using regular expressions - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dfa) = %{version}
Requires:       crate(%{pkgname}/hybrid) = %{version}
Requires:       crate(%{pkgname}/meta) = %{version}
Requires:       crate(%{pkgname}/nfa) = %{version}
Requires:       crate(%{pkgname}/perf) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/syntax) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dfa
Summary:        Automata construction and matching using regular expressions - feature "dfa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dfa-build) = %{version}
Requires:       crate(%{pkgname}/dfa-onepass) = %{version}
Requires:       crate(%{pkgname}/dfa-search) = %{version}
Provides:       crate(%{pkgname}/dfa) = %{version}

%description -n %{name}+dfa
This metapackage enables feature "dfa" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dfa-build
Summary:        Automata construction and matching using regular expressions - feature "dfa-build"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dfa-search) = %{version}
Requires:       crate(%{pkgname}/nfa-thompson) = %{version}
Provides:       crate(%{pkgname}/dfa-build) = %{version}

%description -n %{name}+dfa-build
This metapackage enables feature "dfa-build" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hybrid
Summary:        Automata construction and matching using regular expressions - feature "hybrid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/nfa-thompson) = %{version}
Provides:       crate(%{pkgname}/hybrid) = %{version}

%description -n %{name}+hybrid
This metapackage enables feature "hybrid" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+internal-instrument-pikevm
Summary:        Automata construction and matching using regular expressions - feature "internal-instrument-pikevm" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/internal-instrument) = %{version}
Provides:       crate(%{pkgname}/internal-instrument-pikevm) = %{version}

%description -n %{name}+internal-instrument-pikevm
This metapackage enables feature "internal-instrument-pikevm" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "internal-instrument" feature.

%package     -n %{name}+logging
Summary:        Automata construction and matching using regular expressions - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aho-corasick-1/logging) >= 1.0.0
Requires:       crate(log-0.4/default) >= 0.4.14
Requires:       crate(memchr-2/logging) >= 2.6.0
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+meta
Summary:        Automata construction and matching using regular expressions - feature "meta"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/nfa-pikevm) = %{version}
Requires:       crate(%{pkgname}/syntax) = %{version}
Provides:       crate(%{pkgname}/meta) = %{version}

%description -n %{name}+meta
This metapackage enables feature "meta" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nfa
Summary:        Automata construction and matching using regular expressions - feature "nfa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/nfa-backtrack) = %{version}
Requires:       crate(%{pkgname}/nfa-pikevm) = %{version}
Requires:       crate(%{pkgname}/nfa-thompson) = %{version}
Provides:       crate(%{pkgname}/nfa) = %{version}

%description -n %{name}+nfa
This metapackage enables feature "nfa" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf
Summary:        Automata construction and matching using regular expressions - feature "perf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/perf-inline) = %{version}
Requires:       crate(%{pkgname}/perf-literal) = %{version}
Provides:       crate(%{pkgname}/perf) = %{version}

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal
Summary:        Automata construction and matching using regular expressions - feature "perf-literal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/perf-literal-multisubstring) = %{version}
Requires:       crate(%{pkgname}/perf-literal-substring) = %{version}
Provides:       crate(%{pkgname}/perf-literal) = %{version}

%description -n %{name}+perf-literal
This metapackage enables feature "perf-literal" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal-multisubstring
Summary:        Automata construction and matching using regular expressions - feature "perf-literal-multisubstring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aho-corasick-1) >= 1.0.0
Provides:       crate(%{pkgname}/perf-literal-multisubstring) = %{version}

%description -n %{name}+perf-literal-multisubstring
This metapackage enables feature "perf-literal-multisubstring" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal-substring
Summary:        Automata construction and matching using regular expressions - feature "perf-literal-substring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aho-corasick-1/perf-literal) >= 1.0.0
Requires:       crate(memchr-2) >= 2.6.0
Provides:       crate(%{pkgname}/perf-literal-substring) = %{version}

%description -n %{name}+perf-literal-substring
This metapackage enables feature "perf-literal-substring" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Automata construction and matching using regular expressions - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(aho-corasick-1/std) >= 1.0.0
Requires:       crate(memchr-2/std) >= 2.6.0
Requires:       crate(regex-syntax-0.8/std) >= 0.8.5
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntax
Summary:        Automata construction and matching using regular expressions - feature "syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(regex-syntax-0.8) >= 0.8.5
Provides:       crate(%{pkgname}/syntax) = %{version}

%description -n %{name}+syntax
This metapackage enables feature "syntax" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Automata construction and matching using regular expressions - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unicode-age) = %{version}
Requires:       crate(%{pkgname}/unicode-bool) = %{version}
Requires:       crate(%{pkgname}/unicode-case) = %{version}
Requires:       crate(%{pkgname}/unicode-gencat) = %{version}
Requires:       crate(%{pkgname}/unicode-perl) = %{version}
Requires:       crate(%{pkgname}/unicode-script) = %{version}
Requires:       crate(%{pkgname}/unicode-segment) = %{version}
Requires:       crate(%{pkgname}/unicode-word-boundary) = %{version}
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.5
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-age
Summary:        Automata construction and matching using regular expressions - feature "unicode-age"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-syntax-0.8/unicode-age) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-age) = %{version}

%description -n %{name}+unicode-age
This metapackage enables feature "unicode-age" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-bool
Summary:        Automata construction and matching using regular expressions - feature "unicode-bool"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-syntax-0.8/unicode-bool) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-bool) = %{version}

%description -n %{name}+unicode-bool
This metapackage enables feature "unicode-bool" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-case
Summary:        Automata construction and matching using regular expressions - feature "unicode-case"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-syntax-0.8/unicode-case) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-case) = %{version}

%description -n %{name}+unicode-case
This metapackage enables feature "unicode-case" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-gencat
Summary:        Automata construction and matching using regular expressions - feature "unicode-gencat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-syntax-0.8/unicode-gencat) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-gencat) = %{version}

%description -n %{name}+unicode-gencat
This metapackage enables feature "unicode-gencat" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-perl
Summary:        Automata construction and matching using regular expressions - feature "unicode-perl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-syntax-0.8/unicode-perl) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-perl) = %{version}

%description -n %{name}+unicode-perl
This metapackage enables feature "unicode-perl" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-script
Summary:        Automata construction and matching using regular expressions - feature "unicode-script"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-syntax-0.8/unicode-script) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-script) = %{version}

%description -n %{name}+unicode-script
This metapackage enables feature "unicode-script" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-segment
Summary:        Automata construction and matching using regular expressions - feature "unicode-segment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-syntax-0.8/unicode-segment) >= 0.8.5
Provides:       crate(%{pkgname}/unicode-segment) = %{version}

%description -n %{name}+unicode-segment
This metapackage enables feature "unicode-segment" for the Rust regex-automata crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
