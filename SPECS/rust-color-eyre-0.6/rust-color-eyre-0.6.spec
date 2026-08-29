# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name color-eyre
%global full_version 0.6.5
%global pkgname color-eyre-0.6

Name:           rust-color-eyre-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "color-eyre"
License:        MIT OR Apache-2.0
URL:            https://github.com/eyre-rs/eyre
#!RemoteAsset:  sha256:e5920befb47832a6d61ee3a3a846565cfa39b331331e68a3b1d1116630f2f26d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(backtrace-0.3/default) >= 0.3.59
Requires:       crate(eyre-0.6/default) >= 0.6.0
Requires:       crate(indenter-0.3/default) >= 0.3.0
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(owo-colors-4/default) >= 4.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/track-caller) = %{version}

%description
Source code for takopackized Rust crate "color-eyre"

%package     -n %{name}+capture-spantrace
Summary:        Error report handler for panics and eyre::Reports for colorful, consistent, and well formatted error reports for all kinds of errors - feature "capture-spantrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/color-spantrace) = %{version}
Requires:       crate(%{pkgname}/tracing-error) = %{version}
Provides:       crate(%{pkgname}/capture-spantrace) = %{version}

%description -n %{name}+capture-spantrace
This metapackage enables feature "capture-spantrace" for the Rust color-eyre crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color-spantrace
Summary:        Error report handler for panics and eyre::Reports for colorful, consistent, and well formatted error reports for all kinds of errors - feature "color-spantrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(color-spantrace-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/color-spantrace) = %{version}

%description -n %{name}+color-spantrace
This metapackage enables feature "color-spantrace" for the Rust color-eyre crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Error report handler for panics and eyre::Reports for colorful, consistent, and well formatted error reports for all kinds of errors - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/capture-spantrace) = %{version}
Requires:       crate(%{pkgname}/track-caller) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust color-eyre crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-error
Summary:        Error report handler for panics and eyre::Reports for colorful, consistent, and well formatted error reports for all kinds of errors - feature "tracing-error"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-error-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/tracing-error) = %{version}

%description -n %{name}+tracing-error
This metapackage enables feature "tracing-error" for the Rust color-eyre crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        Error report handler for panics and eyre::Reports for colorful, consistent, and well formatted error reports for all kinds of errors - feature "url" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(url-2/default) >= 2.1.1
Provides:       crate(%{pkgname}/issue-url) = %{version}
Provides:       crate(%{pkgname}/url) = %{version}

%description -n %{name}+url
This metapackage enables feature "url" for the Rust color-eyre crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "issue-url" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
