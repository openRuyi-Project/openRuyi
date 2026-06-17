# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aho-corasick
%global full_version 1.1.4
%global pkgname aho-corasick-1

Name:           rust-aho-corasick-1
Version:        1.1.4
Release:        %autorelease
Summary:        Rust crate "aho-corasick"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/aho-corasick
#!RemoteAsset:  sha256:ddd31a130427c27518df266943a5308ed92d4b226cc639f5a8f1002816174301
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "aho-corasick"

%package     -n %{name}+default
Summary:        Fast multiple substring searching - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/perf-literal) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust aho-corasick crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Fast multiple substring searching - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.17
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust aho-corasick crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal
Summary:        Fast multiple substring searching - feature "perf-literal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2) >= 2.4.0
Provides:       crate(%{pkgname}/perf-literal) = %{version}

%description -n %{name}+perf-literal
This metapackage enables feature "perf-literal" for the Rust aho-corasick crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fast multiple substring searching - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/std) >= 2.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust aho-corasick crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
