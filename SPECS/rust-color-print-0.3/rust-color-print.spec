# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name color-print
%global full_version 0.3.7
%global pkgname color-print-0.3

Name:           rust-color-print-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "color-print"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/dajoha/color-print
#!RemoteAsset:  sha256:3aa954171903797d5623e047d9ab69d91b493657917bdfb8c2c80ecaf9cdb6f4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(color-print-proc-macro-0.3/default) >= 0.3.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "color-print"

%package     -n %{name}+lazy-static
Summary:        Colorize and stylize strings for terminal at compile-time, by using an HTML-like syntax - feature "lazy_static"
Requires:       crate(%{pkgname})
Requires:       crate(lazy-static-1.0/default) >= 1.4
Provides:       crate(%{pkgname}/lazy-static)

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust color-print crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+terminfo
Summary:        Colorize and stylize strings for terminal at compile-time, by using an HTML-like syntax - feature "terminfo"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/lazy-static)
Requires:       crate(%{pkgname}/terminfo-crate)
Requires:       crate(color-print-proc-macro-0.3/terminfo) >= 0.3.7
Provides:       crate(%{pkgname}/terminfo)

%description -n %{name}+terminfo
This metapackage enables feature "terminfo" for the Rust color-print crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+terminfo-crate
Summary:        Colorize and stylize strings for terminal at compile-time, by using an HTML-like syntax - feature "terminfo_crate"
Requires:       crate(%{pkgname})
Requires:       crate(terminfo-0.7/default) >= 0.7.3
Provides:       crate(%{pkgname}/terminfo-crate)

%description -n %{name}+terminfo-crate
This metapackage enables feature "terminfo_crate" for the Rust color-print crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
