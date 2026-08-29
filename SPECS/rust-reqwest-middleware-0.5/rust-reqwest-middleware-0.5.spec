# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name reqwest-middleware
%global full_version 0.5.2
%global pkgname reqwest-middleware-0.5

Name:           rust-reqwest-middleware-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "reqwest-middleware"
License:        MIT OR Apache-2.0
URL:            https://github.com/TrueLayer/reqwest-middleware
#!RemoteAsset:  sha256:07bc3f1384cffa4f274dad2d4ddd73aed32fed8f786d96c6be8aa4e5fd3c3b58
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(async-trait-0.1/default) >= 0.1.51
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(reqwest-0.13) >= 0.13.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "reqwest-middleware"

%package     -n %{name}+charset
Summary:        Wrapper around reqwest to allow for client middleware chains - feature "charset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/charset) >= 0.13.1
Provides:       crate(%{pkgname}/charset) = %{version}

%description -n %{name}+charset
This metapackage enables feature "charset" for the Rust reqwest-middleware crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+form
Summary:        Wrapper around reqwest to allow for client middleware chains - feature "form"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/form) >= 0.13.1
Requires:       crate(serde-1/default) >= 1.0.106
Provides:       crate(%{pkgname}/form) = %{version}

%description -n %{name}+form
This metapackage enables feature "form" for the Rust reqwest-middleware crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Wrapper around reqwest to allow for client middleware chains - feature "http2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/http2) >= 0.13.1
Provides:       crate(%{pkgname}/http2) = %{version}

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust reqwest-middleware crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Wrapper around reqwest to allow for client middleware chains - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/json) >= 0.13.1
Requires:       crate(serde-1/default) >= 1.0.106
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust reqwest-middleware crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multipart
Summary:        Wrapper around reqwest to allow for client middleware chains - feature "multipart"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/multipart) >= 0.13.1
Provides:       crate(%{pkgname}/multipart) = %{version}

%description -n %{name}+multipart
This metapackage enables feature "multipart" for the Rust reqwest-middleware crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+query
Summary:        Wrapper around reqwest to allow for client middleware chains - feature "query"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/query) >= 0.13.1
Requires:       crate(serde-1/default) >= 1.0.106
Provides:       crate(%{pkgname}/query) = %{version}

%description -n %{name}+query
This metapackage enables feature "query" for the Rust reqwest-middleware crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Wrapper around reqwest to allow for client middleware chains - feature "rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/rustls) >= 0.13.1
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust reqwest-middleware crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        Wrapper around reqwest to allow for client middleware chains - feature "stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.13/stream) >= 0.13.1
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust reqwest-middleware crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
