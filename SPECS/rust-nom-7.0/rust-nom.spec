# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nom
%global full_version 7.1.3
%global pkgname nom-7.0

Name:           rust-nom-7.0
Version:        7.1.3
Release:        %autorelease
Summary:        Rust crate "nom"
License:        MIT
URL:            https://github.com/Geal/nom
#!RemoteAsset:  sha256:d273983c5a657a70a3e8f2a01329822f3b8c8172b73826411a55751e404a0a4a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0) >= 2.3
Requires:       crate(minimal-lexical-0.2) >= 0.2.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/docsrs)

%description
Source code for takopackized Rust crate "nom"

%package     -n %{name}+std
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(memchr-2.0/std) >= 2.3
Requires:       crate(minimal-lexical-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust nom crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
