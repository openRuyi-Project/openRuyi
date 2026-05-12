# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winnow
%global full_version 0.7.15
%global pkgname winnow-0.7

Name:           rust-winnow-0.7
Version:        0.7.15
Release:        %autorelease
Summary:        Rust crate "winnow"
License:        MIT
URL:            https://github.com/winnow-rs/winnow
#!RemoteAsset:  sha256:df79d97927682d2fd8adb29682d1140b343be4ac0f08fd68b7765d9c059d3945
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/unstable-recover)

%description
Source code for takopackized Rust crate "winnow"

%package     -n %{name}+debug
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(anstream-0.6/default) >= 0.6.15
Requires:       crate(anstyle-1.0/default) >= 1.0.8
Requires:       crate(is-terminal-polyfill-1.0/default) >= 1.48.1
Requires:       crate(terminal-size-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "simd"
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0) >= 2.7
Provides:       crate(%{pkgname}/simd)

%description -n %{name}+simd
This metapackage enables feature "simd" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(memchr-2.0/std) >= 2.7
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unstable-doc
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "unstable-doc"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/simd)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unstable-recover)
Provides:       crate(%{pkgname}/unstable-doc)

%description -n %{name}+unstable-doc
This metapackage enables feature "unstable-doc" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
