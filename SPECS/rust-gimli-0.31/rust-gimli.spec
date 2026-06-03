# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gimli
%global full_version 0.31.1
%global pkgname gimli-0.31

Name:           rust-gimli-0.31
Version:        0.31.1
Release:        %autorelease
Summary:        Rust crate "gimli"
License:        MIT OR Apache-2.0
URL:            https://github.com/gimli-rs/gimli
#!RemoteAsset:  sha256:07e28edb80900c19c28f1072f2e8aeca7fa06b23cd4169cefe1af5aa3260783f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/read)
Provides:       crate(%{pkgname}/read-core)

%description
Source code for takopackized Rust crate "gimli"

%package     -n %{name}+default
Summary:        Reading and writing the DWARF debugging format - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/read-all)
Requires:       crate(%{pkgname}/write)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+endian-reader
Summary:        Reading and writing the DWARF debugging format - feature "endian-reader"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/read)
Requires:       crate(stable-deref-trait-1.0) >= 1.1.0
Provides:       crate(%{pkgname}/endian-reader)

%description -n %{name}+endian-reader
This metapackage enables feature "endian-reader" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fallible-iterator
Summary:        Reading and writing the DWARF debugging format - feature "fallible-iterator"
Requires:       crate(%{pkgname})
Requires:       crate(fallible-iterator-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/fallible-iterator)

%description -n %{name}+fallible-iterator
This metapackage enables feature "fallible-iterator" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+read-all
Summary:        Reading and writing the DWARF debugging format - feature "read-all"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/endian-reader)
Requires:       crate(%{pkgname}/fallible-iterator)
Requires:       crate(%{pkgname}/read)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/read-all)

%description -n %{name}+read-all
This metapackage enables feature "read-all" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Reading and writing the DWARF debugging format - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(fallible-iterator-0.3/std) >= 0.3.0
Requires:       crate(stable-deref-trait-1.0/std) >= 1.1.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write
Summary:        Reading and writing the DWARF debugging format - feature "write"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/default) >= 2.0.0
Provides:       crate(%{pkgname}/write)

%description -n %{name}+write
This metapackage enables feature "write" for the Rust gimli crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
