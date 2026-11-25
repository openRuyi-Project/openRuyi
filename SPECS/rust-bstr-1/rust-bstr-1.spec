# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bstr
%global full_version 1.13.1
%global pkgname bstr-1

Name:           rust-bstr-1
Version:        1.13.1
Release:        %autorelease
Summary:        Rust crate "bstr"
License:        MIT OR Apache-2.0
URL:            https://github.com/BurntSushi/bstr
#!RemoteAsset:  sha256:6bb31b46c14244e20ee9984b11bf5c992b91fb6939fea616e3512c8baecdbe5f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2) >= 2.7.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bstr"

%package     -n %{name}+alloc
Summary:        String type that is not required to be valid UTF-8 - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/alloc) >= 2.7.1
Requires:       crate(serde-core-1/alloc) >= 1.0.85
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        String type that is not required to be valid UTF-8 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        String type that is not required to be valid UTF-8 - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.85
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        String type that is not required to be valid UTF-8 - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(memchr-2/std) >= 2.7.1
Requires:       crate(serde-core-1/std) >= 1.0.85
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        String type that is not required to be valid UTF-8 - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/dfa-search) >= 0.4.1
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
