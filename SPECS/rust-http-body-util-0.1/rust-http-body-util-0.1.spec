# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name http-body-util
%global full_version 0.1.3
%global pkgname http-body-util-0.1

Name:           rust-http-body-util-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "http-body-util"
License:        MIT
URL:            https://github.com/hyperium/http-body
#!RemoteAsset:  sha256:b021d93e26becf5dc7e1b75b1bed1fd93124b374ceb73f43d4d4eafec896a64a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(http-body-1/default) >= 1.0.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "http-body-util"

%package     -n %{name}+channel
Summary:        Combinators and adapters for HTTP request or response bodies - feature "channel" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Provides:       crate(%{pkgname}/channel) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+channel
This metapackage enables feature "channel" for the Rust http-body-util crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "full" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
