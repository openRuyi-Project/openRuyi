# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bstr
%global full_version 1.12.1
%global pkgname bstr-1.0

Name:           rust-bstr-1.0
Version:        1.12.1
Release:        %autorelease
Summary:        Rust crate "bstr"
License:        MIT OR Apache-2.0
URL:            https://github.com/BurntSushi/bstr
#!RemoteAsset:  sha256:63044e1ae8e69f3b5a92c736ca6269b8d12fa7efe39bf34ddb06d102cf0e2cab
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0) >= 2.8.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "bstr"

%package     -n %{name}+alloc
Summary:        String type that is not required to be valid UTF-8 - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/alloc) >= 2.8.0
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        String type that is not required to be valid UTF-8 - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unicode)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        String type that is not required to be valid UTF-8 - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        String type that is not required to be valid UTF-8 - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(memchr-2.0/std) >= 2.8.0
Requires:       crate(serde-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        String type that is not required to be valid UTF-8 - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(regex-automata-0.4/dfa-search) >= 0.4.14
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
