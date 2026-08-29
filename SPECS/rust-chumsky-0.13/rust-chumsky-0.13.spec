# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chumsky
%global full_version 0.13.0
%global pkgname chumsky-0.13

Name:           rust-chumsky-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "chumsky"
License:        MIT
URL:            https://codeberg.org/zesterer/chumsky
#!RemoteAsset:  sha256:e0d2bfadce76f963d776feff99db6dc33783829539258314776383b33e2a00f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.15/default) >= 0.15.0
Requires:       crate(unicode-ident-1/default) >= 1.0.10
Requires:       crate(unicode-segmentation-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/docsrs) = %{version}
Provides:       crate(%{pkgname}/extension) = %{version}
Provides:       crate(%{pkgname}/memoization) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/pratt) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "chumsky"

%package     -n %{name}+test-stable
Summary:        Parser library for humans with powerful error recovery - feature "_test_stable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(%{pkgname}/either) = %{version}
Requires:       crate(%{pkgname}/extension) = %{version}
Requires:       crate(%{pkgname}/memoization) = %{version}
Requires:       crate(%{pkgname}/pratt) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/stacker) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/test-stable) = %{version}

%description -n %{name}+test-stable
This metapackage enables feature "_test_stable" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Parser library for humans with powerful error recovery - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Parser library for humans with powerful error recovery - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/nightly) = %{version}
Requires:       crate(%{pkgname}/unstable) = %{version}
Requires:       crate(railroad-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Parser library for humans with powerful error recovery - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/stacker) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either
Summary:        Parser library for humans with powerful error recovery - feature "either"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(either-1/default) >= 1.8.1
Provides:       crate(%{pkgname}/either) = %{version}

%description -n %{name}+either
This metapackage enables feature "either" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lexical
Summary:        Parser library for humans with powerful error recovery - feature "lexical"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-6/format) >= 6.1.1
Requires:       crate(lexical-6/parse-floats) >= 6.1.1
Requires:       crate(lexical-6/parse-integers) >= 6.1.1
Provides:       crate(%{pkgname}/lexical) = %{version}

%description -n %{name}+lexical
This metapackage enables feature "lexical" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lexical-numbers
Summary:        Parser library for humans with powerful error recovery - feature "lexical-numbers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lexical) = %{version}
Requires:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/lexical-numbers) = %{version}

%description -n %{name}+lexical-numbers
This metapackage enables feature "lexical-numbers" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Parser library for humans with powerful error recovery - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/perf) >= 0.4.0
Requires:       crate(regex-automata-0.4/unicode) >= 0.4.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Parser library for humans with powerful error recovery - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stacker
Summary:        Parser library for humans with powerful error recovery - feature "stacker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(stacker-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/stacker) = %{version}

%description -n %{name}+stacker
This metapackage enables feature "stacker" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Parser library for humans with powerful error recovery - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.0
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/perf) >= 0.4.0
Requires:       crate(regex-automata-0.4/std) >= 0.4.0
Requires:       crate(regex-automata-0.4/unicode) >= 0.4.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust chumsky crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
