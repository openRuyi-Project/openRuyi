# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lalrpop
%global full_version 0.20.2
%global pkgname lalrpop-0.20

Name:           rust-lalrpop-0.20
Version:        0.20.2
Release:        %autorelease
Summary:        Rust crate "lalrpop"
License:        Apache-2.0 OR MIT
URL:            https://github.com/lalrpop/lalrpop
#!RemoteAsset:  sha256:55cb077ad656299f160924eb2912aa147d7339ea7d69e1b5517326fdcec3c1ca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ascii-canvas-3) >= 3.0.0
Requires:       crate(bit-set-0.5) >= 0.5.2
Requires:       crate(ena-0.14) >= 0.14.0
Requires:       crate(itertools-0.11/use-std) >= 0.11.0
Requires:       crate(lalrpop-util-0.20) >= 0.20.0
Requires:       crate(petgraph-0.6) >= 0.6.0
Requires:       crate(regex-1/std) >= 1.3.0
Requires:       crate(regex-syntax-0.8) >= 0.8.0
Requires:       crate(string-cache-0.8) >= 0.8.0
Requires:       crate(term-0.7) >= 0.7.0
Requires:       crate(tiny-keccak-2/default) >= 2.0.2
Requires:       crate(tiny-keccak-2/sha3) >= 2.0.2
Requires:       crate(unicode-xid-0.2) >= 0.2.0
Requires:       crate(walkdir-2/default) >= 2.4.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "lalrpop"

%package     -n %{name}+default
Summary:        Convenient LR(1) parser generator - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lexer) = %{version}
Requires:       crate(%{pkgname}/pico-args) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust lalrpop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lexer
Summary:        Convenient LR(1) parser generator - feature "lexer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lalrpop-util-0.20/lexer) >= 0.20.0
Provides:       crate(%{pkgname}/lexer) = %{version}

%description -n %{name}+lexer
This metapackage enables feature "lexer" for the Rust lalrpop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pico-args
Summary:        Convenient LR(1) parser generator - feature "pico-args"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pico-args-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/pico-args) = %{version}

%description -n %{name}+pico-args
This metapackage enables feature "pico-args" for the Rust lalrpop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Convenient LR(1) parser generator - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lalrpop-util-0.20/unicode) >= 0.20.0
Requires:       crate(regex-1/std) >= 1.3.0
Requires:       crate(regex-1/unicode) >= 1.3.0
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.0
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust lalrpop crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
