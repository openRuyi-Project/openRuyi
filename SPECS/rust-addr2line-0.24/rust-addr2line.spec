# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name addr2line
%global full_version 0.24.2
%global pkgname addr2line-0.24

Name:           rust-addr2line-0.24
Version:        0.24.2
Release:        %autorelease
Summary:        Rust crate "addr2line"
License:        Apache-2.0 OR MIT
URL:            https://github.com/gimli-rs/addr2line
#!RemoteAsset:  sha256:dfbe277e56a376000877090da837660b4427aad530e3028d44e0bffe4f89a1c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gimli-0.31/read) >= 0.31.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cargo-all)

%description
Source code for takopackized Rust crate "addr2line"

%package     -n %{name}+fallible-iterator
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "fallible-iterator"
Requires:       crate(%{pkgname})
Requires:       crate(fallible-iterator-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/fallible-iterator)

%description -n %{name}+fallible-iterator
This metapackage enables feature "fallible-iterator" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-demangle
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "rustc-demangle"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-demangle-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/rustc-demangle)

%description -n %{name}+rustc-demangle
This metapackage enables feature "rustc-demangle" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "smallvec"
Requires:       crate(%{pkgname})
Requires:       crate(smallvec-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec)

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Cross-platform symbolication library written in Rust, using `gimli` - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(gimli-0.31/read) >= 0.31.1
Requires:       crate(gimli-0.31/std) >= 0.31.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust addr2line crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
