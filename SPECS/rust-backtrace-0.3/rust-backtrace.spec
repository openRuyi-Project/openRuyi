# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name backtrace
%global full_version 0.3.76
%global pkgname backtrace-0.3

Name:           rust-backtrace-0.3
Version:        0.3.76
Release:        %autorelease
Summary:        Rust crate "backtrace"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/backtrace-rs
#!RemoteAsset:  sha256:bb531853791a215d7c62a30daf0dde835f381ab5de4589cfe7c649d2cbe92bd6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(addr2line-0.25) >= 0.25.1
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2) >= 0.2.186
Requires:       crate(miniz-oxide-0.8) >= 0.8.9
Requires:       crate(object-0.37/archive) >= 0.37.3
Requires:       crate(object-0.37/elf) >= 0.37.3
Requires:       crate(object-0.37/macho) >= 0.37.3
Requires:       crate(object-0.37/pe) >= 0.37.3
Requires:       crate(object-0.37/read-core) >= 0.37.3
Requires:       crate(object-0.37/unaligned) >= 0.37.3
Requires:       crate(object-0.37/xcoff) >= 0.37.3
Requires:       crate(rustc-demangle-0.1/default) >= 0.1.27
Requires:       crate(windows-link-0.2/default) >= 0.2.1
Provides:       crate(backtrace) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/coresymbolication)
Provides:       crate(%{pkgname}/dbghelp)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/dl-iterate-phdr)
Provides:       crate(%{pkgname}/dladdr)
Provides:       crate(%{pkgname}/kernel32)
Provides:       crate(%{pkgname}/libunwind)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unix-backtrace)

%description
Source code for takopackized Rust crate "backtrace"

%package     -n %{name}+cpp-demangle
Summary:        Acquire a stack trace (backtrace) at runtime in a Rust program - feature "cpp_demangle"
Requires:       crate(%{pkgname})
Requires:       crate(cpp-demangle-0.5/alloc) >= 0.5.0
Provides:       crate(%{pkgname}/cpp-demangle)

%description -n %{name}+cpp-demangle
This metapackage enables feature "cpp_demangle" for the Rust backtrace crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ruzstd
Summary:        Acquire a stack trace (backtrace) at runtime in a Rust program - feature "ruzstd"
Requires:       crate(%{pkgname})
Requires:       crate(ruzstd-0.8) >= 0.8.1
Provides:       crate(%{pkgname}/ruzstd)

%description -n %{name}+ruzstd
This metapackage enables feature "ruzstd" for the Rust backtrace crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Acquire a stack trace (backtrace) at runtime in a Rust program - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/serialize-serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust backtrace crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize-serde" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
